"""Setup script for the psy-reg package."""

# Disclaimer
# ----------
#
# Copyright (C) 2021 Helmholtz-Zentrum Hereon
# Copyright (C) 2020-2021 Helmholtz-Zentrum Geesthacht
# Copyright (C) 2016-2021 University of Lausanne
#
# This file is part of psy-reg and is released under the GNU LGPL-3.O license.
# See COPYING and COPYING.LESSER in the root of the repository for full
# licensing details.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3.0 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU LGPL-3.0 license for more details.
#
# You should have received a copy of the GNU LGPL-3.0 license
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys

import versioneer


def readme():
    with open('README.rst') as f:
        return f.read()


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ''

    def run_tests(self):
        import shlex
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


cmdclass = versioneer.get_cmdclass({'test': PyTest})


setup(name='psy-reg',
      version=versioneer.get_version(),
      description=(
          'Psyplot plugin for visualizing and calculating regression plots'
      ),
      long_description=readme(),
      long_description_content_type="text/x-rst",
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
      ],
      project_urls={
          'Documentation': 'https://psyplot.github.io/psy-reg',
          'Source': 'https://github.com/psyplot/psy-reg',
          'Tracker': 'https://github.com/psyplot/psy-reg/issues',
      },
      keywords='visualization netcdf raster cartopy earth-sciences psyplot',
      url='https://github.com/psyplot/psy-reg',
      author='Philipp S. Sommer',
      author_email='psyplot@hereon.de',
      license="LGPL-3.0-only",
      packages=find_packages(exclude=['docs', 'tests*', 'examples']),
      python_requires=">=3.7",
      install_requires=[
          'psyplot',
          'psy-simple>=1.3.0',
          'statsmodels',
          'scipy',
      ],
      tests_require=['pytest'],
      cmdclass=cmdclass,
      entry_points={'psyplot': ['plugin=psy_reg.plugin',
                                'patches=psy_reg.plugin:patches']},
      zip_safe=False)
