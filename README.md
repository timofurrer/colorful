# colorful

[![Actions Status](https://github.com/timofurrer/colorful/workflows/Continuous%20Integration/badge.svg)](https://github.com/timofurrer/colorful/actions)
[![codecov.io](https://codecov.io/github/timofurrer/colorful/coverage.svg?branch=master)](https://codecov.io/github/timofurrer/colorful?branch=master)
[![PyPI version](https://badge.fury.io/py/colorful.svg)](https://badge.fury.io/py/colorful)
[![PyPI](https://img.shields.io/pypi/pyversions/colorful.svg)](https://pypi.python.org/pypi/colorful)
[![PyPI](https://img.shields.io/pypi/wheel/colorful.svg)](https://pypi.python.org/pypi/colorful)

Terminal string styling done right, in Python :tada:

## Here's a tease

![colorful example](examples/basic_example.png)

```python
import colorful as cf

# create a colored string using clever method translation
print(cf.bold_white('Hello World'))
# create a colored string using `str.format()`
print('{c.bold}{c.lightCoral_on_white}Hello World{c.reset}'.format(c=cf))

# nest colors
print(cf.red('red {0} red'.format(cf.white('white'))))
print(cf.red('red' + cf.white(' white ', nested=True) + 'red'))

# combine styles with strings
print(cf.bold & cf.red | 'Hello World')

# use true colors
cf.use_true_colors()

# extend default color palette
cf.update_palette({'mint': '#c5e8c8'})
print(cf.mint_on_snow('Wow, this is actually mint'))

# choose a predefined style
cf.use_style('solarized')
# print the official solarized colors
print(cf.yellow('yellow'), cf.orange('orange'),
    cf.red('red'), cf.magenta('magenta'),
    cf.violet('violet'), cf.blue('blue'),
    cf.cyan('cyan'), cf.green('green'))

# directly print with colors
cf.print('{c.bold_blue}Hello World{c.reset}')

# choose specific color mode for one block
with cf.with_8_ansi_colors() as c:
    print(c.bold_green('colorful is awesome!'))

# create and choose your own color palette
MY_COMPANY_PALETTE = {
    'companyOrange': '#f4b942',
    'companyBaige': '#e8dcc5'
}
with cf.with_palette(MY_COMPANY_PALETTE) as c:
    print(c.companyOrange_on_companyBaige('Thanks for choosing our product!'))

# use f-string (only Python >= 3.6)
print(f'{cf.bold}Hello World')

# support for chinese
print(cf.red('你好'))
```

## Key Features

* expressive and consistent API ([docs](#style-a-string))
* support for different color modes (8 ANSI, 256 ANSI, true colors) ([docs](#color-modes))
* support for predefined awesome styles (solarized, ...) ([docs](#styles))
* support for custom color palettes ([docs](#color-palette))
* support nesting styles ([docs](#nesting-styles))
* support for different platforms (using colorama on Windows)
* context managers for clean color mode, color palette or style switch ([docs](#temporarily-change-colorful-settings))
* support `len()` on colored strings ([docs](#correctly-support-the-len-protocol))
* support color names from [X11 rgb.txt](https://en.wikipedia.org/wiki/X11_color_names) ([docs](#1-style-a-string-with-a-method-call-colorfulmodifiers_fgcolor_on_bgcolorstr-nestedfalse))
* no dependencies

## Usage

**colorful** supports all major Python versions: *3.5*, *3.6* and *3.7*, *3.8*, *3.9*, *3.10*, *3.11*. <br>
We recommend to use the latest version released on [PyPI](https://pypi.python.org/pypi/colorful):

```bash
pip install colorful
```

**colorful** does not require any special setup in order to be used:

```python
import colorful as cf

print(cf.italic_coral_on_beige('Hello World'))
print(cf.italic & cf.coral_on_beige | 'Hello World')
print('{c.italic_coral_on_beige}Hello World{c.reset}'.format(c=cf))
```

Note: the entire documentation assumes `colorful` to be imported as `cf`.

See the [Style a string](https://github.com/timofurrer/colorful#style-a-string) section for more information!

### Color modes

These days terminals not only support the ancient 8 ANSI colors but often they support up to 16 Million colors with *[true color](https://en.wikipedia.org/wiki/Color_depth#True_color_.2824-bit.29)*. And if they don't support *true color* they might support the *[256 ANSI color palette](https://en.wikipedia.org/wiki/ANSI_escape_code#Colors)* at least.

**colorful** supports the following color modes:

* no colors / disable (``cf.NO_COLORS``)
* 8 colors -> 8 ANSI colors (``cf.ANSI_8_COLORS``)
* 256 colors -> 256 ANSI color palette (8bit ``cf.ANSI_256_COLORS``)
* 16'777'215 colors -> true color (24bit, ``cf.TRUE_COLORS``)

By default *colorful* tries to auto detect the best supported color mode by your terminal. Consult [`cf.terminal`](https://github.com/timofurrer/colorful/blob/master/colorful/terminal.py) for more details.

However, sometimes it makes sense to specify what color mode should be used.<br>
**colorful** provides multiple ways to do so:

#### (1) specify color mode globally via Python API

```python
cf.disable()
cf.use_8_ansi_colors()
cf.use_256_ansi_colors()
cf.use_true_colors()
```

If you change the color mode during runtime it takes affect immediately and globally.

#### (2) enforce color mode globally via environment variable

```bash
COLORFUL_DISABLE=1 python eggs.py  # this process will not use ANY coloring
COLORFUL_FORCE_8_COLORS=1 python eggs.py  # this process will use 8 ANSI colors by default
COLORFUL_FORCE_256_COLORS=1 python eggs.py  # this process will use 256 ANSI colors by default
COLORFUL_FORCE_TRUE_COLORS=1 python eggs.py  # this process will use true colors by default
```

#### (3) specify color mode locally via Python API (contextmanager)

```python
with cf.with_8_ansi_colors() as c:
    print(c.italic_coral_on_beige('Hello world'))

with cf.with_256_ansi_colors() as c:
    print(c.italic_coral_on_beige('Hello world'))

with cf.with_true_colors() as c:
    print(c.italic_coral_on_beige('Hello world'))
```

### Color palette

**colorful**'s Python API is based on *color names* like in `cf.bold_white_on_black('Hello')`. During runtime these *color names* are translated into proper [ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code) sequences supported by the *color mode* in use. However, all *color names* are registered in a **color palette** which is basically a mapping between the *color names* and it's corresponding RGB value. Very much like this:

```python
color_palette_example = {
    'black': '#000000',
    'white': '#FFFFFF',
}
```

*Note: Depending on the color mode which is used the RGB value will be reduced to fit in the value domain of the color mode.*

The default color palette is the [X11 rgb.txt](https://en.wikipedia.org/wiki/X11_color_names) palette - it's shipped with *colorful*, thus, you don't have to provide your own.
*colorful* ships with a second built-in [color palette called *colornames*](https://codepen.io/meodai/full/VMpNdQ/).
Those colors are from the curated list of the [color-names](https://github.com/meodai/color-names) repository.
You can use those via the `cf.setup()` method, like this:


```python
cf.setup(colorpalette=cf.COLORNAMES_COLORS)
```

If you wish to have another color palette from a file as your default color palette you can set the `COLORFUL_DEFAULT_COLOR_PALETTE` environment variable to this file:

```bash
COLORFUL_DEFAULT_COLOR_PALETTE=/usr/share/X11/rgb.txt python spam.py
```

The file either has to be a txt file like the X11 rgb.txt or a JSON file:

```json
[
    {"name": "18th Century Green", "hex":"#a59344"},
    {"name": "1975 Earth Red", "hex":"#7a463a"}
]
```

#### Custom color palette
**colorful** supports to update or replace the default color palette with custom colors. The colors have to be specified as RGB hex or channel values:

```python
# corporate identity colors
ci_colors = {
    'mint': '#c5e8c8',  # RGB hex value
    'darkRed': '#c11b55',  # RGB hex value
    'lightBlue': (15, 138, 191)  # RGB channel triplet
}

# replace the default palette with my custom one
cf.use_palette(ci_colors)
# update the default palette with my custom one
cf.update_palette(ci_colors)

# we can use these colors
print(cf.italic_mint_on_darkRed('My company'))
```

### Styles

**colorful** supports some famous color palettes using what's called *styles* in colorful:

```python
cf.use_style('solarized')

# print the official solarized colors
print(cf.yellow('yellow'), cf.orange('orange'),
    cf.red('red'), cf.magenta('magenta'),
    cf.violet('violet'), cf.blue('blue'),
    cf.cyan('cyan'), cf.green('green'))
```

The following styles are already supported:

<details open>
 <summary>solarized - <a href="http://ethanschoonover.com/solarized">Website</a></summary>
 <br>
 <img src="https://github.com/timofurrer/colorful/blob/master/examples/solarized_base_colors.png" alt="solarized colors">
</details>
<details open>
 <summary>monokai</summary>
 <br>
 <img src="https://github.com/timofurrer/colorful/blob/master/examples/monokai_base_colors.png" alt="monokai colors">
</details>
<br>

*Note: if you know some awesome color palettes which could be a new style in colorful, please contribute it!*

### Style a string

**colorful** provides multiple ways to use style a string. Most useful and expressive is probably the *method syntax* where you specify the modifiers and colors in the method name itself and pass the string as argument to this method. However, you can use all the following methods to achive similars things:

#### (1) Style a string with a method call `cf.[<modifiers...>]_[<fgColor>]_[on_<bgColor>](str, nested=False)`

```python
print(cf.red('I am red'))
print(cf.italic_yellow('I am italic and yellow'))
print(cf.black_on_white('I am black on white'))
```

The method syntax can be one of:

* `cf.<modifier>`
* `cf.<modifier1>_<modifier2>`
* `cf.<fg_color>`
* `cf.on_<bg_color>`
* `cf.<modifiers>_<fg_color>`
* `cf.<modifiers>_<bg_color>`
* `cf.<fg_colors>_on_<bg_color>`
* `cf.<modifiers>_<fg_color>_on_<bg_color>`

*Note that multiple `<modifier>`s can be specified at once.*

Available modifiers are:

* reset (explicitely reset all styles before the passed argument)
* bold
* dimmed (not widely supported)
* italic
* underlined
* blinkslow
* blinkrapid
* inversed (not widely supported)
* concealed (not widely supported)
* struckthrough

The available colors depend on the [color palette](#color-palette) you are using. By default all [X11 rgb.txt colors](https://en.wikipedia.org/wiki/X11_color_names) are available.

The type of the return value of such a *style method* is `colorful.ColorfulString`. It correctly supports all `str()` methods including [`len()`](#correctly-support-the-len-protocol).

As you can see from the syntax in the section name, **colorful** supports nesting styles. See [Nesting styles](#nesting-styles).

#### (2) Style a string with `&` and `|`

**colorful** implements the `__or__` and `__and__` protocol to combine styles and pipe strings into them:

```python
print(cf.bold & cf.red | 'Hello World')
print(cf.bold_red_on_black | 'Hello World')
print(cf.bold | cf.red_on_black('Hello World')
```

*Note: the piping `|` has the same effect as doing a method call to the style.<br>
So you could do `(cf.bold & cf.red)('Hello World')`*

#### (3) Style a string with `cf.format(string, *args, **kwargs)`

```python
print(cf.format('{c.red}I am {what}{c.close_fg_color}', what='red'))
# alternatively to ``c.close_fg_color`` you can reset every style with ``c.reset``
print(cf.format('{c.red}I am red{c.reset}'))

print(cf.format('{c.italic_yellow}I am italic and yellow{c.no_italic}{c.close_fg_color}'))
print(cf.format('{c.black_on_white}I am black on white{c.close_fg_color}{c.close_bg_color}'))
```

**colorful** will replace the `{c.<style>}` with the correspnding style. It's **not** necessary to pass a colorful object for `c` to `format()` - colorful will handle that. Every other format argument (`{<name>}`) has to be pass to the `cf.format()` call as *args* or *kwarg*.

Note: The same syntax, modifiers and colors for the style in `{c.<style>}` can be used as for [(1) Style a string with a method call](#1-style-a-string-with-a-method-call).

#### (4) Style and print a string with `cf.print(*strings, sep=' ', end='\n', file=sys.stdout, flush=False)`

```python
cf.print('{c.italic_yellow}I am italic and yellow{c.no_italic}{c.close_fg_color}')
cf.print('{c.red}I am red{c.reset}', end='', file=open('log.txt', 'a+'))
```

The `cf.print()` method accepts the same arguments as the Python 3.X [built-in print()](https://docs.python.org/3/library/functions.html#print) function.

#### (5) Style a string with [`str.format()`](https://docs.python.org/3.6/library/stdtypes.html#str.format)

```python
print('{c.red}I am red{c.close_fg_color}'.format(c=cf))
# alternatively to ``c.close_fg_color`` you can reset every style with ``c.reset``
print('{c.red}I am red{c.reset}'.format(c=cf))

print('{c.italic_yellow}I am italic and yellow{c.no_italic}{c.close_fg_color}'.format(
    c=cf))
print('{c.black_on_white}I am black on white{c.close_fg_color}{c.close_bg_color}'.format(
    c=cf))
```

Note: The same syntax, modifiers and colors for the style in `{c.<style>}` can be used as for [(1) Style a string with a method call](#1-style-a-string-with-a-method-call).

#### Nesting styles

**colorful** supports to nest styles with it's [method call syntax](#1-style-a-string-with-a-method-call) when setting the parameter `nested` to `True`.
If you are using `str.format()` like in the first example below you don't even need the `nested=True` flag!

The following examples show the behavior:

```python
print(cf.red('red {0} red'.format(cf.white('white'))))
print(cf.red('red' + cf.white(' white ', nested=True) + 'red'))

# if using ``nested=True`` but you don't actually nest
# it's absolutely fine and will work as expected.
print(cf.red('red', nested=True) + ' default color')
```

#### Correctly support the [`len()` protocol](https://docs.python.org/3/library/functions.html#len)

**colorful** correctly supports the `len()` protocol (`__len__`) on the styled strings. As mentioned above, when you style a string a `colorful.ColorfulString` object is returned. This object returns the length (when calling `len()`) as it would be for the *unstyled string* to integrate styled strings seemlessly into your application.

```python
>>> s = 'Hello World'
>>> len(s)
11
>>> len(cf.yellow(s))
11
>>> assert len(s) == len(cf.yellow(s))
```

### Temporarily change colorful settings

**colorful** provides a hand full of convenient context managers to change the colorful settings temporarily:

#### (1) change color mode

Use 8 ANSI colors:

```python
with cf.with_8_ansi_colors() as c:
    print(c.red('I am red'))
```

Use 256 ANSI colors:

```python
with cf.with_256_ansi_colors() as c:
    print(c.red('I am red'))
```

Use true colors:

```python
with cf.with_true_colors() as c:
    print(c.red('I am red'))
```

#### (2) change color palette

```python
# replace the entire color palette
with cf.with_palette(my_palette) as c:
    print(c.customRed('I am custom red'))

# update the color palette
with cf.with_updated_palette(my_palette) as c:
    print(c.customRed('I am custom red'))
```

#### (3) change style

```python
with cf.with_style('solarized') as c:
    print(c.red('I am solarized red'))
```

***

*<p align="center">This project is published under [MIT](LICENSE).<br>A [Timo Furrer](https://tuxtimo.me) project.<br>- :tada: -</p>*
