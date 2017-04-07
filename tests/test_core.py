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
def test_translate_style(style_string, expected):
    """
    Test translating style strings
    """
    assert core.translate_style(style_string) == expected


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
def test_method_to_style_conversion(method_name, expected):
    """
    Test converting the method to an actual style
    """
    colorful = core.Colorful()
    method = getattr(colorful, method_name)

    assert method('No, I am your father') == expected
