# -*- coding: utf-8 -*-

"""
    colorful
    ~~~~~~~~

    Terminal string styling done right, in Python.

    :copyright: (c) 2017 by Timo Furrer <tuxtimo@gmail.com>
    :license: MIT, see LICENSE for more details.
"""

import math


def round(value):
    x = math.floor(value)
    if (value - x) < 0.5:
        return int(x)
    return int(math.ceil(value))


def rgb_to_ansi265(r, g, b):
    """
    Convert RGB to ANSI 256 color
    """
    if r == g and g == b:
        if r < 8:
            return 16
        if r > 248:
            return 231

        return round(((r - 8) / 247) * 24) + 232

    ansi_r = 36 * round(r / 255.0 * 5.0)
    ansi_g = 6 * round(g / 255.0 * 5.0)
    ansi_b = round(b / 255.0 * 5.0)
    ansi = 16 + ansi_r + ansi_g + ansi_b
    return ansi


def rgb_to_ansi16(r, g, b, use_bright=False):
    """
    Convert RGB to ANSI 16bit color
    """
    ansi_b = round(b / 255.0) << 2
    ansi_g = round(g / 255.0) << 1
    ansi_r = round(r / 255.0)
    ansi = (90 if use_bright else 30) + (ansi_b | ansi_g | ansi_r)

    return ansi
