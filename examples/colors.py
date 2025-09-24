# -*- coding: utf-8 -*-

"""
colorful
~~~~~~~~

Terminal string styling done right, in Python.

:copyright: (c) 2017 by Timo Furrer <tuxtimo@gmail.com>
:license: MIT, see LICENSE for more details.
"""

import sys

import colorful


def show():
    """
    Show the modifiers and colors
    """
    # modifiers
    sys.stdout.write(colorful.bold('bold') + ' ')
    sys.stdout.write(colorful.dimmed('dimmed') + ' ')
    sys.stdout.write(colorful.italic('italic') + ' ')
    sys.stdout.write(colorful.underlined('underlined') + ' ')
    sys.stdout.write(colorful.inversed('inversed') + ' ')
    sys.stdout.write(colorful.concealed('concealed') + ' ')
    sys.stdout.write(colorful.struckthrough('struckthrough') + '\n')

    # foreground colors
    sys.stdout.write(colorful.red('red') + ' ')
    sys.stdout.write(colorful.green('green') + ' ')
    sys.stdout.write(colorful.yellow('yellow') + ' ')
    sys.stdout.write(colorful.blue('blue') + ' ')
    sys.stdout.write(colorful.magenta('magenta') + ' ')
    sys.stdout.write(colorful.cyan('cyan') + ' ')
    sys.stdout.write(colorful.white('white') + '\n')

    # background colors
    sys.stdout.write(colorful.on_red('red') + ' ')
    sys.stdout.write(colorful.on_green('green') + ' ')
    sys.stdout.write(colorful.on_yellow('yellow') + ' ')
    sys.stdout.write(colorful.on_blue('blue') + ' ')
    sys.stdout.write(colorful.on_magenta('magenta') + ' ')
    sys.stdout.write(colorful.on_cyan('cyan') + ' ')
    sys.stdout.write(colorful.on_white('white') + '\n')


if __name__ == '__main__':
    show()
