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
    with colorful.with_style('solarized') as c:
        # modifiers
        sys.stdout.write(c.bold('bold') + ' ')
        sys.stdout.write(c.dimmed('dimmed') + ' ')
        sys.stdout.write(c.italic('italic') + ' ')
        sys.stdout.write(c.underlined('underlined') + ' ')
        sys.stdout.write(c.inversed('inversed') + ' ')
        sys.stdout.write(c.concealed('concealed') + ' ')
        sys.stdout.write(c.struckthrough('struckthrough') + '\n')

        # foreground colors
        sys.stdout.write(c.yellow('yellow') + ' ')
        sys.stdout.write(c.red('orange') + ' ')
        sys.stdout.write(c.red('red') + ' ')
        sys.stdout.write(c.magenta('magenta') + ' ')
        sys.stdout.write(c.magenta('violet') + ' ')
        sys.stdout.write(c.blue('blue') + ' ')
        sys.stdout.write(c.cyan('cyan') + ' ')
        sys.stdout.write(c.green('green') + '\n')

        # background colors
        sys.stdout.write(c.on_yellow('yellow') + ' ')
        sys.stdout.write(c.on_red('orange') + ' ')
        sys.stdout.write(c.on_red('red') + ' ')
        sys.stdout.write(c.on_magenta('magenta') + ' ')
        sys.stdout.write(c.on_magenta('violet') + ' ')
        sys.stdout.write(c.on_blue('blue') + ' ')
        sys.stdout.write(c.on_cyan('cyan') + ' ')
        sys.stdout.write(c.on_green('green') + '\n')


if __name__ == '__main__':
    show()

