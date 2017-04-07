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
    ('bold', r'\033[1m'),
    ('strikethroughed', r'\033[9m'),
    # foreground colors
    ('black', r'\033[30m'),
    ('blue', r'\033[34m'),
    ('white', r'\033[37m'),
    # background colors
    ('on_black', r'\033[40m'),
    ('on_blue', r'\033[44m'),
    ('on_white', r'\033[47m'),
    # modifiers with foreground colors
    ('bold_black', r'\033[1m\033[30m'),
    ('italic_blue', r'\033[3m\033[34m'),
    ('strikethroughed_white', r'\033[9m\033[37m'),
    # modifiers with background colors
    ('bold_on_black', r'\033[1m\033[40m'),
    ('italic_on_blue', r'\033[3m\033[44m'),
    ('strikethroughed_on_white', r'\033[9m\033[47m'),
    # modifiers with foreground and background colors
    ('bold_green_on_black', r'\033[1m\033[32m\033[40m'),
    ('italic_cyan_on_blue', r'\033[3m\033[36m\033[44m'),
    ('strikethroughed_yellow_on_white', r'\033[9m\033[33m\033[47m'),
    # multiple modifiers
    ('bold_italic', r'\033[1m\033[3m'),
    ('underlined_strikethroughed', r'\033[4m\033[9m'),
    # multiple modifiers with foreground colors
    ('bold_italic_green', r'\033[1m\033[3m\033[32m'),
    ('underlined_strikethroughed_cyan', r'\033[4m\033[9m\033[36m')
])
def test_translate_style(style_string, expected):
    """
    Test translating style strings
    """
    assert core.translate_style(style_string) == expected
