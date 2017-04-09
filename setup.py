# -*- coding: utf-8 -*-

"""
    colorful
    ~~~~~~~~

    Terminal string styling done right, in Python.

    :copyright: (c) 2017 by Timo Furrer <tuxtimo@gmail.com>
    :license: MIT, see LICENSE for more details.
"""

import ast
import os
import sys
import codecs
from setuptools import setup, find_packages

# These python versions are explicitly not supported
# by colorful. This is mostly because of the incompatiblities
# with unicode strings. If there is an urgent reason why
# to support it after all or if you have a quick fix
# please open an issue on GitHub.
EXPL_NOT_SUPPORTED_VERSIONS = ((3, 0), (3, 1), (3, 2))

if sys.version_info[0:2] in EXPL_NOT_SUPPORTED_VERSIONS:
    raise SystemExit("colorful does explicitly not support the following python versions "
                     "due to big incompatibilities: {0}".format(EXPL_NOT_SUPPORTED_VERSIONS))


#: Holds the root dir for the project.
PROJECT_ROOT = os.path.dirname(__file__)


class VersionFinder(ast.NodeVisitor):

    def __init__(self):
        self.version = None

    def visit_Assign(self, node):
        try:
            if node.targets[0].id == '__version__':
                self.version = node.value.s
        except:
            pass


def read_version():
    """Read version from __init__.py without loading any files"""
    finder = VersionFinder()
    path = os.path.join(PROJECT_ROOT, 'colorful', '__init__.py')
    with codecs.open(path, 'r', encoding='utf-8') as fp:
        file_data = fp.read().encode('utf-8')
        finder.visit(ast.parse(file_data))

    return finder.version


def local_text_file(*f):
    path = os.path.join(PROJECT_ROOT, *f)
    with open(path, 'rt') as fp:
        file_data = fp.read()

    return file_data


def read_readme():
    """Read README content.
    If the README.rst file does not exist yet
    (this is the case when not releasing)
    only the short description is returned.
    """
    try:
        return local_text_file('README.rst')
    except IOError:
        return __doc__


#: Holds the requirements for colorful
requirements = [
    'colorama;platform_system=="Windows"'
]


if __name__ == '__main__':

    setup(
        name='colorful',
        version=read_version(),
        description=__doc__,
        long_description=read_readme(),
        url='http://github.com/timofurrer/colorful',
        author='Timo Furrer',
        author_email='tuxtimo@gmail.com',
        maintainer='Timo Furrer',
        maintainer_email='tuxtimo@gmail.com',
        include_package_data=True,
        package_data={'': ['colorful/data/*.txt']},
        packages=find_packages(exclude=['*tests*']),
        install_requires=requirements,
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'License :: OSI Approved :: MIT License',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: POSIX',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: Implementation',
        ]
    )
