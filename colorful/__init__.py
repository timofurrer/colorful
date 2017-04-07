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

from .core import Colorful


class ColorfulModule(types.ModuleType):
    """
    Module Type object for dynamic attribute access on
    this module.
    """
    def __init__(self, colorful, *args):
        super(ColorfulModule, self).__init__(*args)
        self.colorful = colorful

    def __getattr__(self, name):
        """
        Dynamically get methods from Colorful object.
        """
        print('In ColorfulModule.__getattr__ {0}'.format(name))
        return getattr(self.colorful, name)


if os.environ.get('COLORFUL_NO_MODULE_OVERWRITE', '0') != '1':
    # expose the Colorful class as module
    sys.modules[__name__] = ColorfulModule(Colorful(), __name__)
