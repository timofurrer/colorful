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

import colorful.ansi as ansi  # noqa


@pytest.mark.parametrize('r, g, b, result', [
    (118, 118, 118, 243),
])
def test_rgb_to_ansi256(r, g, b, result):
    """
    Test converting an RGB value to an ANSI 256 color.
    """

    assert result == ansi.rgb_to_ansi256(r, g, b)
