# -*- coding: utf-8 -*-

"""
    colorful
    ~~~~~~~~

    Terminal string styling done right, in Python.

    :copyright: (c) 2017 by Timo Furrer <tuxtimo@gmail.com>
    :license: MIT, see LICENSE for more details.
"""

import sys


# Valid color modes for colorful
NO_COLORS = 0
ANSI_8_COLORS = 8
ANSI_16_COLORS = 16
ANSI_256_COLORS = 256
TRUE_COLORS = 0xFFFFFF


def detect_color_support(env):  # noqa
    """
    Detect what color palettes are supported.
    It'll return a valid color mode to use
    with colorful.

    :param dict env: the environment dict like returned by ``os.envion``
    """
    if env.get('COLORFUL_DISABLE', '0') == '1':
        return NO_COLORS

    if env.get('COLORFUL_FORCE_8_COLORS', '0') == '1':
        return ANSI_8_COLORS

    if env.get('COLORFUL_FORCE_16_COLORS', '0') == '1':
        return ANSI_16_COLORS

    if env.get('COLORFUL_FORCE_256_COLORS', '0') == '1':
        return ANSI_256_COLORS

    if env.get('COLORFUL_FORCE_TRUE_COLORS', '0') == '1':
        return TRUE_COLORS

    # if we are not a tty
    if hasattr(sys.stdout, 'isatty') and not sys.stdout.isatty():
        return NO_COLORS

    colorterm_env = env.get('COLORTERM')
    if colorterm_env:
        if colorterm_env in {'truecolor', '24bit'}:
            return TRUE_COLORS

        if colorterm_env in {'8bit'}:
            return ANSI_256_COLORS

    termprog_env = env.get('TERM_PROGRAM')
    if termprog_env:
        if termprog_env in {'iTerm.app', 'Hyper'}:
            return TRUE_COLORS

        if termprog_env in {'Apple_Terminal'}:
            return ANSI_256_COLORS

    term_env = env.get('TERM')
    if term_env:
        if term_env in {'screen-256', 'screen-256color', 'xterm-256', 'xterm-256color'}:
            return ANSI_256_COLORS

        if term_env in {'screen', 'xterm', 'vt100', 'color', 'ansi', 'cygwin', 'linux'}:
            return ANSI_16_COLORS

    if colorterm_env:
        # if there was no match with $TERM either but we
        # had one with $COLORTERM, we use it!
        return ANSI_16_COLORS

    return ANSI_8_COLORS
