"""
colorful
~~~~~~~~

Terminal string styling done right, in Python.

:copyright: (c) 2017 by Timo Furrer <tuxtimo@gmail.com>
:license: MIT, see LICENSE for more details.
"""

import os
import sys
import copy
import types
import platform
from contextlib import contextmanager

from .core import Colorful
from . import terminal

#: Holds the current version
__version__ = '0.5.8'

# if we are on Windows we have to init colorama
if platform.system() == 'Windows':
    os.system('color')


class ColorfulModule(types.ModuleType):
    """
    Module Type object for dynamic attribute access on
    this module.
    """
    def __init__(self, colorful, *args):
        super().__init__(*args)
        self.colorful = colorful

    @contextmanager
    def with_setup(self, colormode=None, colorpalette=None, extend_colors=False):
        """
        Return a new Colorful object with the given color config.
        """
        colorful = Colorful(
            colormode=self.colorful.colormode,
            colorpalette=copy.copy(self.colorful.colorpalette)
        )

        colorful.setup(
            colormode=colormode, colorpalette=colorpalette, extend_colors=extend_colors
        )
        yield colorful

    @contextmanager
    def with_8_ansi_colors(self):
        yield Colorful(
            colormode=terminal.ANSI_8_COLORS,
            colorpalette=copy.copy(self.colorful.colorpalette)
        )

    @contextmanager
    def with_16_ansi_colors(self):
        yield Colorful(
            colormode=terminal.ANSI_16_COLORS,
            colorpalette=copy.copy(self.colorful.colorpalette)
        )

    @contextmanager
    def with_256_ansi_colors(self):
        yield Colorful(
            colormode=terminal.ANSI_256_COLORS,
            colorpalette=copy.copy(self.colorful.colorpalette)
        )

    @contextmanager
    def with_true_colors(self):
        yield Colorful(
            colormode=terminal.TRUE_COLORS,
            colorpalette=copy.copy(self.colorful.colorpalette)
        )

    @contextmanager
    def with_palette(self, colorpalette):
        yield Colorful(
            colormode=self.colorful.colormode,
            colorpalette=colorpalette
        )

    @contextmanager
    def with_updated_palette(self, colorpalette):
        colorful = Colorful(
            colormode=self.colorful.colormode,
            colorpalette=copy.copy(self.colorful.colorpalette),
        )
        colorful.update_palette(colorpalette)
        yield colorful

    @contextmanager
    def with_style(self, style_name):
        colorful = Colorful(
            colormode=self.colorful.colormode,
            colorpalette={},
        )
        colorful.use_style(style_name)
        yield colorful

    def __getattr__(self, name):
        """
        Dynamically get methods from Colorful object.
        """
        # check if original module had the requested attribute
        # if yes, we have to return it since we don't want to
        # break the module functionality
        orig_module = __name__ + '_orig'
        if orig_module in sys.modules:
            try:
                return getattr(sys.modules[orig_module], name)
            except AttributeError:
                pass  # fallback to colorful functionality

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
