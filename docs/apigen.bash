#!/bin/bash
# script to automatically generate the psyplot api documentation using
# sphinx-apidoc and sed
sphinx-apidoc -f -M -e  -T -o api ../psy_reg/
# replace chapter title in psy_maps.rst
sed -i -e 1,1s/.*/'API Reference'/ api/psy_reg.rst

sphinx-autogen -o generated *.rst
