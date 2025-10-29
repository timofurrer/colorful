"""
colorful
~~~~~~~~

Terminal string styling done right, in Python.

:copyright: (c) 2017 by Timo Furrer <tuxtimo@gmail.com>
:license: MIT, see LICENSE for more details.
"""

import math

# For the ANSI escape code sequences please consult
# https://en.wikipedia.org/wiki/ANSI_escape_code

#: Holds the modifier names in the correct order
MODIFIERS = {
    'reset': (0, 0),
    'bold': (1, 22),
    'dimmed': (2, 22),
    'italic': (3, 23),
    'underlined': (4, 24),
    'blinkslow': (5, 25),
    'blinkrapid': (6, 25),
    'inversed': (7, 27),
    'concealed': (8, 28),
    'struckthrough': (9, 29)
}

#: Holds the offset for resetting the modifiers
MODIFIER_RESET_OFFSET = 21

#: Holds the start index for the fore- and background colors
FOREGROUND_COLOR_OFFSET = 30
BACKGROUND_COLOR_OFFSET = 40

#: Holds the offset to reset the color back to default.
#  this number has to be added to either ``FOREGROUND_COLOR_OFFSET`` or
#  ``BACKGROUND_COLOR_OFFSET`` to get an usable ANSI escape code.
COLOR_CLOSE_OFFSET = 9

#: Holds the Control Sequence Introducer
CSI = '\033['

#: Holds the base ANSI escape code
ANSI_ESCAPE_CODE = '{csi}{{code}}m'.format(csi=CSI)

#: Holds the placeholder for the nest indicators
NEST_PLACEHOLDER = ANSI_ESCAPE_CODE.format(code=26)


def round(value):
    x = math.floor(value)
    if (value - x) < 0.5:
        return int(x)
    return int(math.ceil(value))


def rgb_to_ansi256(r, g, b):
    """
    Convert RGB to ANSI 256 color
    """
    if r == g and g == b:
        if r < 8:
            return 16
        if r > 248:
            return 231

        return round(((r - 8) / 247.0) * 24) + 232

    ansi_r = 36 * round(r / 255.0 * 5.0)
    ansi_g = 6 * round(g / 255.0 * 5.0)
    ansi_b = round(b / 255.0 * 5.0)
    ansi = 16 + ansi_r + ansi_g + ansi_b
    return ansi


def rgb_to_ansi16(r, g, b, use_bright=False):
    """
    Convert RGB to ANSI 16 color
    """
    ansi_b = round(b / 255.0) << 2
    ansi_g = round(g / 255.0) << 1
    ansi_r = round(r / 255.0)
    ansi = (90 if use_bright else 30) + (ansi_b | ansi_g | ansi_r)

    return ansi
