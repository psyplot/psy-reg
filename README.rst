========================================================================
psy-reg: Psyplot plugin for visualizing and calculating regression plots
========================================================================

.. start-badges

.. list-table::
    :stub-columns: 1
    :widths: 10 90

    * - docs
      - |docs|
    * - tests
      - |travis| |appveyor| |requires| |coveralls|
    * - package
      - |version| |conda| |supported-versions| |supported-implementations| |zenodo|

.. |docs| image:: http://readthedocs.org/projects/psy-reg/badge/?version=latest
    :alt: Documentation Status
    :target: http://psy-reg.readthedocs.io/en/latest/?badge=latest

.. |travis| image:: https://travis-ci.org/Chilipp/psy-reg.svg?branch=master
    :alt: Travis
    :target: https://travis-ci.org/Chilipp/psy-reg

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/3jk6ea1n4a4dl6vk?svg=true
    :alt: AppVeyor
    :target: https://ci.appveyor.com/project/Chilipp/psy-reg

.. |coveralls| image:: https://coveralls.io/repos/github/Chilipp/psy-reg/badge.svg?branch=master
    :alt: Coverage
    :target: https://coveralls.io/github/Chilipp/psy-reg?branch=master

.. |requires| image:: https://requires.io/github/Chilipp/psy-reg/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/Chilipp/psy-reg/requirements/?branch=master

.. |version| image:: https://img.shields.io/pypi/v/psy-reg.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/psy-reg

.. |conda| image:: https://anaconda.org/conda-forge/psy-reg/badges/version.svg
    :alt: conda
    :target: https://conda.anaconda.org/conda-forge/psy-reg

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/psy-reg.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/psy-reg

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/psy-reg.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/psy-reg

.. |zenodo| image:: https://zenodo.org/badge/83479056.svg
    :alt: Zenodo
    :target: https://zenodo.org/badge/latestdoi/83479056


.. end-badges

Welcome to the psyplot plugin for visualizating and calculating regression
plots. This package uses the scipy_ and statsmodels_ packages to evaluate your
data, fit a regression to it and visualize it through the psy-simple_ plugin.

It's plot methods are the linreg_ and densityreg_ plot methods.

See the full documentation on
`readthedocs.org <http://psyplot.readthedocs.io/projects/psy-simple>`__ for all
`plot methods`_ and examples_.

.. _psy-simple: http://psyplot.readthedocs.io/projects/psy-simple/
.. _statsmodels: http://www.statsmodels.org/stable/index.html
.. _scipy: https://www.scipy.org/
.. _linreg: http://psyplot.readthedocs.io/projects/psy-reg/en/latest/generated/psyplot.project.plot.linreg.html#psyplot.project.plot.linreg
.. _densityreg: http://psyplot.readthedocs.io/projects/psy-reg/en/latest/generated/psyplot.project.plot.densityreg.html#psyplot.project.plot.densityreg
.. _plot methods: http://psyplot.readthedocs.io/projects/psy-simple/en/latest/plot_methods
.. _examples: http://psyplot.readthedocs.io/projects/psy-simple/en/latest/examples
