"""
colorful
~~~~~~~~

Terminal string styling done right, in Python.

:copyright: (c) 2017 by Timo Furrer <tuxtimo@gmail.com>
:license: MIT, see LICENSE for more details.
"""

import os

from . import ansi
from . import colors
from . import styles
from . import terminal

#: Holds the name of the env variable which is
#  used as path to the default rgb.txt file
DEFAULT_RGB_TXT_PATH = os.environ.get(
    'COLORFUL_DEFAULT_COLOR_PALETTE',
    os.path.join(os.path.dirname(__file__), 'data', 'rgb.txt'))

#: Holds the color names mapped to RGB channels
COLOR_PALETTE = colors.parse_colors(path=DEFAULT_RGB_TXT_PATH)

#: Holds the path to the built-in `colornames` color palette file
COLORNAMES_COLORS_PATH = os.path.join(os.path.dirname(__file__), "data", "colornames.json")


class ColorfulError(Exception):
    """
    Exception which is raised for Colorful specific
    usage errors.
    """


class ColorfulAttributeError(AttributeError, ColorfulError):
    """
    Exception which is raised for Colorful specific
    usage errors raised during ``__getattr__`` calls.

    This is to ensure a correct ``__getattr__`` protocol implementation.
    """


def translate_rgb_to_ansi_code(red, green, blue, offset, colormode):
    """
    Translate the given RGB color into the appropriate ANSI escape code
    for the given color mode.
    The offset is used for the base color which is used.

    The ``colormode`` has to be one of:
        * 0: no colors / disabled
        * 8: use ANSI 8 colors
        * 16: use ANSI 16 colors (same as 8 but with brightness)
        * 256: use ANSI 256 colors
        * 0xFFFFFF / 16777215: use 16 Million true colors

    :param int red: the red channel value
    :param int green: the green channel value
    :param int blue: the blue channel value
    :param int offset: the offset to use for the base color
    :param int colormode: the color mode to use. See explanation above
    """
    if colormode == terminal.NO_COLORS:  # colors are disabled, thus return empty string
        return '', ''

    if colormode == terminal.ANSI_8_COLORS or colormode == terminal.ANSI_16_COLORS:
        color_code = ansi.rgb_to_ansi16(red, green, blue)
        start_code = ansi.ANSI_ESCAPE_CODE.format(
            code=color_code + offset - ansi.FOREGROUND_COLOR_OFFSET)
        end_code = ansi.ANSI_ESCAPE_CODE.format(code=offset + ansi.COLOR_CLOSE_OFFSET)
        return start_code, end_code

    if colormode == terminal.ANSI_256_COLORS:
        color_code = ansi.rgb_to_ansi256(red, green, blue)
        start_code = ansi.ANSI_ESCAPE_CODE.format(code='{base};5;{code}'.format(
            base=8 + offset, code=color_code))
        end_code = ansi.ANSI_ESCAPE_CODE.format(code=offset + ansi.COLOR_CLOSE_OFFSET)
        return start_code, end_code

    if colormode == terminal.TRUE_COLORS:
        start_code = ansi.ANSI_ESCAPE_CODE.format(code='{base};2;{red};{green};{blue}'.format(
            base=8 + offset, red=red, green=green, blue=blue))
        end_code = ansi.ANSI_ESCAPE_CODE.format(code=offset + ansi.COLOR_CLOSE_OFFSET)
        return start_code, end_code

    raise ColorfulAttributeError('invalid color mode "{}"'.format(colormode))


def translate_colorname_to_ansi_code(colorname, offset, colormode, colorpalette):
    """
    Translate the given color name to a valid
    ANSI escape code.

    :parma str colorname: the name of the color to resolve
    :parma str offset: the offset for the color code
    :param int colormode: the color mode to use. See ``translate_rgb_to_ansi_code``
    :parma dict colorpalette: the color palette to use for the color name mapping

    :returns str: the color as ANSI escape code

    :raises ColorfulError: if the given color name is invalid
    """
    try:
        red, green, blue = colorpalette[colorname]
    except KeyError:
        raise ColorfulAttributeError('the color "{}" is unknown. Use a color in your color palette (by default: X11 rgb.txt)'.format(  # noqa
            colorname))
    else:
        return translate_rgb_to_ansi_code(red, green, blue, offset, colormode)


def resolve_modifier_to_ansi_code(modifiername, colormode):
    """
    Resolve the given modifier name to a valid
    ANSI escape code.

    :param str modifiername: the name of the modifier to resolve
    :param int colormode: the color mode to use. See ``translate_rgb_to_ansi_code``

    :returns str: the ANSI escape code for the modifier

    :raises ColorfulError: if the given modifier name is invalid
    """
    if colormode == terminal.NO_COLORS:  # return empty string if colors are disabled
        return '', ''

    try:
        start_code, end_code = ansi.MODIFIERS[modifiername]
    except KeyError:
        raise ColorfulAttributeError('the modifier "{}" is unknown. Use one of: {}'.format(
            modifiername, ansi.MODIFIERS.keys()))
    else:
        return ansi.ANSI_ESCAPE_CODE.format(
            code=start_code), ansi.ANSI_ESCAPE_CODE.format(
                code=end_code)


def translate_style(style, colormode, colorpalette):
    """
    Translate the given style to an ANSI escape code
    sequence.

    ``style`` examples are:

    * green
    * bold
    * red_on_black
    * bold_green
    * italic_yellow_on_cyan

    :param str style: the style to translate
    :param int colormode: the color mode to use. See ``translate_rgb_to_ansi_code``
    :parma dict colorpalette: the color palette to use for the color name mapping
    """
    style_parts = iter(style.split('_'))

    ansi_start_sequence = []
    ansi_end_sequence = []

    try:
        # consume all modifiers
        part = None
        for mod_part in style_parts:
            part = mod_part
            if part not in ansi.MODIFIERS:
                break  # all modifiers have been consumed

            mod_start_code, mod_end_code = resolve_modifier_to_ansi_code(part, colormode)
            ansi_start_sequence.append(mod_start_code)
            ansi_end_sequence.append(mod_end_code)
        else:  # we've consumed all parts, thus we can exit
            raise StopIteration()

        # next part has to be a foreground color or the 'on' keyword
        # which means we have to consume background colors
        if part != 'on':
            ansi_start_code, ansi_end_code = translate_colorname_to_ansi_code(
                part, ansi.FOREGROUND_COLOR_OFFSET, colormode, colorpalette)
            ansi_start_sequence.append(ansi_start_code)
            ansi_end_sequence.append(ansi_end_code)
            # consume the required 'on' keyword after the foreground color
            next(style_parts)

        # next part has to be the background color
        part = next(style_parts)
        ansi_start_code, ansi_end_code = translate_colorname_to_ansi_code(
            part, ansi.BACKGROUND_COLOR_OFFSET, colormode, colorpalette)
        ansi_start_sequence.append(ansi_start_code)
        ansi_end_sequence.append(ansi_end_code)
    except StopIteration:  # we've consumed all parts of the styling string
        pass

    # construct and return ANSI escape code sequence
    return ''.join(ansi_start_sequence), ''.join(ansi_end_sequence)


def style_string(string, ansi_style, colormode, nested=False):
    """
    Style the given string according to the given
    ANSI style string.

    :param str string: the string to style
    :param tuple ansi_style: the styling string returned by ``translate_style``
    :param int colormode: the color mode to use. See ``translate_rgb_to_ansi_code``

    :returns: a string containing proper ANSI sequence
    """
    ansi_start_code, ansi_end_code = ansi_style

    # replace nest placeholders with the current begin style
    string = str(string).replace(ansi.NEST_PLACEHOLDER, ansi_start_code)

    return '{start_code}{string}{end_code}{nest_ph}'.format(
            start_code=ansi_start_code,
            string=string,
            end_code=ansi_end_code,
            nest_ph=ansi.NEST_PLACEHOLDER if nested else '')


class ColorfulString():
    """
    Represents a colored string
    """
    def __init__(self, orig_string, styled_string, colorful_ctx):
        self.orig_string = str(orig_string)
        self.styled_string = str(styled_string)
        self.colorful_ctx = colorful_ctx

    def __str__(self):
        if self.colorful_ctx.colormode == terminal.NO_COLORS:
            return self.orig_string
        else:
            return self.styled_string

    def __len__(self):
        return len(self.orig_string)

    def __iter__(self):
        return iter(self.styled_string)

    def __add__(self, other):
        if isinstance(other, ColorfulString):
            return ColorfulString(
                self.orig_string + other.orig_string,
                self.styled_string + other.styled_string,
                self.colorful_ctx)

        return ColorfulString(
            self.orig_string + other,
            self.styled_string + other,
            self.colorful_ctx)

    def __iadd__(self, other):
        if isinstance(other, ColorfulString):
            self.orig_string += other.orig_string
            self.styled_string += other.styled_string
        else:
            self.orig_string += other
            self.styled_string += other

        return self

    def __radd__(self, other):
        if isinstance(other, ColorfulString):
            return ColorfulString(
                other.orig_string + self.orig_string,
                other.styled_string + self.styled_string,
                self.colorful_ctx)

        # we return handover the conversion to the
        # object on the left side
        return other + self.styled_string

    def __mul__(self, other):
        return ColorfulString(
            self.orig_string * other,
            self.styled_string * other,
            self.colorful_ctx)

    def __format__(self, format_spec):
        if self.colorful_ctx.colormode == terminal.NO_COLORS:
            return self.orig_string.__format__(format_spec)

        # append nested placeholder to styled string in order to continue the
        # previous styles. If the string already ends with the nest placeholder
        # we don't have to append it again.
        if self.styled_string.endswith(ansi.NEST_PLACEHOLDER):
            styled_string = self.styled_string
        else:
            styled_string = '{orig_str}{nest_ph}'.format(
                orig_str=self.styled_string, nest_ph=ansi.NEST_PLACEHOLDER)
        return styled_string.__format__(format_spec)

    def __getattr__(self, name):
        str_method = getattr(self.styled_string, name)
        return str_method


class Colorful():
    """
    Provides methods to style strings for terminal
    output.

    :param int colormode: the color mode to use. See ``translate_rgb_to_ansi_code``
    """
    # re-expose the color modes from ``colorful.terminal``
    # on a package level.
    NO_COLORS = terminal.NO_COLORS
    ANSI_8_COLORS = terminal.ANSI_8_COLORS
    ANSI_16_COLORS = terminal.ANSI_16_COLORS
    ANSI_256_COLORS = terminal.ANSI_256_COLORS
    TRUE_COLORS = terminal.TRUE_COLORS

    # expose the `colornames` color palette
    COLORNAMES_COLORS = COLORNAMES_COLORS_PATH

    # expose ANSI escape codes to close colors
    # this is especially useful when using ``str.format()``.
    close_fg_color = ansi.ANSI_ESCAPE_CODE.format(
        code=ansi.FOREGROUND_COLOR_OFFSET + ansi.COLOR_CLOSE_OFFSET)
    close_bg_color = ansi.ANSI_ESCAPE_CODE.format(
        code=ansi.BACKGROUND_COLOR_OFFSET + ansi.COLOR_CLOSE_OFFSET)

    # expose ANSI escape codes to close modifiers
    no_bold = ansi.ANSI_ESCAPE_CODE.format(code=ansi.MODIFIERS['bold'][1])
    no_dimmed = ansi.ANSI_ESCAPE_CODE.format(code=ansi.MODIFIERS['dimmed'][1])
    no_italic = ansi.ANSI_ESCAPE_CODE.format(code=ansi.MODIFIERS['italic'][1])
    no_underlined = ansi.ANSI_ESCAPE_CODE.format(code=ansi.MODIFIERS['underlined'][1])
    no_blinkslow = ansi.ANSI_ESCAPE_CODE.format(code=ansi.MODIFIERS['blinkslow'][1])
    no_blinkrapid = ansi.ANSI_ESCAPE_CODE.format(code=ansi.MODIFIERS['blinkrapid'][1])
    no_inversed = ansi.ANSI_ESCAPE_CODE.format(code=ansi.MODIFIERS['inversed'][1])
    no_concealed = ansi.ANSI_ESCAPE_CODE.format(code=ansi.MODIFIERS['concealed'][1])
    no_struckthrough = ansi.ANSI_ESCAPE_CODE.format(code=ansi.MODIFIERS['struckthrough'][1])

    def __init__(self, colormode=None, colorpalette=None):
        if colormode is None:  # try to auto-detect color mode
            colormode = terminal.detect_color_support(env=os.environ)

        if colorpalette is None:  # load default color palette
            colorpalette = COLOR_PALETTE
        elif isinstance(colorpalette, str):  # we assume it's a path to a color file
            colorpalette = colors.parse_colors(colorpalette)

        #: Holds the color mode to use for this Colorful object.
        self.colormode = colormode

        #: Holds the color palette to use for this Colorful object.
        self._colorpalette = None
        self.colorpalette = colorpalette

    @property
    def colorpalette(self):
        """
        Get the current used color palette
        """
        return self._colorpalette

    @colorpalette.setter
    def colorpalette(self, colorpalette):
        """
        Set the colorpalette which should be used
        """
        if isinstance(colorpalette, str):  # we assume it's a path to a color file
            colorpalette = colors.parse_colors(colorpalette)

        self._colorpalette = colors.sanitize_color_palette(colorpalette)

    def setup(self, colormode=None, colorpalette=None, extend_colors=False):
        """
        Setup this colorful object by setting a ``colormode`` and
        the ``colorpalette`. The ``extend_colors`` flag is used
        to extend the currently active color palette instead of
        replacing it.

        :param int colormode: the color mode to use. See ``translate_rgb_to_ansi_code``
        :parma dict colorpalette: the colorpalette to use. This ``dict`` should map
                                  color names to it's corresponding RGB value
        :param bool extend_colors: extend the active color palette instead of replacing it
        """
        if colormode is not None:
            self.colormode = colormode

        if colorpalette:
            if extend_colors:
                self.update_palette(colorpalette)
            else:
                self.colorpalette = colorpalette

    def disable(self):
        """
        Disable all colors and styles
        """
        self.colormode = terminal.NO_COLORS

    def use_8_ansi_colors(self):
        """
        Use 8 ANSI colors for this colorful object
        """
        self.colormode = terminal.ANSI_8_COLORS

    def use_16_ansi_colors(self):
        """
        Use 16 ANSI colors for this colorful object
        """
        self.colormode = terminal.ANSI_16_COLORS

    def use_256_ansi_colors(self):
        """
        Use 256 ANSI colors for this colorful object
        """
        self.colormode = terminal.ANSI_256_COLORS

    def use_true_colors(self):
        """
        Use true colors for this colorful object
        """
        self.colormode = terminal.TRUE_COLORS

    def use_palette(self, colorpalette):
        """
        Use the given color palette
        """
        self.colorpalette = colorpalette

    def update_palette(self, colorpalette):
        """
        Update the currently active color palette
        with the given color palette
        """
        self.colorpalette.update(colors.sanitize_color_palette(colorpalette))

    def use_style(self, style_name):
        """
        Use a predefined style as color palette

        :param str style_name: the name of the style
        """
        try:
            style = getattr(styles, style_name.upper())
        except AttributeError:
            raise ColorfulError('the style "{}" is undefined'.format(
                style_name))
        else:
            self.colorpalette = style

    def format(self, string, *args, **kwargs):
        """
        Format the given string with the given ``args`` and ``kwargs``.
        The string can contain references to ``c`` which is provided by
        this colorful object.

        :param str string: the string to format
        """
        return string.format(c=self, *args, **kwargs)

    def str(self, string):
        """
        Create a new ColorfulString instance of the given
        unstyled string.

        This method should be used to create a ColorfulString
        which is actually not styled yet but can safely be concatinated
        with other ColorfulStrings like:

        >>> s = colorful.str('Hello ')
        >>> s =+ colorful.black('World')
        >>> str(s)
        'Hello \033[30mWorld\033[39m'

        :param str string: the string to use for the ColorfulString
        """
        return ColorfulString(string, string, self)

    def print(self, *objects, sep=' ', end='\n', file=None, flush=False):
        """
        Print the given objects to the given file stream.
        See https://docs.python.org/3/library/functions.html#print

        The only difference to the ``print()`` built-in is that
        ``Colorful.print()`` formats the string with ``c=self``.
        With that stylings are possible

        :param str sep: the seperater between the objects
        :param str end: the ending delimiter after all objects
        :param file: the file stream to write to
        :param bool flush: if the stream should be flushed
        """
        styled_objects = [self.format(o) for o in objects]
        print(*styled_objects, sep=sep, end=end, file=file, flush=flush)

    class ColorfulStyle():
        """
        Represents a colorful style
        """
        def __init__(self, style, colormode, colorful_ctx):
            self.style = style
            self.colormode = colormode
            self.colorful_ctx = colorful_ctx

        def evaluate(self, string, nested=False):
            """
            Evaluate the style on the given string.

            :parma str string: the string to style
            :param bool nested: if the string is part of another styled string
                                (=> nested in another style)
            """
            return ColorfulString(
                string,
                style_string(string, self.style, self.colormode, nested),
                self.colorful_ctx)

        def __str__(self):
            return self.style[0]

        def __and__(self, other):
            new_style = (
                self.style[0] + other.style[0],
                self.style[1] + other.style[1]
            )
            return Colorful.ColorfulStyle(new_style, self.colormode, self.colorful_ctx)

        def __call__(self, string, nested=False):
            return self.evaluate(string, nested)

        def __or__(self, other):
            return self.evaluate(other)

        def __eq__(self, other):
            if not isinstance(other, Colorful.ColorfulStyle):
                return False

            return (
                self.style == other.style and
                self.colormode == other.colormode and
                self.colorful_ctx == other.colorful_ctx
            )

        def __hash__(self):
            return hash((self.style, self.colormode, self.colorful_ctx))

    def __getattr__(self, name):
        # translate the given name into an ANSI escape code sequence
        style = translate_style(name, self.colormode, self.colorpalette)
        style_wrapper = self.ColorfulStyle(style, self.colormode, self)
        return style_wrapper
