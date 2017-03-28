.. _install:

.. highlight:: bash

Installation
============

How to install
--------------

Installation using conda
^^^^^^^^^^^^^^^^^^^^^^^^
We highly recommend to use conda_ for installing psy-reg.

After downloading the installer from anaconda_, you can install psy-reg simply
via::

    $ conda install -c chilipp psy-reg

.. _anaconda: https://www.continuum.io/downloads
.. _conda-forge: http://conda-forge.github.io/
.. _conda: http://conda.io/

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

.. _psyplot: http://psyplot.readthedocs.io/en/latest/
.. _statsmodels: http://www.statsmodels.org/stable/index.html
.. _scipy: https://www.scipy.org/


Running the tests
-----------------
First, clone out the github_ repository. And install psyplot_, statsmodels_ and
scipy_.

After that, you can run::

    $ python setup.py test

or after having install pytest_::

    $ py.test


.. _pytest: https://pytest.org/latest/contents.html
.. _github: https://github.com/Chilipp/psy-reg
