# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

*Nothing here yet.*

## [v0.5.7]
## Fixed
- Read version from ast.Constant instead of ast.Str thanks @carlwgeorge
- fix: DualOutput object has no attribute isatty thanks @HollowMan6
- Test Python 3.13 support
- Unsupported Python versions 3.4, 3.5, 3.6 are not tested anymore


## [v0.5.6]
## Fixed
- Fix PEP420 Implicit name space thanks @MocioF
- Test Python 3.12 support

## [v0.5.5]
## Fixed
- Fix `setup(colormode=NO_COLORS)`
- Fix correctnes of `__str__` to return always a str
- Drop Python 2 support
- Test Python 3.5 - Python 3.11

## [v0.5.4]
## Fixed
- `__getattr__` protocol implementation

## [v0.5.3]
## Fixed
- Support equals protocol for ColorfulStyle objects

## [v0.5.2]
## Fixed
- Expose the path to the built-in `colornames` color palette. Refs #31

## [v0.5.1]
## Fixed
- Removed placeholder artifacts (`[26m`) when coloring is disabled

## [v0.5.0]
## Added
- Support for color names in a JSON file
- Built-in support for [color-names](https://github.com/meodai/color-names)

## [v0.4.5]

## Fixed
- Reading files in UTF-8 in setup.py

## [v0.4.4]

## Added
- Official Python 3.7 support

## [v0.4.3]

## Fixed
- Catch AttributeError in case sys.stdout was monkey patched. Refs #15

## [v0.4.2]

## Fixed
- If stdout default encoding is not set, UTF-8 is assumed

## [v0.4.1]

## Fixed
- Support for Chinese and other languages requiring unicode. Refs #9

## [v0.4.0]
- Officially support PyPy 5.6, including Python 2 and 3 support

## [v0.3.12]
- Improve support for nesting styles with `str.format()`

## [v0.3.11]
- Support original module functionality for module hack

## [v0.3.10]
- Add disable method

## [v0.3.9]

### Fixed
- Augment add a `str()` to `ColorfulString`

## [v0.3.8]

### Added
- Support creating unstyled ColorfulString

## [v0.3.7]

### Added
- Support augmented add for ColorfulString's
- Validate hex string for RGB colors

## [v0.3.6]

### Added
- Combine and Pipe Styles

## [v0.3.5]

### Added
- Support for Windows using colorama

## [v0.3.4]

### Added
- Implement Colorful.print() method
- Support env variable to point to local rgb.txt file

## [v0.3.3]

This release is just to fix the PyPI project page.

## [v.0.3.2]

### Added
- Support for styling objects which implement the `str()` protocol

## [v0.3.1]

### Added
- Correctly support `len()`
- Support nesting styles
- Improved documentation

## [v0.3.0]

- Initial release

[Unreleased]: https://github.com/timofurrer/colorful/compare/v0.5.6...HEAD
[v0.5.5]: https://github.com/timofurrer/colorful/compare/v0.5.5...v0.5.6
[v0.5.5]: https://github.com/timofurrer/colorful/compare/v0.5.4...v0.5.5
[v0.5.4]: https://github.com/timofurrer/colorful/compare/v0.5.3...v0.5.4
[v0.5.3]: https://github.com/timofurrer/colorful/compare/v0.5.2...v0.5.3
[v0.5.2]: https://github.com/timofurrer/colorful/compare/v0.5.1...v0.5.2
[v0.5.1]: https://github.com/timofurrer/colorful/compare/v0.5.0...v0.5.1
[v0.5.0]: https://github.com/timofurrer/colorful/compare/v0.4.5...v0.5.0
[v0.4.5]: https://github.com/timofurrer/colorful/compare/v0.4.4...v0.4.5
[v0.4.4]: https://github.com/timofurrer/colorful/compare/v0.4.3...v0.4.4
[v0.4.3]: https://github.com/timofurrer/colorful/compare/v0.4.2...v0.4.3
[v0.4.2]: https://github.com/timofurrer/colorful/compare/v0.4.1...v0.4.2
[v0.4.1]: https://github.com/timofurrer/colorful/compare/v0.4.0...v0.4.1
[v0.4.0]: https://github.com/timofurrer/colorful/compare/v0.3.12...v0.4.0
[v0.3.12]: https://github.com/timofurrer/colorful/compare/v0.3.11...v0.3.12
[v0.3.11]: https://github.com/timofurrer/colorful/compare/v0.3.10...v0.3.11
[v0.3.10]: https://github.com/timofurrer/colorful/compare/v0.3.9...v0.3.10
[v0.3.9]: https://github.com/timofurrer/colorful/compare/v0.3.8...v0.3.9
[v0.3.8]: https://github.com/timofurrer/colorful/compare/v0.3.7...v0.3.8
[v0.3.7]: https://github.com/timofurrer/colorful/compare/v0.3.6...v0.3.7
[v0.3.6]: https://github.com/timofurrer/colorful/compare/v0.3.5...v0.3.6
[v0.3.5]: https://github.com/timofurrer/colorful/compare/v0.3.4...v0.3.5
[v0.3.4]: https://github.com/timofurrer/colorful/compare/v0.3.3...v0.3.4
[v0.3.3]: https://github.com/timofurrer/colorful/compare/v0.3.2...v0.3.3
[v0.3.2]: https://github.com/timofurrer/colorful/compare/v0.3.1...v0.3.2
[v0.3.1]: https://github.com/timofurrer/colorful/compare/v0.3.0...v0.3.1
[v0.3.0]: https://github.com/timofurrer/colorful/compare/466cfeddee681c8221ab981018597c01...v0.3.0
