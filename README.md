<!--
SPDX-FileCopyrightText: 2021-2024 Helmholtz-Zentrum hereon GmbH

SPDX-License-Identifier: CC-BY-4.0
-->

# psy-reg: Psyplot plugin for visualizing and calculating regression plots

[![CI](https://codebase.helmholtz.cloud/psyplot/psy-reg/badges/main/pipeline.svg)](https://codebase.helmholtz.cloud/psyplot/psy-reg/-/pipelines?page=1&scope=all&ref=main)
[![Code coverage](https://codebase.helmholtz.cloud/psyplot/psy-reg/badges/main/coverage.svg)](https://codebase.helmholtz.cloud/psyplot/psy-reg/-/graphs/main/charts)
[![Latest Release](https://codebase.helmholtz.cloud/psyplot/psy-reg/-/badges/release.svg)](https://codebase.helmholtz.cloud/psyplot/psy-reg)
<!-- TODO: uncomment the following line when the package is published at https://pypi.org -->
<!-- [![PyPI version](https://img.shields.io/pypi/v/psy-reg.svg)](https://pypi.python.org/pypi/psy-reg/) -->
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
<!-- TODO: uncomment the following line when the package is registered at https://api.reuse.software -->
<!-- [![REUSE status](https://api.reuse.software/badge/codebase.helmholtz.cloud/psyplot/psy-reg)](https://api.reuse.software/info/codebase.helmholtz.cloud/psyplot/psy-reg) -->


Welcome to the psyplot plugin for visualizating and calculating
regression plots. This package uses the [scipy](https://www.scipy.org/)
and [statsmodels](https://www.statsmodels.org/stable/index.html)
packages to evaluate your data, fit a regression to it and visualize it
through the [psy-simple](http://psyplot.github.io/psy-simple/) plugin.

It\'s plot methods are the
[linreg](http://psyplot.github.io/psy-reg/generated/psyplot.project.plot.linreg.html#psyplot.project.plot.linreg)
and
[densityreg](http://psyplot.github.io/psy-reg/generated/psyplot.project.plot.densityreg.html#psyplot.project.plot.densityreg)
plot methods.

See the full documentation on
[psyplot.github.io/psy-reg/](http://psyplot.github.io/psy-reg) for all
[plot methods](http://psyplot.github.io/psy-simple/plot_methods), and
checkout the [examples](http://psyplot.github.io/examples/).


## Installation

Install this package in a dedicated python environment via

```bash
python -m venv venv
source venv/bin/activate
pip install psy-reg
```

To use this in a development setup, clone the [source code][source code] from
gitlab, start the development server and make your changes::

```bash
git clone https://codebase.helmholtz.cloud/psyplot/psy-reg
cd psy-reg
python -m venv venv
source venv/bin/activate
make dev-install
```

More detailed installation instructions my be found in the [docs][docs].


[source code]: https://codebase.helmholtz.cloud/psyplot/psy-reg
[docs]: https://psyplot.github.io/psy-reginstallation.html

## Technical note

This package has been generated from the template
https://codebase.helmholtz.cloud/psyplot/psyplot-plugin-template.git.

See the template repository for instructions on how to update the skeleton for
this package.


## License information

Copyright © 2021-2024 Helmholtz-Zentrum hereon GmbH



Code files in this repository are licensed under the
LGPL-3.0-only, if not stated otherwise
in the file.

Documentation files in this repository are licensed under CC-BY-4.0, if not stated otherwise in the file.

Supplementary and configuration files in this repository are licensed
under CC0-1.0, if not stated otherwise
in the file.

Please check the header of the individual files for more detailed
information.



### License management

License management is handled with [``reuse``](https://reuse.readthedocs.io/).
If you have any questions on this, please have a look into the
[contributing guide][contributing] or contact the maintainers of
`psy-reg`.

[contributing]: https://psyplot.github.io/psy-regcontributing.html
