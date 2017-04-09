# -*- coding: utf-8 -*-

"""
    colorful
    ~~~~~~~~

    Terminal string styling done right, in Python.

    :copyright: (c) 2017 by Timo Furrer <tuxtimo@gmail.com>
    :license: MIT, see LICENSE for more details.
"""

import os

import pytest

# do not overwrite module
os.environ['COLORFUL_NO_MODULE_OVERWRITE'] = '1'

import colorful.core as core  # noqa


@pytest.mark.parametrize('style_string,expected', [
    # modifiers
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
def test_translate_style_8bit(style_string, expected):
    """
    Test translating style strings with 8bit colors
    """
    assert core.translate_style(style_string, colormode=8,
                                colorpalette=core.COLOR_PALETTE) == expected


@pytest.mark.parametrize('style_string,expected', [
    # modifiers
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
def test_translate_style_16bit(style_string, expected):
    """
    Test translating style strings with 16bit colors
    """
    assert core.translate_style(style_string, colormode=16,
                                colorpalette=core.COLOR_PALETTE) == expected


@pytest.mark.parametrize('style_string,expected', [
    # modifiers
    ('bold', '\033[1m'),
    ('struckthrough', '\033[9m'),
    # foreground colors
    ('black', '\033[38;5;16m'),
    ('blue', '\033[38;5;21m'),
    ('white', '\033[38;5;231m'),
    # background colors
    ('on_black', '\033[48;5;16m'),
    ('on_blue', '\033[48;5;21m'),
    ('on_white', '\033[48;5;231m'),
    # modifiers with foreground colors
    ('bold_black', '\033[1m\033[38;5;16m'),
    ('italic_blue', '\033[3m\033[38;5;21m'),
    ('struckthrough_white', '\033[9m\033[38;5;231m'),
    # modifiers with background colors
    ('bold_on_black', '\033[1m\033[48;5;16m'),
    ('italic_on_blue', '\033[3m\033[48;5;21m'),
    ('struckthrough_on_white', '\033[9m\033[48;5;231m'),
    # modifiers with foreground and background colors
    ('bold_green_on_black', '\033[1m\033[38;5;46m\033[48;5;16m'),
    ('italic_cyan_on_blue', '\033[3m\033[38;5;51m\033[48;5;21m'),
    ('struckthrough_yellow_on_white', '\033[9m\033[38;5;226m\033[48;5;231m'),
    # multiple modifiers
    ('bold_italic', '\033[1m\033[3m'),
    ('underlined_struckthrough', '\033[4m\033[9m'),
    # multiple modifiers with foreground colors
    ('bold_italic_green', '\033[1m\033[3m\033[38;5;46m'),
    ('underlined_struckthrough_cyan', '\033[4m\033[9m\033[38;5;51m')
])
def test_translate_style_256(style_string, expected):
    """
    Test translating style strings with 256 colors
    """
    assert core.translate_style(style_string, colormode=256,
                                colorpalette=core.COLOR_PALETTE) == expected


@pytest.mark.parametrize('style_string,expected', [
    # modifiers
    ('bold', '\033[1m'),
    ('struckthrough', '\033[9m'),
    # foreground colors
    ('black', '\033[38;2;0;0;0m'),
    ('blue', '\033[38;2;0;0;255m'),
    ('white', '\033[38;2;255;255;255m'),
    # background colors
    ('on_black', '\033[48;2;0;0;0m'),
    ('on_blue', '\033[48;2;0;0;255m'),
    ('on_white', '\033[48;2;255;255;255m'),
    # modifiers with foreground colors
    ('bold_black', '\033[1m\033[38;2;0;0;0m'),
    ('italic_blue', '\033[3m\033[38;2;0;0;255m'),
    ('struckthrough_white', '\033[9m\033[38;2;255;255;255m'),
    # modifiers with background colors
    ('bold_on_black', '\033[1m\033[48;2;0;0;0m'),
    ('italic_on_blue', '\033[3m\033[48;2;0;0;255m'),
    ('struckthrough_on_white', '\033[9m\033[48;2;255;255;255m'),
    # modifiers with foreground and background colors
    ('bold_green_on_black', '\033[1m\033[38;2;0;255;0m\033[48;2;0;0;0m'),
    ('italic_cyan_on_blue', '\033[3m\033[38;2;0;255;255m\033[48;2;0;0;255m'),
    ('struckthrough_yellow_on_white', '\033[9m\033[38;2;255;255;0m\033[48;2;255;255;255m'),
    # multiple modifiers
    ('bold_italic', '\033[1m\033[3m'),
    ('underlined_struckthrough', '\033[4m\033[9m'),
    # multiple modifiers with foreground colors
    ('bold_italic_green', '\033[1m\033[3m\033[38;2;0;255;0m'),
    ('underlined_struckthrough_cyan', '\033[4m\033[9m\033[38;2;0;255;255m')
])
def test_translate_style_true_colors(style_string, expected):
    """
    Test translating style strings with true colors
    """
    assert core.translate_style(style_string, colormode=0xFFFFFF,
                                colorpalette=core.COLOR_PALETTE) == expected


@pytest.mark.parametrize('method_name,expected', [
    ('bold', '\033[1mNo, I am your father\033[0m'),
    ('struckthrough', '\033[9mNo, I am your father\033[0m'),
    # foreground colors
    ('black', '\033[30mNo, I am your father\033[0m'),
    ('blue', '\033[34mNo, I am your father\033[0m'),
    ('white', '\033[37mNo, I am your father\033[0m'),
    # background colors
    ('on_black', '\033[40mNo, I am your father\033[0m'),
    ('on_blue', '\033[44mNo, I am your father\033[0m'),
    ('on_white', '\033[47mNo, I am your father\033[0m'),
    # modifiers with foreground colors
    ('bold_black', '\033[1m\033[30mNo, I am your father\033[0m'),
    ('italic_blue', '\033[3m\033[34mNo, I am your father\033[0m'),
    ('struckthrough_white', '\033[9m\033[37mNo, I am your father\033[0m'),
    # modifiers with background colors
    ('bold_on_black', '\033[1m\033[40mNo, I am your father\033[0m'),
    ('italic_on_blue', '\033[3m\033[44mNo, I am your father\033[0m'),
    ('struckthrough_on_white', '\033[9m\033[47mNo, I am your father\033[0m'),
    # modifiers with foreground and background colors
    ('bold_green_on_black', '\033[1m\033[32m\033[40mNo, I am your father\033[0m'),
    ('italic_cyan_on_blue', '\033[3m\033[36m\033[44mNo, I am your father\033[0m'),
    ('struckthrough_yellow_on_white', '\033[9m\033[33m\033[47mNo, I am your father\033[0m'),
    # multiple modifiers
    ('bold_italic', '\033[1m\033[3mNo, I am your father\033[0m'),
    ('underlined_struckthrough', '\033[4m\033[9mNo, I am your father\033[0m'),
    # multiple modifiers with foreground colors
    ('bold_italic_green', '\033[1m\033[3m\033[32mNo, I am your father\033[0m'),
    ('underlined_struckthrough_cyan', '\033[4m\033[9m\033[36mNo, I am your father\033[0m')
])
def test_method_call_to_style_conversion(method_name, expected):
    """
    Test converting the method call to an actual style
    """
    colorful = core.Colorful(colormode=8)
    method = getattr(colorful, method_name)

    assert method('No, I am your father') == expected


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
    colorful = core.Colorful(colormode=0)
    method = getattr(colorful, method_name)

    assert method('No, I am your father') == 'No, I am your father'


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
    colorful = core.Colorful(colormode=8)
    method = getattr(colorful, method_name)

    assert str(method) == expected


@pytest.mark.parametrize('method_name,expected', [
    ('bold', '\033[1mNo, I am your father\033[0m'),
    ('struckthrough', '\033[9mNo, I am your father\033[0m'),
    # foreground colors
    ('black', '\033[30mNo, I am your father\033[0m'),
    ('blue', '\033[34mNo, I am your father\033[0m'),
    ('white', '\033[37mNo, I am your father\033[0m'),
    # background colors
    ('on_black', '\033[40mNo, I am your father\033[0m'),
    ('on_blue', '\033[44mNo, I am your father\033[0m'),
    ('on_white', '\033[47mNo, I am your father\033[0m'),
    # modifiers with foreground colors
    ('bold_black', '\033[1m\033[30mNo, I am your father\033[0m'),
    ('italic_blue', '\033[3m\033[34mNo, I am your father\033[0m'),
    ('struckthrough_white', '\033[9m\033[37mNo, I am your father\033[0m'),
    # modifiers with background colors
    ('bold_on_black', '\033[1m\033[40mNo, I am your father\033[0m'),
    ('italic_on_blue', '\033[3m\033[44mNo, I am your father\033[0m'),
    ('struckthrough_on_white', '\033[9m\033[47mNo, I am your father\033[0m'),
    # modifiers with foreground and background colors
    ('bold_green_on_black', '\033[1m\033[32m\033[40mNo, I am your father\033[0m'),
    ('italic_cyan_on_blue', '\033[3m\033[36m\033[44mNo, I am your father\033[0m'),
    ('struckthrough_yellow_on_white', '\033[9m\033[33m\033[47mNo, I am your father\033[0m'),
    # multiple modifiers
    ('bold_italic', '\033[1m\033[3mNo, I am your father\033[0m'),
    ('underlined_struckthrough', '\033[4m\033[9mNo, I am your father\033[0m'),
    # multiple modifiers with foreground colors
    ('bold_italic_green', '\033[1m\033[3m\033[32mNo, I am your father\033[0m'),
    ('underlined_struckthrough_cyan', '\033[4m\033[9m\033[36mNo, I am your father\033[0m')
])
def test_method_in_format_to_style_conversion(method_name, expected):
    """
    Test converting the method in a format() call to an actual style
    """
    colorful = core.Colorful(colormode=8)
    method = getattr(colorful, method_name)

    assert '{method}No, I am your father{c.reset}'.format(method=method, c=colorful) == expected


# @pytest.mark.parametrize('method_name,expected', [
    # ('bold', 'No, I am your father'),
    # ('struckthrough', 'No, I am your father'),
    # # foreground colors
    # ('black', 'No, I am your father'),
    # ('blue', 'No, I am your father'),
    # ('white', 'No, I am your father'),
    # # background colors
    # ('on_black', 'No, I am your father'),
    # ('on_blue', 'No, I am your father'),
    # ('on_white', 'No, I am your father'),
    # # modifiers with foreground colors
    # ('bold_black', 'No, I am your father'),
    # ('italic_blue', 'No, I am your father'),
    # ('struckthrough_white', 'No, I am your father'),
    # # modifiers with background colors
    # ('bold_on_black', 'No, I am your father'),
    # ('italic_on_blue', 'No, I am your father'),
    # ('struckthrough_on_white', 'No, I am your father'),
    # # modifiers with foreground and background colors
    # ('bold_green_on_black', 'No, I am your father'),
    # ('italic_cyan_on_blue', 'No, I am your father'),
    # ('struckthrough_yellow_on_white', 'No, I am your father'),
    # # multiple modifiers
    # ('bold_italic', 'No, I am your father'),
    # ('underlined_struckthrough', 'No, I am your father'),
    # # multiple modifiers with foreground colors
    # ('bold_italic_green', 'No, I am your father'),
    # ('underlined_struckthrough_cyan', 'No, I am your father')
# ])
# def test_length_of_styled_string(method_name, expected):
    # """
    # Test the length of a styled string
    # """
    # colorful = core.Colorful(colormode=8)
    # method = getattr(colorful, method_name)

    # assert len(method(expected)) == len(expected)
