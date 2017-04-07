# -*- coding: utf-8 -*-

"""
    colorful
    ~~~~~~~~

    Terminal string styling done right, in Python.

    :copyright: (c) 2017 by Timo Furrer <tuxtimo@gmail.com>
    :license: MIT, see LICENSE for more details.
"""

# For the ANSI escape code sequences please consult
# https://en.wikipedia.org/wiki/ANSI_escape_code

#: Holds the color names in the correct order
COLOR_NAMES = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
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


def resolve_color_to_ansi_code(colorname, offset):
    """
    Resolve the given color name to a valid
    ANSI escape code.

    :parma str colorname: the name of the color to resolve
    :parma str offset: the offset for the color code

    :returns str: the color as ANSI escape code

    :raises ColorfulError: if the given color name is invalid
    """
    try:
        index = COLOR_NAMES.index(colorname)
    except ValueError:
        raise ColorfulError('the color "{0}" is unknown. Use one of: {1}'.format(
            colorname, COLOR_NAMES))
    else:

        return ANSI_ESCAPE_CODE.format(code=offset + index)


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


def translate_style(style):
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
            ansi_sequence.append(resolve_color_to_ansi_code(part, FOREGROUND_COLOR_OFFSET))
            # consume the required 'on' keyword after the foreground color
            next(style_parts)

        # next part has to be the background color
        part = next(style_parts)
        ansi_sequence.append(resolve_color_to_ansi_code(part, BACKGROUND_COLOR_OFFSET))
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
    """
    def __getattr__(self, name):

        # translate the given name into an ANSI escape code sequence
        style = translate_style(name)

        def __style_wrapper(string):
            """
            Style the given string according to the methods
            style string which happens to be the name of the
            method.

            :param str string: the string to style
            """
            return style_string(string, style)

        return __style_wrapper
