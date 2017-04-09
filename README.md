# colorful

Terminal string styling done right, in Python :tada:

## Here's a tease

```python
import colorful

# create a colored string using clever method translation
print(colorful.bold_white('Hello World'))
# create a colored string using `str.format()`
print('{c.bold}{c.lightCoral_on_white}Hello World{c.reset}'.format(c=colorful))

# use true colors
colorful.use_true_colors()

# extend default color palette
colorful.update_palette({'mint': '#c5e8c8'})
print(colorful.mint_on_snow('Wow, this is actually mint'))

# choose specific color mode for one block
with colorful.with_8bit_ansi_colors() as c:
    print(c.bold_green('colorful is awesome!'))

# choose a predefined style for color names
with colorful.with_style('solarized') as c:
    # print the official solarized colors
    print(c.yellow('yellow'), c.orange('orange'), c.red('red'), c.magenta('magenta'),
        c.violet('violet'), c.blue('blue') c.cyan('cyan'), c.green('green'))

# create and choose your own color palette
MY_COMPANY_PALETTE = {
    'companyOrange': '#f4b942',
    'companyBaige': '#e8dcc5'
}
with colorful.with_palette(my_company_palette) as c:
    print(c.companyOrange_on_companyBaige('Thanks for choosing our product!'))
```

## Key Features

* expressive and consistent API
* support for different color modes (8bit ANSI, 256 ANSI, true colors)
* support for predefined awesome styles (solarized, ...)
* support for custom color palettes
* support for different platforms (using colorama on windows)
* context managers for clean color mode, color palette or style switch

## Color modes

These days terminals not only support the ancient 8bit ANSI colors but often they support up to 16 Million colors with *[true color](https://en.wikipedia.org/wiki/Color_depth#True_color_.2824-bit.29)*. And if they don't support *true color* they might support the *[256 ANSI color palette](https://en.wikipedia.org/wiki/ANSI_escape_code#Colors)* at least.

**colorful** supports the following color modes:

* no colors / disable (``colorful.NO_COLORS``)
* 8 colors -> 8 bit ANSI colors (``colorful.ANSI_8BIT_COLORS``)
* 256 colors -> 256 ANSI color palette (24bit ``colorful.ANSI_256_COLORS``)
* 16'777'215 colors -> true color (``colorful.TRUE_COLORS``)

***

*<p align="center">This project is published under [MIT](LICENSE).<br>A [Timo Furrer](https://tuxtimo.me) project.<br>- :tada: -</p>*
