# -*- coding: utf-8 -*-

"""
    colorful
    ~~~~~~~~

    Terminal string styling done right, in Python.

    :copyright: (c) 2017 by Timo Furrer <tuxtimo@gmail.com>
    :license: MIT, see LICENSE for more details.
"""


def hex_to_rgb(value):
    """
    Convert the given hex string to a
    valid RGB channel triplet.
    """
    value = value.lstrip('#')

    length = len(value)
    return tuple(int(value[i:i + int(length / 3)], 16) for i in range(0, length, int(length / 3)))
