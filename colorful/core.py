# -*- coding: utf-8 -*-

"""
    colorful
    ~~~~~~~~

    Terminal string styling done right, in Python.

    :copyright: (c) 2017 by Timo Furrer <tuxtimo@gmail.com>
    :license: MIT, see LICENSE for more details.
"""

from . import ansi
from . import rgb
from . import utils

# For the ANSI escape code sequences please consult
# https://en.wikipedia.org/wiki/ANSI_escape_code

#: Holds the color names mapped to RGB channels
COLOR_NAMES = rgb.parse_rgb_txt_file()

#: Holds the modifier names in the correct order
MODIFIER_NAMES = ['reset', 'bold', 'dimmed', 'italic', 'underlined',
                  'blinkslow', 'blinkrapid', 'inversed', 'concealed', 'struckthrough']

#: Holds the start index for the fore- and background colors
BACKGROUND_COLOR_OFFSET = 40
FOREGROUND_COLOR_OFFSET = 30

#: Holds the base ANSI escape code
ANSI_ESCAPE_CODE = '\033[{code}m'


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
    if colormode == 0:  # colors are disabled, thus return empty string
        return ''

    if colormode == 8 or colormode == 16:
        color_code = ansi.rgb_to_ansi16(red, green, blue)
        return ANSI_ESCAPE_CODE.format(code=color_code + offset - FOREGROUND_COLOR_OFFSET)

    if colormode == 256:
        color_code = ansi.rgb_to_ansi265(red, green, blue)
        return ANSI_ESCAPE_CODE.format(code='{base};5;{code}'.format(
            base=8 + offset, code=color_code))

    if colormode == 0xFFFFFF:
        return ANSI_ESCAPE_CODE.format(code='{base};2;{red};{green};{blue}'.format(
            base=8 + offset, red=red, green=green, blue=blue))

    raise ColorfulError('invalid color mode "{0}"'.format(colormode))


def translate_colorname_to_ansi_code(colorname, offset, colormode):
    """
    Translate the given color name to a valid
    ANSI escape code.

    :parma str colorname: the name of the color to resolve
    :parma str offset: the offset for the color code
    :param int colormode: the color mode to use. See ``translate_rgb_to_ansi_code``

    :returns str: the color as ANSI escape code

    :raises ColorfulError: if the given color name is invalid
    """
    try:
        red, green, blue = COLOR_NAMES[colorname]
    except KeyError:
        raise ColorfulError('the color "{0}" is unknown. Use X11 rgb.txt valid color name'.format(
            colorname))
    else:
        return translate_rgb_to_ansi_code(red, green, blue, offset, colormode)


def translate_hex_to_ansi_code(value, offset, colormode):
    """
    Translate the given RGB hex value to a valid
    ANSI escape code.

    :param str value: the RGB hex value
    :param str offset: the offset for the color code
    :param int colormode: the color mode to use. See ``translate_rgb_to_ansi_code``

    :returns str: the color as ANSI escape code
    """
    red, green, blue = utils.hex_to_rgb(value)
    return translate_rgb_to_ansi_code(red, green, blue, offset, colormode)


def resolve_modifier_to_ansi_code(modifiername):
    """
    Resolve the given modifier name to a valid
    ANSI escape code.

    :param str modifiername: the name of the modifier to resolve

    :returns str: the ANSI escape code for the modifier

    :raises ColorfulError: if the given modifier name is invalid
    """
    try:
        code = MODIFIER_NAMES.index(modifiername)
    except ValueError:
        raise ColorfulError('the modifier "{0}" is unknown. Use one of: {1}'.format(
            modifiername, MODIFIER_NAMES))
    else:
        return ANSI_ESCAPE_CODE.format(code=code)


def translate_style(style, colormode):
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
    """
    style_parts = iter(style.split('_'))

    ansi_sequence = []

    try:
        # consume all modifiers
        part = None
        for mod_part in style_parts:
            part = mod_part
            if part not in MODIFIER_NAMES:
                break  # all modifiers have been consumed

            ansi_sequence.append(resolve_modifier_to_ansi_code(part))
        else:  # we've consumed all parts, thus we can exit
            raise StopIteration()

        # next part has to be a foreground color or the 'on' keyword
        # which means we have to consume background colors
        if part != 'on':
            ansi_sequence.append(translate_colorname_to_ansi_code(part,
                                                                  FOREGROUND_COLOR_OFFSET, colormode))
            # consume the required 'on' keyword after the foreground color
            next(style_parts)

        # next part has to be the background color
        part = next(style_parts)
        ansi_sequence.append(translate_colorname_to_ansi_code(part, BACKGROUND_COLOR_OFFSET,
                                                              colormode))
    except StopIteration:  # we've consumed all parts of the styling string
        pass

    # construct and return ANSI escape code sequence
    return ''.join(ansi_sequence)


def style_string(string, ansi_style):
    """
    Style the given string according to the given
    ANSI style string.

    :param str string: the string to style
    :param str ansi_style: the styling string returned by ``translate_style``

    :returns: a string containing proper ANSI sequence
    """
    return '{style}{string}{reset}'.format(
        style=ansi_style,
        string=string,
        reset=resolve_modifier_to_ansi_code('reset'))


class Colorful(object):
    """
    Provides methods to style strings for terminal
    output.

    :param int colormode: the color mode to use. See ``translate_rgb_to_ansi_code``
    """
    def __init__(self, colormode):
        self.colormode = colormode

    def __getattr__(self, name):

        # translate the given name into an ANSI escape code sequence
        style = translate_style(name, self.colormode)

        def __style_wrapper(string):
            """
            Style the given string according to the methods
            style string which happens to be the name of the
            method.

            :param str string: the string to style
            """
            return style_string(string, style)

        return __style_wrapper
