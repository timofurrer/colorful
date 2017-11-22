# -*- coding: utf-8 -*-

"""
    colorful
    ~~~~~~~~

    Terminal string styling done right, in Python.

    :copyright: (c) 2017 by Timo Furrer <tuxtimo@gmail.com>
    :license: MIT, see LICENSE for more details.
"""

# NOTE: only used for Colorful.print()
from __future__ import print_function

import os

import pytest

# do not overwrite module
os.environ['COLORFUL_NO_MODULE_OVERWRITE'] = '1'

import colorful.core as core  # noqa
import colorful.terminal as terminal  # noqa


@pytest.mark.parametrize('style_string,expected', [
    # modifiers
    ('bold', ('\033[1m', '\033[22m')),
    ('struckthrough', ('\033[9m', '\033[29m')),
    # foreground colors
    ('black', ('\033[30m', '\033[39m')),
    ('blue', ('\033[34m', '\033[39m')),
    ('white', ('\033[37m', '\033[39m')),
    # background colors
    ('on_black', ('\033[40m', '\033[49m')),
    ('on_blue', ('\033[44m', '\033[49m')),
    ('on_white', ('\033[47m', '\033[49m')),
    # modifiers with foreground colors
    ('bold_black', ('\033[1m\033[30m', '\033[22m\033[39m')),
    ('italic_blue', ('\033[3m\033[34m', '\033[23m\033[39m')),
    ('struckthrough_white', ('\033[9m\033[37m', '\033[29m\033[39m')),
    # modifiers with background colors
    ('bold_on_black', ('\033[1m\033[40m', '\033[22m\033[49m')),
    ('italic_on_blue', ('\033[3m\033[44m', '\033[23m\033[49m')),
    ('struckthrough_on_white', ('\033[9m\033[47m', '\033[29m\033[49m')),
    # modifiers with foreground and background colors
    ('bold_green_on_black', ('\033[1m\033[32m\033[40m', '\033[22m\033[39m\033[49m')),
    ('italic_cyan_on_blue', ('\033[3m\033[36m\033[44m', '\033[23m\033[39m\033[49m')),
    ('struckthrough_yellow_on_white', ('\033[9m\033[33m\033[47m', '\033[29m\033[39m\033[49m')),
    # multiple modifiers
    ('bold_italic', ('\033[1m\033[3m', '\033[22m\033[23m')),
    ('underlined_struckthrough', ('\033[4m\033[9m', '\033[24m\033[29m')),
    # multiple modifiers with foreground colors
    ('bold_italic_green', ('\033[1m\033[3m\033[32m', '\033[22m\033[23m\033[39m')),
    ('underlined_struckthrough_cyan', ('\033[4m\033[9m\033[36m', '\033[24m\033[29m\033[39m'))
])
def test_translate_style_8(style_string, expected):
    """
    Test translating style strings with 8 colors
    """
    assert core.translate_style(style_string, colormode=terminal.ANSI_8_COLORS,
                                colorpalette=core.COLOR_PALETTE) == expected


@pytest.mark.parametrize('style_string,expected', [
    # modifiers
    ('bold', ('\033[1m', '\033[22m')),
    ('struckthrough', ('\033[9m', '\033[29m')),
    # foreground colors
    ('black', ('\033[30m', '\033[39m')),
    ('blue', ('\033[34m', '\033[39m')),
    ('white', ('\033[37m', '\033[39m')),
    # background colors
    ('on_black', ('\033[40m', '\033[49m')),
    ('on_blue', ('\033[44m', '\033[49m')),
    ('on_white', ('\033[47m', '\033[49m')),
    # modifiers with foreground colors
    ('bold_black', ('\033[1m\033[30m', '\033[22m\033[39m')),
    ('italic_blue', ('\033[3m\033[34m', '\033[23m\033[39m')),
    ('struckthrough_white', ('\033[9m\033[37m', '\033[29m\033[39m')),
    # modifiers with background colors
    ('bold_on_black', ('\033[1m\033[40m', '\033[22m\033[49m')),
    ('italic_on_blue', ('\033[3m\033[44m', '\033[23m\033[49m')),
    ('struckthrough_on_white', ('\033[9m\033[47m', '\033[29m\033[49m')),
    # modifiers with foreground and background colors
    ('bold_green_on_black', ('\033[1m\033[32m\033[40m', '\033[22m\033[39m\033[49m')),
    ('italic_cyan_on_blue', ('\033[3m\033[36m\033[44m', '\033[23m\033[39m\033[49m')),
    ('struckthrough_yellow_on_white', ('\033[9m\033[33m\033[47m', '\033[29m\033[39m\033[49m')),
    # multiple modifiers
    ('bold_italic', ('\033[1m\033[3m', '\033[22m\033[23m')),
    ('underlined_struckthrough', ('\033[4m\033[9m', '\033[24m\033[29m')),
    # multiple modifiers with foreground colors
    ('bold_italic_green', ('\033[1m\033[3m\033[32m', '\033[22m\033[23m\033[39m')),
    ('underlined_struckthrough_cyan', ('\033[4m\033[9m\033[36m', '\033[24m\033[29m\033[39m'))
])
def test_translate_style_16(style_string, expected):
    """
    Test translating style strings with 16 colors
    """
    assert core.translate_style(style_string, colormode=terminal.ANSI_16_COLORS,
                                colorpalette=core.COLOR_PALETTE) == expected


@pytest.mark.parametrize('style_string,expected', [
    # modifiers
    ('bold', ('\033[1m', '\033[22m')),
    ('struckthrough', ('\033[9m', '\033[29m')),
    # foreground colors
    ('black', ('\033[38;5;16m', '\033[39m')),
    ('blue', ('\033[38;5;21m', '\033[39m')),
    ('white', ('\033[38;5;231m', '\033[39m')),
    # background colors
    ('on_black', ('\033[48;5;16m', '\033[49m')),
    ('on_blue', ('\033[48;5;21m', '\033[49m')),
    ('on_white', ('\033[48;5;231m', '\033[49m')),
    # modifiers with foreground colors
    ('bold_black', ('\033[1m\033[38;5;16m', '\033[22m\033[39m')),
    ('italic_blue', ('\033[3m\033[38;5;21m', '\033[23m\033[39m')),
    ('struckthrough_white', ('\033[9m\033[38;5;231m', '\033[29m\033[39m')),
    # modifiers with background colors
    ('bold_on_black', ('\033[1m\033[48;5;16m', '\033[22m\033[49m')),
    ('italic_on_blue', ('\033[3m\033[48;5;21m', '\033[23m\033[49m')),
    ('struckthrough_on_white', ('\033[9m\033[48;5;231m', '\033[29m\033[49m')),
    # modifiers with foreground and background colors
    ('bold_green_on_black', ('\033[1m\033[38;5;46m\033[48;5;16m', '\033[22m\033[39m\033[49m')),
    ('italic_cyan_on_blue', ('\033[3m\033[38;5;51m\033[48;5;21m', '\033[23m\033[39m\033[49m')),
    ('struckthrough_yellow_on_white', ('\033[9m\033[38;5;226m\033[48;5;231m', '\033[29m\033[39m\033[49m')),  # noqa
    # multiple modifiers
    ('bold_italic', ('\033[1m\033[3m', '\033[22m\033[23m')),
    ('underlined_struckthrough', ('\033[4m\033[9m', '\033[24m\033[29m')),
    # multiple modifiers with foreground colors
    ('bold_italic_green', ('\033[1m\033[3m\033[38;5;46m', '\033[22m\033[23m\033[39m')),
    ('underlined_struckthrough_cyan', ('\033[4m\033[9m\033[38;5;51m', '\033[24m\033[29m\033[39m'))
])
def test_translate_style_256(style_string, expected):
    """
    Test translating style strings with 256 colors
    """
    assert core.translate_style(style_string, colormode=terminal.ANSI_256_COLORS,
                                colorpalette=core.COLOR_PALETTE) == expected


@pytest.mark.parametrize('style_string,expected', [
    # modifiers
    ('bold', ('\033[1m', '\033[22m')),
    ('struckthrough', ('\033[9m', '\033[29m')),
    # foreground colors
    ('black', ('\033[38;2;0;0;0m', '\033[39m')),
    ('blue', ('\033[38;2;0;0;255m', '\033[39m')),
    ('white', ('\033[38;2;255;255;255m', '\033[39m')),
    # background colors
    ('on_black', ('\033[48;2;0;0;0m', '\033[49m')),
    ('on_blue', ('\033[48;2;0;0;255m', '\033[49m')),
    ('on_white', ('\033[48;2;255;255;255m', '\033[49m')),
    # modifiers with foreground colors
    ('bold_black', ('\033[1m\033[38;2;0;0;0m', '\033[22m\033[39m')),
    ('italic_blue', ('\033[3m\033[38;2;0;0;255m', '\033[23m\033[39m')),
    ('struckthrough_white', ('\033[9m\033[38;2;255;255;255m', '\033[29m\033[39m')),
    # modifiers with background colors
    ('bold_on_black', ('\033[1m\033[48;2;0;0;0m', '\033[22m\033[49m')),
    ('italic_on_blue', ('\033[3m\033[48;2;0;0;255m', '\033[23m\033[49m')),
    ('struckthrough_on_white', ('\033[9m\033[48;2;255;255;255m', '\033[29m\033[49m')),
    # modifiers with foreground and background colors
    ('bold_green_on_black', ('\033[1m\033[38;2;0;255;0m\033[48;2;0;0;0m', '\033[22m\033[39m\033[49m')),  # noqa
    ('italic_cyan_on_blue', ('\033[3m\033[38;2;0;255;255m\033[48;2;0;0;255m', '\033[23m\033[39m\033[49m')),  # noqa
    ('struckthrough_yellow_on_white', ('\033[9m\033[38;2;255;255;0m\033[48;2;255;255;255m', '\033[29m\033[39m\033[49m')),  # noqa
    # multiple modifiers
    ('bold_italic', ('\033[1m\033[3m', '\033[22m\033[23m')),
    ('underlined_struckthrough', ('\033[4m\033[9m', '\033[24m\033[29m')),
    # multiple modifiers with foreground colors
    ('bold_italic_green', ('\033[1m\033[3m\033[38;2;0;255;0m', '\033[22m\033[23m\033[39m')),
    ('underlined_struckthrough_cyan', ('\033[4m\033[9m\033[38;2;0;255;255m', '\033[24m\033[29m\033[39m'))  # noqa
])
def test_translate_style_true_colors(style_string, expected):
    """
    Test translating style strings with true colors
    """
    assert core.translate_style(style_string, colormode=terminal.TRUE_COLORS,
                                colorpalette=core.COLOR_PALETTE) == expected


@pytest.mark.parametrize('method_name,expected', [
    ('bold', '\033[1mNo, I am your father\033[22m'),
    ('struckthrough', '\033[9mNo, I am your father\033[29m'),
    # foreground colors
    ('black', '\033[30mNo, I am your father\033[39m'),
    ('blue', '\033[34mNo, I am your father\033[39m'),
    ('white', '\033[37mNo, I am your father\033[39m'),
    # background colors
    ('on_black', '\033[40mNo, I am your father\033[49m'),
    ('on_blue', '\033[44mNo, I am your father\033[49m'),
    ('on_white', '\033[47mNo, I am your father\033[49m'),
    # modifiers with foreground colors
    ('bold_black', '\033[1m\033[30mNo, I am your father\033[22m\033[39m'),
    ('italic_blue', '\033[3m\033[34mNo, I am your father\033[23m\033[39m'),
    ('struckthrough_white', '\033[9m\033[37mNo, I am your father\033[29m\033[39m'),
    # modifiers with background colors
    ('bold_on_black', '\033[1m\033[40mNo, I am your father\033[22m\033[49m'),
    ('italic_on_blue', '\033[3m\033[44mNo, I am your father\033[23m\033[49m'),
    ('struckthrough_on_white', '\033[9m\033[47mNo, I am your father\033[29m\033[49m'),
    # modifiers with foreground and background colors
    ('bold_green_on_black', '\033[1m\033[32m\033[40mNo, I am your father\033[22m\033[39m\033[49m'),
    ('italic_cyan_on_blue', '\033[3m\033[36m\033[44mNo, I am your father\033[23m\033[39m\033[49m'),
    ('struckthrough_yellow_on_white', '\033[9m\033[33m\033[47mNo, I am your father\033[29m\033[39m\033[49m'),  # noqa
    # multiple modifiers
    ('bold_italic', '\033[1m\033[3mNo, I am your father\033[22m\033[23m'),
    ('underlined_struckthrough', '\033[4m\033[9mNo, I am your father\033[24m\033[29m'),
    # multiple modifiers with foreground colors
    ('bold_italic_green', '\033[1m\033[3m\033[32mNo, I am your father\033[22m\033[23m\033[39m'),
    ('underlined_struckthrough_cyan', '\033[4m\033[9m\033[36mNo, I am your father\033[24m\033[29m\033[39m')  # noqa
])
def test_method_call_to_style_conversion(method_name, expected):
    """
    Test converting the method call to an actual style
    """
    colorful = core.Colorful(colormode=terminal.ANSI_8_COLORS)
    method = getattr(colorful, method_name)

    assert str(method('No, I am your father')) == expected


@pytest.mark.parametrize('method_name', [
    ('bold'),
    ('struckthrough'),
    # foreground colors
    ('black'),
    ('blue'),
    ('white'),
    # background colors
    ('on_black'),
    ('on_blue'),
    ('on_white'),
    # modifiers with foreground colors
    ('bold_black'),
    ('italic_blue'),
    ('struckthrough_white'),
    # modifiers with background colors
    ('bold_on_black'),
    ('italic_on_blue'),
    ('struckthrough_on_white'),
    # modifiers with foreground and background colors
    ('bold_green_on_black'),
    ('italic_cyan_on_blue'),
    ('struckthrough_yellow_on_white'),
    # multiple modifiers
    ('bold_italic'),
    ('underlined_struckthrough'),
    # multiple modifiers with foreground colors
    ('bold_italic_green'),
    ('underlined_struckthrough_cyan'),
])
def test_method_call_to_style_conversion_disabled_colors(method_name):
    """
    Test converting the method call to an actual style with disabled colors
    """
    colorful = core.Colorful(colormode=terminal.NO_COLORS)
    method = getattr(colorful, method_name)

    assert str(method('No, I am your father')) == 'No, I am your father'


@pytest.mark.parametrize('method_name,expected', [
    ('bold', '\033[1m'),
    ('struckthrough', '\033[9m'),
    # foreground colors
    ('black', '\033[30m'),
    ('blue', '\033[34m'),
    ('white', '\033[37m'),
    # background colors
    ('on_black', '\033[40m'),
    ('on_blue', '\033[44m'),
    ('on_white', '\033[47m'),
    # modifiers with foreground colors
    ('bold_black', '\033[1m\033[30m'),
    ('italic_blue', '\033[3m\033[34m'),
    ('struckthrough_white', '\033[9m\033[37m'),
    # modifiers with background colors
    ('bold_on_black', '\033[1m\033[40m'),
    ('italic_on_blue', '\033[3m\033[44m'),
    ('struckthrough_on_white', '\033[9m\033[47m'),
    # modifiers with foreground and background colors
    ('bold_green_on_black', '\033[1m\033[32m\033[40m'),
    ('italic_cyan_on_blue', '\033[3m\033[36m\033[44m'),
    ('struckthrough_yellow_on_white', '\033[9m\033[33m\033[47m'),
    # multiple modifiers
    ('bold_italic', '\033[1m\033[3m'),
    ('underlined_struckthrough', '\033[4m\033[9m'),
    # multiple modifiers with foreground colors
    ('bold_italic_green', '\033[1m\033[3m\033[32m'),
    ('underlined_struckthrough_cyan', '\033[4m\033[9m\033[36m')
])
def test_method_str_to_style_conversion(method_name, expected):
    """
    Test converting the method to an actual style
    """
    colorful = core.Colorful(colormode=terminal.ANSI_8_COLORS)
    method = getattr(colorful, method_name)

    assert str(method) == expected


@pytest.mark.parametrize('format_str, expected', [
    (
        '{c.bold}No, I am your father{c.reset}',
        '\033[1mNo, I am your father\033[0m'
    ), (
        '{c.struckthrough}No, I am your father{c.reset}',
        '\033[9mNo, I am your father\033[0m'
    ),
    # foreground colors
    (
        '{c.black}No, I am your father{c.reset}',
        '\033[30mNo, I am your father\033[0m'
    ), (
        '{c.blue}No, I am your father{c.reset}',
        '\033[34mNo, I am your father\033[0m'
    ), (
        '{c.white}No, I am your father{c.reset}',
        '\033[37mNo, I am your father\033[0m'
    ),
    # background colors
    (
        '{c.on_black}No, I am your father{c.reset}',
        '\033[40mNo, I am your father\033[0m'
    ), (
        '{c.on_blue}No, I am your father{c.reset}',
        '\033[44mNo, I am your father\033[0m'
    ), (
        '{c.on_white}No, I am your father{c.reset}',
        '\033[47mNo, I am your father\033[0m'
    ),
    # modifiers with foreground colors
    (
        '{c.bold_black}No, I am your father{c.reset}',
        '\033[1m\033[30mNo, I am your father\033[0m'
    ), (
        '{c.italic_blue}No, I am your father{c.reset}',
        '\033[3m\033[34mNo, I am your father\033[0m'
    ), (
        '{c.struckthrough_white}No, I am your father{c.reset}',
        '\033[9m\033[37mNo, I am your father\033[0m'
    ),
    # modifiers with background colors
    (
        '{c.bold_on_black}No, I am your father{c.reset}',
        '\033[1m\033[40mNo, I am your father\033[0m'
    ), (
        '{c.italic_on_blue}No, I am your father{c.reset}',
        '\033[3m\033[44mNo, I am your father\033[0m'
    ), (
        '{c.struckthrough_on_white}No, I am your father{c.reset}',
        '\033[9m\033[47mNo, I am your father\033[0m'
    ),
    # modifiers with foreground and background colors
    (
        '{c.bold_green_on_black}No, I am your father{c.reset}',
        '\033[1m\033[32m\033[40mNo, I am your father\033[0m'
    ), (
        '{c.italic_cyan_on_blue}No, I am your father{c.reset}',
        '\033[3m\033[36m\033[44mNo, I am your father\033[0m'
    ), (
        '{c.struckthrough_yellow_on_white}No, I am your father{c.reset}',
        '\033[9m\033[33m\033[47mNo, I am your father\033[0m'
    ),
    # multiple modifiers
    (
        '{c.bold_italic}No, I am your father{c.reset}',
        '\033[1m\033[3mNo, I am your father\033[0m'
    ), (
        '{c.underlined_struckthrough}No, I am your father{c.reset}',
        '\033[4m\033[9mNo, I am your father\033[0m'
    ),
    # multiple modifiers with foreground colors
    (
        '{c.bold_italic_green}No, I am your father{c.reset}',
        '\033[1m\033[3m\033[32mNo, I am your father\033[0m'
    ), (
        '{c.underlined_struckthrough_cyan}No, I am your father{c.reset}',
        '\033[4m\033[9m\033[36mNo, I am your father\033[0m'
    ),
    # color closing delimiters
    (
        '{c.black}No, I am your father{c.close_fg_color}',
        '\033[30mNo, I am your father\033[39m'
    ), (
        '{c.on_black}No, I am your father{c.close_bg_color}',
        '\033[40mNo, I am your father\033[49m'
    ),
    # modifier closing delimiters
    (
        '{c.bold}No, I am your father{c.no_bold}',
        '\033[1mNo, I am your father\033[22m'
    ), (
        '{c.struckthrough}No, I am your father{c.no_strikethrough}',
        '\033[9mNo, I am your father\033[29m'
    )
])
def test_method_in_format_to_style_conversion(format_str, expected):
    """
    Test converting the method in a format() call to an actual style
    """
    colorful = core.Colorful(colormode=terminal.ANSI_8_COLORS)

    assert format_str.format(c=colorful) == expected


def test_invalid_color_mode():
    """
    Test setting an invalid color mode
    """
    colorful = core.Colorful(colormode=42)

    with pytest.raises(core.ColorfulError) as exc:
        colorful.white('Invalid color mode')
    assert str(exc.value) == 'invalid color mode "42"'


def test_invalid_color_name():
    """
    Test invalid color name
    """
    colorful = core.Colorful(colormode=terminal.ANSI_8_COLORS)

    expected = ('the color "invalidColor" is unknown. '
                'Use a color in your color palette (by default: X11 rgb.txt)')
    with pytest.raises(core.ColorfulError) as exc:
        colorful.bold_invalidColor('Invalid color name')
    assert str(exc.value) == expected


@pytest.mark.parametrize('env,expected', [
    ({'COLORFUL_DISABLE': '1'}, terminal.NO_COLORS),
    ({'COLORTERM': 'truecolor'}, terminal.TRUE_COLORS),
    ({'TERM_PROGRAM': 'iTerm.app'}, terminal.TRUE_COLORS),
    ({'TERM': 'xterm-256color'}, terminal.ANSI_256_COLORS),
    ({'TERM': 'screen'}, terminal.ANSI_16_COLORS),
    ({}, terminal.ANSI_8_COLORS),
])
def test_colorful_obj_color_auto_detection(env, expected):
    """
    Test that the colorful object is able to auto detect the supported colors
    """
    os_env_backup = os.environ.copy()
    os.environ = env
    colorful = core.Colorful(colormode=None)  # None to explicitly auto detect the colors
    assert colorful.colormode == expected

    # restore environ backup
    os.environ = os_env_backup


def test_reading_color_palette(tmpdir):
    """
    Test reading color palette from file
    """
    # create palette file
    palette_file = tmpdir.mkdir('palettes').join('my_rgb.txt')
    palette_file.write("""
0 0 0 myBlack
255 255 255      myWhite""")

    colorful = core.Colorful(colorpalette=str(palette_file))
    assert str(colorful.myBlack) == '\033[30m'
    assert str(colorful.myWhite) == '\033[37m'


def test_colorful_obj_setup():
    """
    Test setup of an existing colorful object
    """
    colorful = core.Colorful(colormode=terminal.ANSI_8_COLORS)
    colorful.setup(
        colormode=terminal.TRUE_COLORS,
        colorpalette={'testColor': (0, 0, 0)},
        extend_colors=False
    )

    assert colorful.colormode == terminal.TRUE_COLORS
    assert str(colorful.testColor) == '\033[38;2;0;0;0m'

    with pytest.raises(core.ColorfulError) as exc:
        colorful.black('black does not exist anymore')

    expected = ('the color "black" is unknown. '
                'Use a color in your color palette (by default: X11 rgb.txt)')
    assert str(exc.value) == expected


def test_colorful_obj_setup_with_extending_palette():
    """
    Test setup of an existing colorful object and extend the color palette
    """
    colorful = core.Colorful(colormode=terminal.ANSI_8_COLORS)
    colorful.setup(
        colormode=terminal.TRUE_COLORS,
        colorpalette={'testColor': (0, 0, 0)},
        extend_colors=True
    )

    assert colorful.colormode == terminal.TRUE_COLORS
    assert str(colorful.testColor) == '\033[38;2;0;0;0m'
    assert str(colorful.black) == '\033[38;2;0;0;0m'


@pytest.mark.parametrize('method_name, colorname, expected', [
    ('use_8_ansi_colors', 'black', '\033[30m'),
    ('use_16_ansi_colors', 'black', '\033[30m'),
    ('use_256_ansi_colors', 'black', '\033[38;5;16m'),
    ('use_true_colors', 'black', '\033[38;2;0;0;0m')
])
def test_set_color_mode_methods(method_name, colorname, expected):
    """
    Test changing the color mode for an existing colorful object
    """
    colorful = core.Colorful(colormode=terminal.NO_COLORS)

    # change color mode
    getattr(colorful, method_name)()

    assert str(getattr(colorful, colorname)) == expected


def test_change_color_palette():
    """
    Test changing the color palette for an existing colorful object
    """
    NEW_COLOR_PALETTE = {
        'black': (0, 0, 0)
    }
    colorful = core.Colorful(
        colormode=terminal.ANSI_8_COLORS, colorpalette={'defaultColor': (255, 255, 255)})

    # updating existing color palette
    colorful.update_palette(NEW_COLOR_PALETTE)
    # old and new colors should exist
    assert str(colorful.black) == '\033[30m'
    assert str(colorful.defaultColor) == '\033[37m'

    # set color palette and overwrite the old one
    colorful.use_palette(NEW_COLOR_PALETTE)
    assert str(colorful.black) == '\033[30m'

    with pytest.raises(core.ColorfulError) as exc:
        colorful.defaultColor('The defaultColor was overwritten by the new palette')

    expected = ('the color "defaultColor" is unknown. '
                'Use a color in your color palette (by default: X11 rgb.txt)')
    assert str(exc.value) == expected


def test_use_styles():
    """
    Test using a predefined style
    """
    colorful = core.Colorful(colormode=terminal.TRUE_COLORS)
    colorful.use_style('solarized')

    assert str(colorful.red) == '\033[38;2;220;50;47m'

    with pytest.raises(core.ColorfulError) as exc:
        colorful.lightCoral('The color lightCoral only exists in the X11 rgb.txt palette')

    assert str(exc.value).startswith('the color "lightCoral" is unknown.')


def test_use_unknown_style():
    """
    Test exception for unknown style
    """
    colorful = core.Colorful(colormode=terminal.ANSI_8_COLORS)

    with pytest.raises(core.ColorfulError) as exc:
        colorful.use_style('unknown')

    assert str(exc.value) == 'the style "unknown" is undefined'


def test_colorful_format():
    """
    Test the colorful.format method
    """
    colorful = core.Colorful(colormode=terminal.ANSI_8_COLORS)

    expected = '\033[3m\033[31mNo, I am your father\033[23m\033[39m'
    assert colorful.format('{c.italic_red}{0}, I am your {who}{c.no_italic}{c.close_fg_color}',
                           'No', who='father') == expected


def test_colorful_direct_print(capsys):
    """
    Test the colorful.print method
    """
    colorful = core.Colorful(colormode=terminal.ANSI_8_COLORS)

    expected = u'\033[3m\033[31mNo, I am your father\033[23m\033[39m\n'

    colorful.print('{c.italic_red}No, I am your father{c.no_italic}{c.close_fg_color}', flush=True)

    out, err = capsys.readouterr()
    assert repr(out) == repr(expected)
    assert err == ''


def test_colorful_print_wrong_argument():
    """
    Test calling the colorful.print method with wrong arguments
    """
    colorful = core.Colorful(colormode=terminal.ANSI_8_COLORS)

    with pytest.raises(TypeError) as exc:
        colorful.print('Never printed because of argument error', foo=42)

    assert str(exc.value) == 'Colorful.print() got unexpected keyword arguments: foo'


@pytest.mark.parametrize('method_name, expected', [
    ('bold', 'No, I am your father'),
    ('struckthrough', 'No, I am your father'),
    # foreground colors
    ('black', 'No, I am your father'),
    ('blue', 'No, I am your father'),
    ('white', 'No, I am your father'),
    # background colors
    ('on_black', 'No, I am your father'),
    ('on_blue', 'No, I am your father'),
    ('on_white', 'No, I am your father'),
    # modifiers with foreground colors
    ('bold_black', 'No, I am your father'),
    ('italic_blue', 'No, I am your father'),
    ('struckthrough_white', 'No, I am your father'),
    # modifiers with background colors
    ('bold_on_black', 'No, I am your father'),
    ('italic_on_blue', 'No, I am your father'),
    ('struckthrough_on_white', 'No, I am your father'),
    # modifiers with foreground and background colors
    ('bold_green_on_black', 'No, I am your father'),
    ('italic_cyan_on_blue', 'No, I am your father'),
    ('struckthrough_yellow_on_white', 'No, I am your father'),
    # multiple modifiers
    ('bold_italic', 'No, I am your father'),
    ('underlined_struckthrough', 'No, I am your father'),
    # multiple modifiers with foreground colors
    ('bold_italic_green', 'No, I am your father'),
    ('underlined_struckthrough_cyan', 'No, I am your father')
])
def test_length_of_styled_string(method_name, expected):
    """
    Test the length of a styled string
    """
    colorful = core.Colorful(colormode=terminal.ANSI_8_COLORS)
    method = getattr(colorful, method_name)

    assert len(method(expected)) == len(expected)


def test_nested_styled_string():
    """
    Test nested styled string
    """
    colorful = core.Colorful(colormode=terminal.ANSI_8_COLORS)

    s = colorful.red('Hello ' + colorful.blue('awesome', nested=True) + ' world')
    assert str(s) == '\033[31mHello \033[34mawesome\033[39m\033[31m world\033[39m'

    s = colorful.red('Hello') + ' World'
    assert str(s) == '\033[31mHello\033[39m World'

    s = 'Hello' + colorful.red(' World')
    assert str(s) == 'Hello\033[31m World\033[39m'

    s = colorful.red('Hello') + colorful.blue(' World')
    assert str(s) == '\033[31mHello\033[39m\033[34m World\033[39m'

    s = colorful.red('Hello {0} world'.format(colorful.blue('awesome', nested=True)))
    assert str(s) == '\033[31mHello \033[34mawesome\033[39m\033[31m world\033[39m'


def test_nested_styled_string_with_format():
    """
    Test nested styled string with format()
    """
    colorful = core.Colorful(colormode=terminal.ANSI_8_COLORS)

    s = colorful.red('Hello {0} world'.format(colorful.blue('awesome')))
    assert str(s) == '\033[31mHello \033[34mawesome\033[39m\033[31m world\033[39m'


def test_styling_object_which_implements_str_proto():
    """
    Test styling an object which implements the str protocol
    """
    class Dummy(object):
        def __str__(self):
            return 'I am a dummy object'

    colorful = core.Colorful(colormode=terminal.ANSI_8_COLORS)
    assert str(colorful.black(Dummy())) == '\033[30mI am a dummy object\033[39m'


def test_str_behavior_for_colorfulstring():
    """
    Test that the ColorfulString object behaves like a str
    """
    colorful = core.Colorful(colormode=terminal.ANSI_8_COLORS)
    s = colorful.black('Hello')

    # test adding to str
    assert str(s + ' World') == '\033[30mHello\033[39m World'

    # test being added to str
    assert 'World ' + s == 'World \033[30mHello\033[39m'

    # test being augment added to str
    string = 'World '
    string += s
    assert string == 'World \033[30mHello\033[39m'

    # test augment add a str
    s2 = colorful.red('Hello ')
    s2 += 'World'
    assert str(s2) == '\033[31mHello \033[39mWorld'

    # test ColorfulString to ColorfulString
    assert str(s + s) == '\033[30mHello\033[39m\033[30mHello\033[39m'

    # test ColorfulString augmented added to other ColorfulString
    s2 = colorful.red('World ')
    s2 += s
    assert str(s2) == '\033[31mWorld \033[39m\033[30mHello\033[39m'

    # test multipling ColorfulString
    assert str(s * 3) == '\033[30mHello\033[39m\033[30mHello\033[39m\033[30mHello\033[39m'

    # other str methods operate on the styled string
    assert s.replace('Hello', 'Adieu') == '\033[30mAdieu\033[39m'


def test_joining_colorfulstrings():
    """
    Test joining ColorfulStrings
    """
    colorful = core.Colorful(colormode=terminal.ANSI_8_COLORS)

    parts = [colorful.red('Hello'), colorful.black('World')]

    # FIXME(TF): is there any other way??
    string = ' '.join(str(part) for part in parts)
    assert string == '\033[31mHello\033[39m \033[30mWorld\033[39m'


def test_creating_unstyled_colorfulstring():
    """
    Test creating an unstyled ColorfulString
    """
    colorful = core.Colorful(colormode=terminal.ANSI_8_COLORS)
    s = colorful.str('Hello ')
    s += colorful.black('World')

    assert s.orig_string == 'Hello World'
    assert s.styled_string == str(s) == 'Hello \033[30mWorld\033[39m'


def test_unicode_support():
    """
    Test unicode support
    """
    colorful = core.Colorful(colormode=terminal.ANSI_8_COLORS)

    s = u'🐧🎉🐧'
    styled_s = colorful.black(s)

    if core.PY2:
        unicode_type = unicode  # noqa
    else:
        unicode_type = str

    # test basic unicode support
    assert unicode_type(styled_s) == u'\033[30m🐧🎉🐧\033[39m'


def test_combining_styles():
    """
    Test combining styles
    """
    colorful = core.Colorful(colormode=terminal.ANSI_8_COLORS)

    style = colorful.bold & colorful.red & colorful.on_black

    assert str(style) == '\033[1m\033[31m\033[40m'


def test_piping_str_into_style():
    """
    Test piping a string into a style
    """
    colorful = core.Colorful(colormode=terminal.ANSI_8_COLORS)

    string = colorful.bold_red | 'No, I am your father'

    assert str(string) == '\033[1m\033[31mNo, I am your father\033[22m\033[39m'


def test_piping_styled_str_into_style():
    """
    Test piping a string into a style
    """
    colorful = core.Colorful(colormode=terminal.ANSI_8_COLORS)

    string = colorful.bold_red | colorful.on_black('No, I am your father')

    assert str(string) == '\033[1m\033[31m\033[40mNo, I am your father\033[49m\033[22m\033[39m'


def test_piping_constitency():
    """
    Test piping a string into a style does the same as the method call
    """
    colorful = core.Colorful(colormode=terminal.ANSI_8_COLORS)

    string_piped = colorful.bold & colorful.red | 'No, I am your father'
    string_called = (colorful.bold & colorful.red)('No, I am your father')
    string_called_single = colorful.bold_red('No, I am your father')

    assert str(string_piped) == str(string_called) == str(string_called_single)


def test_colorfulstring_format_protocol():
    """
    Test format protocol for colorful string
    """
    colorful = core.Colorful(colormode=terminal.ANSI_8_COLORS)
    s = colorful.black('father')

    string = 'No, I am your {0}'.format(s)
    assert string == 'No, I am your \033[30mfather\033[39m\033[26m'

    string = colorful.red('No, I am your {0}')
    formatted = string.format(s)
    assert str(formatted) == '\033[31mNo, I am your \033[30mfather\033[39m\033[26m\033[39m'
