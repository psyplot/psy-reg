.. SPDX-FileCopyrightText: 2021-2024 Helmholtz-Zentrum hereon GmbH
..
.. SPDX-License-Identifier: CC-BY-4.0

.. psy-reg documentation master file
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to psy-reg's documentation!
===================================

|CI|
|Code coverage|
|Latest Release|
|PyPI version|
|Code style: black|
|Imports: isort|
|PEP8|
|Checked with mypy|
|REUSE status|

.. rubric:: Psyplot plugin for visualizing and calculating regression plots

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



.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   plot_methods
   api
   contributing


How to cite this software
-------------------------

.. card:: Please do cite this software!

   .. tab-set::

      .. tab-item:: APA

         .. citation-info::
            :format: apalike

      .. tab-item:: BibTex

         .. citation-info::
            :format: bibtex

      .. tab-item:: RIS

         .. citation-info::
            :format: ris

      .. tab-item:: Endnote

         .. citation-info::
            :format: endnote

      .. tab-item:: CFF

         .. citation-info::
            :format: cff


License information
-------------------
Copyright © 2021-2024 Helmholtz-Zentrum hereon GmbH

The source code of psy-reg is licensed under
LGPL-3.0-only.

If not stated otherwise, the contents of this documentation is licensed under
CC-BY-4.0.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. |CI| image:: https://codebase.helmholtz.cloud/psyplot/psy-reg/badges/master/pipeline.svg
   :target: https://codebase.helmholtz.cloud/psyplot/psy-reg/-/pipelines?page=1&scope=all&ref=master
.. |Code coverage| image:: https://codebase.helmholtz.cloud/psyplot/psy-reg/badges/master/coverage.svg
   :target: https://codebase.helmholtz.cloud/psyplot/psy-reg/-/graphs/master/charts
.. |Latest Release| image:: https://codebase.helmholtz.cloud/psyplot/psy-reg/-/badges/release.svg
   :target: https://codebase.helmholtz.cloud/psyplot/psy-reg
.. |PyPI version| image:: https://img.shields.io/pypi/v/psy-reg.svg
   :target: https://pypi.python.org/pypi/psy-reg/
.. |Code style: black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
.. |Imports: isort| image:: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
   :target: https://pycqa.github.io/isort/
.. |PEP8| image:: https://img.shields.io/badge/code%20style-pep8-orange.svg
   :target: https://www.python.org/dev/peps/pep-0008/
.. |Checked with mypy| image:: http://www.mypy-lang.org/static/mypy_badge.svg
   :target: http://mypy-lang.org/
.. |REUSE status| image:: https://api.reuse.software/badge/codebase.helmholtz.cloud/psyplot/psy-reg
   :target: https://api.reuse.software/info/codebase.helmholtz.cloud/psyplot/psy-reg
