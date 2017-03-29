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

See the :ref:`plot_methods` and :ref:`gallery_examples` for more information.

.. _psy-simple: http://psyplot.readthedocs.io/projects/psy-simple/
.. _statsmodels: http://www.statsmodels.org/stable/index.html
.. _scipy: https://www.scipy.org/

.. start-badges

.. list-table::
    :stub-columns: 1
    :widths: 10 90

    * - docs
      - |docs|
    * - tests
      - |travis| |appveyor| |requires| |coveralls|
    * - package
      - |version| |conda| |supported-versions| |supported-implementations|

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

.. |conda| image:: https://anaconda.org/chilipp/psy-reg/badges/installer/conda.svg
    :alt: conda
    :target: https://conda.anaconda.org/chilipp

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/psy-reg.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/psy-reg

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/psy-reg.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/psy-reg


.. end-badges


Documentation
-------------

.. toctree::
    :maxdepth: 1

    installing
    plot_methods
    examples/index
    api/psy_reg



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
