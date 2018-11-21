# -*- coding: utf-8 -*-

"""
    colorful
    ~~~~~~~~

    Terminal string styling done right, in Python.

    :copyright: (c) 2017 by Timo Furrer <tuxtimo@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
import re
import sys

PY2 = sys.version_info.major == 2

if PY2:
    UNICODE = unicode  # noqa
else:
    UNICODE = str

# Catch error in case sys.stdout was patched with an object that doesn't provide
# the 'encoding' attribute.
try:
    DEFAULT_ENCODING = sys.stdout.encoding or 'utf-8'
except AttributeError:
    DEFAULT_ENCODING = 'utf-8'


def hex_to_rgb(value):
    """
    Convert the given hex string to a
    valid RGB channel triplet.
    """
    value = value.lstrip('#')
    check_hex(value)

    length = len(value)
    step = int(length / 3)
    return tuple(int(value[i:i+step], 16) for i in range(0, length, step))


def check_hex(value):
    """
    Check if the given hex value is a valid RGB color

    It should match the format: [0-9a-fA-F]
    and be of length 3 or 6.
    """
    length = len(value)
    if length not in (3, 6):
        raise ValueError('Hex string #{} is too long'.format(value))

    regex = r'[0-9a-f]{{{length}}}'.format(length=length)
    if not re.search(regex, value, re.I):
        raise ValueError('Invalid Hex String: #{}'.format(value))
