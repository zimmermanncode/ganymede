"""
WebComponents in Jupyter's atmosphere.
"""

import sys

from path import Path

import ganymede


DECLARATIVEWIDGETS_REPO = (
    Path(ganymede.__file__).realpath().dirname().dirname() /
    'jupyter-declarativewidgets')

if DECLARATIVEWIDGETS_REPO.exists():
    sys.path.insert(0, DECLARATIVEWIDGETS_REPO / 'kernel-python')


DECLARATIVEWIDGETS_EXPLORER_REPO = (
    DECLARATIVEWIDGETS_REPO.dirname() /
    'jupyter-declarativewidgets_explorer')


import declarativewidgets


declarativewidgets.init()
