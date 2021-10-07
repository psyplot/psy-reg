.. psy-reg documentation master file, created by
   sphinx-quickstart on Mon Jul 20 18:01:33 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _psy-reg:

Psyplot plugin for visualizing and calculating regression plots
===============================================================

Welcome to the psyplot plugin for visualizating and calculating regression
plots. This package uses the scipy_ and statsmodels_ packages to evaluate your
data, fit a regression to it and visualize it through the psy-simple_ plugin.

It's plot methods are the :attr:`~psyplot.project.ProjectPlotter.linreg` and
:attr:`~psyplot.project.ProjectPlotter.densityreg` plot methods.

See the :ref:`plot_methods` and examples_ for more information.

.. _psy-simple: https://psyplot.github.io/psy-simple/
.. _statsmodels: https://www.statsmodels.org/stable/index.html
.. _scipy: https://www.scipy.org/
.. _examples: https://psyplot.github.io/examples/

.. start-badges

.. only:: html and not epub

    .. list-table::
        :stub-columns: 1
        :widths: 10 90

        * - docs
          - |docs|
        * - tests
          - |circleci| |appveyor| |codecov|
        * - package
          - |version| |conda| |github| |zenodo|
        * - implementations
          - |supported-versions| |supported-implementations|

    .. |docs| image:: https://img.shields.io/github/deployments/psyplot/psy-reg/github-pages
        :alt: Documentation
        :target: http://psyplot.github.io/psy-reg/

    .. |circleci| image:: https://circleci.com/gh/psyplot/psy-reg/tree/master.svg?style=svg
        :alt: CircleCI
        :target: https://circleci.com/gh/psyplot/psy-reg/tree/master

    .. |appveyor| image:: https://ci.appveyor.com/api/projects/status/48pqaquat9bennac/branch/master?svg=true
        :alt: AppVeyor
        :target: https://ci.appveyor.com/project/psyplot/psy-reg

    .. |codecov| image:: https://codecov.io/gh/psyplot/psy-reg/branch/master/graph/badge.svg
        :alt: Coverage
        :target: https://codecov.io/gh/psyplot/psy-reg

    .. |version| image:: https://img.shields.io/pypi/v/psy-reg.svg?style=flat
        :alt: PyPI Package latest release
        :target: https://pypi.python.org/pypi/psy-reg

    .. |conda| image:: https://anaconda.org/conda-forge/psy-reg/badges/version.svg
        :alt: conda
        :target: https://anaconda.org/conda-forge/psy-reg

    .. |supported-versions| image:: https://img.shields.io/pypi/pyversions/psy-reg.svg?style=flat
        :alt: Supported versions
        :target: https://pypi.python.org/pypi/psy-reg

    .. |supported-implementations| image:: https://img.shields.io/pypi/implementation/psy-reg.svg?style=flat
        :alt: Supported implementations
        :target: https://pypi.python.org/pypi/psy-reg

    .. |zenodo| image:: https://zenodo.org/badge/83479056.svg
        :alt: Zenodo
        :target: https://zenodo.org/badge/latestdoi/83479056

    .. |github| image:: https://img.shields.io/github/release/psyplot/psy-reg.svg
        :target: https://github.com/psyplot/psy-reg/releases/latest
        :alt: Latest github release

.. end-badges


Documentation
-------------

.. toctree::
    :maxdepth: 1

    installing
    plot_methods
    contribute
    api/psy_reg



Copyright
---------
Copyright © 2021 Helmholtz-Zentrum Hereon, 2020-2021 Helmholtz-Zentrum
Geesthacht, 2016-2021 University of Lausanne

psy-reg is released under the GNU LGPL-3.O license.
See COPYING and COPYING.LESSER in the root of the repository for full
licensing details.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License version 3.0 as
published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU LGPL-3.0 license for more details.

You should have received a copy of the GNU LGPL-3.0 license
along with this program.  If not, see https://www.gnu.org/licenses/.



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
