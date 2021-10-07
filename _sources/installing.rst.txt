.. _install:

.. highlight:: bash

Installation
============

How to install
--------------

Installation using conda
^^^^^^^^^^^^^^^^^^^^^^^^
We highly recommend to use conda_ for installing psy-reg. After downloading
the `miniconda installer`_, you can install psy-reg simply via::

    $ conda install -c conda-forge psy-reg

.. _miniconda installer: https://conda.io/en/latest/miniconda.html
.. _conda: https://docs.conda.io/en/latest/

Installation using pip
^^^^^^^^^^^^^^^^^^^^^^
If you do not want to use conda for managing your python packages, you can also
use the python package manager ``pip`` and install via::

    $ pip install psy-reg

Note however, that you have to install scipy_ and statsmodels_ beforehand.


Dependencies
------------
Besides the psyplot_ package, psy-reg uses the regression utilities from

- statsmodels_: a python package for different statistical models
- scipy_: The Python-based ecosystem of open-source software for mathematics,
  science, and engineering

.. _psyplot: https://psyplot.github.io/psyplot/
.. _statsmodels: https://www.statsmodels.org/stable/index.html
.. _scipy: https://www.scipy.org/


Running the tests
-----------------
First, clone out the github_ repository. And install psyplot_, statsmodels_ and
scipy_.

After that, you can run::

    $ python setup.py test

or after having install pytest_::

    $ py.test


.. _pytest: https://pytest.org/en/latest/contents.html
.. _github: https://github.com/psyplot/psy-reg
