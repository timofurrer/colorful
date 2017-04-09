# -*- coding: utf-8 -*-

"""
    colorful
    ~~~~~~~~

    Terminal string styling done right, in Python.

    :copyright: (c) 2017 by Timo Furrer <tuxtimo@gmail.com>
    :license: MIT, see LICENSE for more details.
"""

# This module provides the X11 rgb.txt as python dictionary.
# See https://en.wikipedia.org/wiki/X11_color_names for more information

import os

from . import utils


def parse_rgb_txt_file(path=None):
    """
    Parse the given rgb.txt file into a Python dict.

    :param str path: the path to the X11 rgb.txt file
    """
    #: Holds the generated color dict
    color_dict = {}

    # get the default X11 rgb.txt file shipped with colorful
    if path is None:
        path = os.path.join(os.path.dirname(__file__), 'data', 'rgb.txt')

    def __make_valid_color_name(name):
        """
        Convert the given name into a valid colorname
        """
        if len(name) == 1:
            name = name[0]
            return name[:1].lower() + name[1:]

        return name[0].lower() + ''.join(word.capitalize() for word in name[1:])

    with open(path, 'r') as rgb_txt:
        for line in rgb_txt:
            line = line.strip()
            if not line or line.startswith('!'):
                continue  # skip comments

            parts = line.split()
            color_dict[__make_valid_color_name(parts[3:])] = (int(parts[0]),
                                                              int(parts[1]),
                                                              int(parts[2]))

    return color_dict


def sanitize_color_palette(colorpalette):
    """
    Sanitze the given color palette so it can
    be safely used by Colorful.

    It will convert colors specified in hex RGB to
    a RGB channel triplet.
    """
    new_palette = {}
    for key, value in colorpalette.items():
        if isinstance(value, str):
            # we assume it's a hex RGB value
            value = utils.hex_to_rgb(value)
        new_palette[key] = value

    return new_palette
