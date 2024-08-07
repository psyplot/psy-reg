.. SPDX-FileCopyrightText: 2021-2024 Helmholtz-Zentrum hereon GmbH
..
.. SPDX-License-Identifier: CC-BY-4.0

.. _plot_methods:

psyplot plot methods
====================

This plugin defines the following new plot methods for the
:class:`psyplot.project.ProjectPlotter` class. They can, for example, be
accessed through

.. ipython::

    In [1]: import psyplot.project as psy

    In [2]: psy.plot.linreg

.. autosummary::
    :toctree: generated

    ~psyplot.project.plot.linreg
    ~psyplot.project.plot.densityreg
