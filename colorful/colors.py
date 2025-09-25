"""
colorful
~~~~~~~~

Terminal string styling done right, in Python.

:copyright: (c) 2017 by Timo Furrer <tuxtimo@gmail.com>
:license: MIT, see LICENSE for more details.
"""

import json

from . import utils


def parse_colors(path):
    """Parse the given color files.

    Supported are:
        * .txt for X11 colors
        * .json for colornames
    """
    if path.endswith(".txt"):
        return parse_rgb_txt_file(path)
    elif path.endswith(".json"):
        return parse_json_color_file(path)

    raise TypeError("colorful only supports .txt and .json files for colors")


def parse_rgb_txt_file(path):
    """
    Parse the given rgb.txt file into a Python dict.

    See https://en.wikipedia.org/wiki/X11_color_names for more information

    :param str path: the path to the X11 rgb.txt file
    """
    #: Holds the generated color dict
    color_dict = {}

    with open(path) as rgb_txt:
        for line in rgb_txt:
            line = line.strip()
            if not line or line.startswith('!'):
                continue  # skip comments

            parts = line.split()
            color_dict[" ".join(parts[3:])] = (int(parts[0]), int(parts[1]), int(parts[2]))

    return color_dict


def parse_json_color_file(path):
    """Parse a JSON color file.

    The JSON has to be in the following format:

    .. code:: json

       [{"name": "COLOR_NAME", "hex": "#HEX"}, ...]

    :param str path: the path to the JSON color file
    """
    with open(path) as color_file:
        color_list = json.load(color_file)

    # transform raw color list into color dict
    color_dict = {c["name"]: c["hex"] for c in color_list}
    return color_dict


def sanitize_color_palette(colorpalette):
    """
    Sanitze the given color palette so it can
    be safely used by Colorful.

    It will convert colors specified in hex RGB to
    a RGB channel triplet.
    """
    new_palette = {}

    def __make_valid_color_name(name):
        """
        Convert the given name into a valid colorname
        """
        if len(name) == 1:
            name = name[0]
            return name[:1].lower() + name[1:]

        return name[0].lower() + ''.join(word.capitalize() for word in name[1:])

    for key, value in colorpalette.items():
        if isinstance(value, str):
            # we assume it's a hex RGB value
            value = utils.hex_to_rgb(value)
        new_palette[__make_valid_color_name(key.split())] = value

    return new_palette
