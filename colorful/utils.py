# -*- coding: utf-8 -*-

"""
    colorful
    ~~~~~~~~

    Terminal string styling done right, in Python.

    :copyright: (c) 2017 by Timo Furrer <tuxtimo@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
import re


def hex_to_rgb(value):
    """
    Convert the given hex string to a
    valid RGB channel triplet.
    """
    value = value.lstrip('#')
    length = len(value)

    check_hex(value, length)

    step = int(length / 3)
    return tuple(int(value[i:i+step], 16) for i in range(0, length, step))


def check_hex(value, length):
    if not re.search(r'[0-9a-f]', value, re.I):
        raise ValueError('Invalid Hex String: #{}'.format(value))

    if length not in (3, 6):
        raise ValueError('Hex string #{} is too long'.format(value))
