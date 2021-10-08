v1.4.0
======
Compatibility fixes and LGPL license

As with psyplot 1.4.0, psy-reg is now continuously tested and deployed with
CircleCI.


Fixed
-----
- psy-reg is now officially licensed under LGPL-3.0-only,
  see `#9 <https://github.com/psyplot/psy-reg/pull/9>`__


Added
-----
- psy-reg does now have a CITATION.cff file, see https://citation-file-format.github.io


Changed
-------
- Documentation is now hosted with Github Pages at https://psyplot.github.io/psy-reg.
  Redirects from the old documentation at `https://psy-reg.readthedocs.io` have been
  configured.
- Examples have been removed from the psy-reg repository as they now live in a
  central place at https://github.com/psyplot/examples
- We use CicleCI now for a standardized CI/CD pipeline to build and test
  the code and docs all at one place, see `#8 <https://github.com/psyplot/psy-reg/pull/8>`__