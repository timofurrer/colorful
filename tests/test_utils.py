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

import colorful.utils as utils  # noqa


@pytest.mark.parametrize('hex_value', [
    '#FFFFFF',
    '#0000FF',
    '#FF0000',
    '#00FF00',
    '#808080',
    '#FFFF00',
    '#00FFFF',
    '#EF8BA0',
    '#012345',
    '#999FFF',
    '#05fecA'
])
def test_hex_to_rgb_conversion(hex_value):
    """
    Test the conversion from a RGB hex value to a RGB channel triplet
    """
    red, green, blue = utils.hex_to_rgb(hex_value)
    assert '#{:02X}{:02X}{:02X}'.format(red, green, blue).lower() == hex_value.lower()


@pytest.mark.parametrize('hex_error_value', [
    '#FFFFF',
    '#FFFFFFF',
    '#FFFFFG',
    '#fffffG',
])
def test_hex_to_rgb_error(hex_error_value):
    """
    Test if the given hex values are invalid
    """
    with pytest.raises(ValueError):
        utils.hex_to_rgb(hex_error_value)
