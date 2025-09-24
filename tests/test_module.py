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

import colorful  # noqa
import colorful.terminal as terminal  # noqa

# replace colorful name with ColorfulModule instance
ColorfulError = colorful.core.ColorfulError
colorful = colorful.ColorfulModule(
    colorful.Colorful(colormode=terminal.ANSI_8_COLORS), 'colorful')


def test_color_method_resolution():
    """
    Test the color method resolution on the package level
    """
    #
    assert str(colorful.black) == '\033[30m'


def test_setup_contextmanager():
    """
    Test the package level setup context manager
    """
    with colorful.with_setup(colormode=terminal.ANSI_16_COLORS,
                             colorpalette={'testColor': (0, 0, 0)}, extend_colors=False) as c:
        assert str(c.testColor) == '\033[30m'

        with pytest.raises(ColorfulError) as exc:
            c.black('Black does not exist anymore')
        assert str(exc.value).startswith('the color "black" is unknown.')

    with pytest.raises(ColorfulError) as exc:
        colorful.testColor('The testColor only existed in the with block above.')
    assert str(exc.value).startswith('the color "testColor" is unknown.')


@pytest.mark.parametrize('ctxmgr_name, colorname, expected, expected_8', [
    ('with_8_ansi_colors', 'black', '\033[30m', '\033[30m'),
    ('with_16_ansi_colors', 'black', '\033[30m', '\033[30m'),
    ('with_256_ansi_colors', 'black', '\033[38;5;16m', '\033[30m'),
    ('with_true_colors', 'black', '\033[38;2;0;0;0m', '\033[30m')
])
def test_set_color_mode_methods(ctxmgr_name, colorname, expected, expected_8):
    """
    Test changing the color mode in a with-block
    """
    contextmanager = getattr(colorful, ctxmgr_name)

    with contextmanager() as c:
        assert str(getattr(c, colorname)) == expected

    assert str(getattr(colorful, colorname)) == expected_8


def test_change_color_palette():
    """
    Test changing the color palette in a with-block
    """
    NEW_COLOR_PALETTE = {
        'testColor': (0, 0, 0)
    }

    # updating existing color palette
    with colorful.with_updated_palette(NEW_COLOR_PALETTE) as c:
        # old and new colors should exist
        assert str(c.testColor) == '\033[30m'
        assert str(c.black) == '\033[30m'

    # set color palette and overwrite the old one
    with colorful.with_palette(NEW_COLOR_PALETTE) as c:
        assert str(c.testColor) == '\033[30m'

        with pytest.raises(ColorfulError) as exc:
            c.black('the color "black" was overwritten by the new palette')

        expected = ('the color "black" is unknown. '
                    'Use a color in your color palette (by default: X11 rgb.txt)')
        assert str(exc.value) == expected


def test_use_styles():
    """
    Test using a predefined style in a with-block
    """
    with colorful.with_style('solarized') as c:
        c.use_true_colors()
        assert str(c.red) == '\033[38;2;220;50;47m'

    assert str(colorful.red) == '\033[31m'
