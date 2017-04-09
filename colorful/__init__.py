# -*- coding: utf-8 -*-

"""
    colorful
    ~~~~~~~~

    Terminal string styling done right, in Python.

    :copyright: (c) 2017 by Timo Furrer <tuxtimo@gmail.com>
    :license: MIT, see LICENSE for more details.
"""

import os
import sys
import types
from contextlib import contextmanager

from .core import Colorful
from . import terminal


class ColorfulModule(types.ModuleType):
    """
    Module Type object for dynamic attribute access on
    this module.
    """

    # re-expose the color modes from ``colorful.terminal``
    # on a package level.
    NO_COLORS = terminal.NO_COLORS
    ANSI_8BIT_COLORS = terminal.ANSI_8BIT_COLORS
    ANSI_16BIT_COLORS = terminal.ANSI_16BIT_COLORS
    ANSI_256_COLORS = terminal.ANSI_256_COLORS
    TRUE_COLORS = terminal.TRUE_COLORS

    def __init__(self, colorful, *args):
        super(ColorfulModule, self).__init__(*args)
        self.colorful = colorful

    @contextmanager
    def with_config(self, config):
        """
        Return a new Colorful object with the given color config.
        """
        yield Colorful(
            colormode=config.get('colormode'),
            colorpalette=config.get('colorpalette')
        )

    @contextmanager
    def use_8bit_ansi_colors(self):
        yield Colorful(colormode=terminal.ANSI_8BIT_COLORS)

    @contextmanager
    def use_16bit_ansi_colors(self):
        yield Colorful(colormode=terminal.ANSI_16BIT_COLORS)

    @contextmanager
    def use_256_ansi_colors(self):
        yield Colorful(colormode=terminal.ANSI_256_COLORS)

    @contextmanager
    def use_true_colors(self):
        yield Colorful(colormode=terminal.TRUE_COLORS)

    def __getattr__(self, name):
        """
        Dynamically get methods from Colorful object.
        """
        return getattr(self.colorful, name)


if os.environ.get('COLORFUL_NO_MODULE_OVERWRITE', '0') != '1':
    # Unfortunately, prior to Python 3.4 the replaced
    # modules gets garbage collected which will
    # destroy all currently imported modules.
    # To prevent this, is to store a backup of the original
    # modules in sys.modules.
    sys.modules[__name__ + '_orig'] = sys.modules[__name__]
    # expose the Colorful class as module
    sys.modules[__name__] = ColorfulModule(Colorful(), __name__)
