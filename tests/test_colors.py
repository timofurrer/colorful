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

import colorful.colors as colors  # noqa


@pytest.mark.parametrize('colorpalette, expected', [
    ({'black': '#000000'}, {'black': (0, 0, 0)}),
    ({'red': '#FF0000'}, {'red': (255, 0, 0)}),
    ({'purple': '#800080'}, {'purple': (128, 0, 128)}),
    ({
        'maroon': '#800000',
        'magenta': '#FF00FF',
        'cyan': '#00FFFF'
    }, {
        'maroon': (128, 0, 0),
        'magenta': (255, 0, 255),
        'cyan': (0, 255, 255)
    })
])
def test_sanitize_color_palette(colorpalette, expected):
    """
    Test sanitizing a color palette
    """
    assert colors.sanitize_color_palette(colorpalette) == expected
