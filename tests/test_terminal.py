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

import pytest

# do not overwrite module
os.environ['COLORFUL_NO_MODULE_OVERWRITE'] = '1'

import colorful.terminal as terminal  # noqa


@pytest.mark.skipif(not sys.stdout.isatty(), reason='fails without a tty')
@pytest.mark.parametrize('env,expected', [
    # test force color settings
    ({'COLORFUL_DISABLE': '1'}, terminal.NO_COLORS),
    ({'COLORFUL_FORCE_8_COLORS': '1'}, terminal.ANSI_8_COLORS),
    ({'COLORFUL_FORCE_16_COLORS': '1'}, terminal.ANSI_16_COLORS),
    ({'COLORFUL_FORCE_256_COLORS': '1'}, terminal.ANSI_256_COLORS),
    ({'COLORFUL_FORCE_TRUE_COLORS': '1'}, terminal.TRUE_COLORS),
    # test recommended $COLORTERM variable
    ({'COLORTERM': 'truecolor'}, terminal.TRUE_COLORS),
    ({'COLORTERM': '24bit'}, terminal.TRUE_COLORS),
    ({'COLORTERM': '8bit'}, terminal.ANSI_256_COLORS),
    ({'COLORTERM': 'XYZ'}, terminal.ANSI_16_COLORS),
    # test $TERM_PROGRAM variable
    ({'TERM_PROGRAM': 'iTerm.app'}, terminal.TRUE_COLORS),
    ({'TERM_PROGRAM': 'Hyper'}, terminal.TRUE_COLORS),
    ({'TERM_PROGRAM': 'Apple_Terminal'}, terminal.ANSI_256_COLORS),
    # test $TERM variable values for 256 ANSI colors
    ({'TERM': 'screen-256'}, terminal.ANSI_256_COLORS),
    ({'TERM': 'screen-256color'}, terminal.ANSI_256_COLORS),
    ({'TERM': 'xterm-256'}, terminal.ANSI_256_COLORS),
    ({'TERM': 'xterm-256color'}, terminal.ANSI_256_COLORS),
    # test $TERM variable values for 16 colors
    ({'TERM': 'screen'}, terminal.ANSI_16_COLORS),
    ({'TERM': 'xterm'}, terminal.ANSI_16_COLORS),
    ({'TERM': 'vt100'}, terminal.ANSI_16_COLORS),
    ({'TERM': 'color'}, terminal.ANSI_16_COLORS),
    ({'TERM': 'ansi'}, terminal.ANSI_16_COLORS),
    ({'TERM': 'cygwin'}, terminal.ANSI_16_COLORS),
    ({'TERM': 'linux'}, terminal.ANSI_16_COLORS),
    # test fallback to 8 colors
    ({}, terminal.ANSI_8_COLORS),
    # force disable overrules force colors
    ({
        'COLORFUL_DISABLE': '1',
        'COLORFUL_FORCE_8_COLORS': '1', 'COLORFUL_FORCE_16_COLORS': '1',
        'COLORFUL_FORCE_256_COLORS': '1', 'COLORFUL_FORCE_TRUE_COLORS': '1'
    }, terminal.NO_COLORS),
    # force colors overrules $COLORTERM
    ({
        'COLORFUL_FORCE_TRUE_COLORS': '1',
        'COLORTERM': '24bit'
    }, terminal.TRUE_COLORS),
    # $COLORTERM overrules $TERM_PROGRAM
    ({
        'COLORTERM': 'truecolor',
        'TERM_PROGRAM': 'iTerm.app'
    }, terminal.TRUE_COLORS),
    # $TERM_PROGRAM overrules $TERM with 256 colors
    ({
        'TERM_PROGRAM': 'iTerm.app',
        'TERM': 'xterm-256color'
    }, terminal.TRUE_COLORS)
])
def test_color_support_detection(env, expected):
    """
    Test the terminal color support auto detection
    """
    assert terminal.detect_color_support(env) == expected
