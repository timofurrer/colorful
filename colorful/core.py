# -*- coding: utf-8 -*-

"""
    colorful
    ~~~~~~~~

    Terminal string styling done right, in Python.

    :copyright: (c) 2017 by Timo Furrer <tuxtimo@gmail.com>
    :license: MIT, see LICENSE for more details.
"""

import os
import sys

from . import ansi
from . import rgb
from . import styles
from . import terminal

#: Holds the color names mapped to RGB channels
COLOR_PALETTE = rgb.parse_rgb_txt_file()

#: Holds a flag if the Python version is 2.X
PY2 = sys.version_info.major == 2


class ColorfulError(Exception):
    """
    Exception which is raised for Colorful specific
    usage errors.
    """
    pass


def translate_rgb_to_ansi_code(red, green, blue, offset, colormode):
    """
    Translate the given RGB color into the appropriate ANSI escape code
    for the given color mode.
    The offset is used for the base color which is used.

    The ``colormode`` has to be one of:
        * 0: no colors / disabled
        * 8: use ANSI 8bit colors
        * 16: use ANSI 16bit colors (same as 8bit but with brightness)
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

    if colormode == terminal.ANSI_8BIT_COLORS or colormode == terminal.ANSI_16BIT_COLORS:
        color_code = ansi.rgb_to_ansi16(red, green, blue)
        start_code = ansi.ANSI_ESCAPE_CODE.format(
            code=color_code + offset - ansi.FOREGROUND_COLOR_OFFSET)
        end_code = ansi.ANSI_ESCAPE_CODE.format(code=offset + ansi.COLOR_CLOSE_OFFSET)
        return start_code, end_code

    if colormode == terminal.ANSI_256_COLORS:
        color_code = ansi.rgb_to_ansi265(red, green, blue)
        start_code = ansi.ANSI_ESCAPE_CODE.format(code='{base};5;{code}'.format(
            base=8 + offset, code=color_code))
        end_code = ansi.ANSI_ESCAPE_CODE.format(code=offset + ansi.COLOR_CLOSE_OFFSET)
        return start_code, end_code

    if colormode == terminal.TRUE_COLORS:
        start_code = ansi.ANSI_ESCAPE_CODE.format(code='{base};2;{red};{green};{blue}'.format(
            base=8 + offset, red=red, green=green, blue=blue))
        end_code = ansi.ANSI_ESCAPE_CODE.format(code=offset + ansi.COLOR_CLOSE_OFFSET)
        return start_code, end_code

    raise ColorfulError('invalid color mode "{0}"'.format(colormode))


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
        raise ColorfulError('the color "{0}" is unknown. Use a color in your color palette (by default: X11 rgb.txt)'.format(  # noqa
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
        raise ColorfulError('the modifier "{0}" is unknown. Use one of: {1}'.format(
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
    string = string.replace(ansi.NEST_PLACEHOLDER, ansi_start_code)

    return '{start_code}{string}{end_code}{nest_ph}'.format(
        start_code=ansi_start_code,
        string=string,
        end_code=ansi_end_code,
        nest_ph=ansi.NEST_PLACEHOLDER if nested else '')


class ColorfulString(object):
    """
    Represents a colored string
    """
    def __init__(self, orig_string, styled_string):
        self.orig_string = orig_string
        self.styled_string = styled_string

    def __str__(self):
        return self.styled_string

    if PY2:
        __unicode__ = __str__

    def __len__(self):
        return len(self.orig_string)

    def __iter__(self):
        return iter(self.styled_string)

    def __add__(self, other):
        if isinstance(other, ColorfulString):
            return ColorfulString(
                self.orig_string + other.orig_string,
                self.styled_string + other.styled_string)

        return ColorfulString(
            self.orig_string + other,
            self.styled_string + other)

    def __radd__(self, other):
        if isinstance(other, ColorfulString):
            return ColorfulString(
                other.orig_string + self.orig_string,
                other.styled_string + self.styled_string)

        return ColorfulString(
            other + self.orig_string,
            other + self.styled_string)

    def __mul__(self, other):
        return ColorfulString(
            self.orig_string * other,
            self.styled_string * other)

    def __getattr__(self, name):
        str_method = getattr(self.styled_string, name)
        return str_method


class Colorful(object):
    """
    Provides methods to style strings for terminal
    output.

    :param int colormode: the color mode to use. See ``translate_rgb_to_ansi_code``
    """
    # re-expose the color modes from ``colorful.terminal``
    # on a package level.
    NO_COLORS = terminal.NO_COLORS
    ANSI_8BIT_COLORS = terminal.ANSI_8BIT_COLORS
    ANSI_16BIT_COLORS = terminal.ANSI_16BIT_COLORS
    ANSI_256_COLORS = terminal.ANSI_256_COLORS
    TRUE_COLORS = terminal.TRUE_COLORS

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
    no_underline = ansi.ANSI_ESCAPE_CODE.format(code=ansi.MODIFIERS['underlined'][1])
    no_blink = ansi.ANSI_ESCAPE_CODE.format(code=ansi.MODIFIERS['blinkslow'][1])
    no_inversed = ansi.ANSI_ESCAPE_CODE.format(code=ansi.MODIFIERS['inversed'][1])
    no_reveal = ansi.ANSI_ESCAPE_CODE.format(code=ansi.MODIFIERS['concealed'][1])
    no_strikethrough = ansi.ANSI_ESCAPE_CODE.format(code=ansi.MODIFIERS['struckthrough'][1])

    def __init__(self, colormode=None, colorpalette=None):
        if colormode is None:  # try to auto-detect color mode
            colormode = terminal.detect_color_support(env=os.environ)

        if colorpalette is None:  # load default color palette
            colorpalette = COLOR_PALETTE
        elif isinstance(colorpalette, str):  # we assume it's a path to a X11 rgb.txt
            colorpalette = rgb.parse_rgb_txt_file(colorpalette)

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
        self._colorpalette = rgb.sanitize_color_palette(colorpalette)

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
        if colormode:
            self.colormode = colormode

        if colorpalette:
            if extend_colors:
                self.update_palette(colorpalette)
            else:
                self.colorpalette = colorpalette

    def use_8bit_ansi_colors(self):
        """
        Use 8bit ANSI colors for this colorful object
        """
        self.colormode = terminal.ANSI_8BIT_COLORS

    def use_16bit_ansi_colors(self):
        """
        Use 16bit ANSI colors for this colorful object
        """
        self.colormode = terminal.ANSI_16BIT_COLORS

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
        self.colorpalette.update(rgb.sanitize_color_palette(colorpalette))

    def use_style(self, style_name):
        """
        Use a predefined style as color palette

        :param str style_name: the name of the style
        """
        try:
            style = getattr(styles, style_name.upper())
        except AttributeError:
            raise ColorfulError('the style "{0}" is undefined'.format(
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

    class ColorfulStyle(object):
        """
        Represents a colorful style
        """
        def __init__(self, style, colormode):
            self.style = style
            self.colormode = colormode

        def __str__(self):
            return self.style[0]

        def __call__(self, string, nested=False):
            return ColorfulString(
                string,
                style_string(string, self.style, self.colormode, nested))

    def __getattr__(self, name):
        # translate the given name into an ANSI escape code sequence
        style = translate_style(name, self.colormode, self.colorpalette)
        style_wrapper = self.ColorfulStyle(style, self.colormode)
        return style_wrapper
