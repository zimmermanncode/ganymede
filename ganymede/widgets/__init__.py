"""
WebComponents in Jupyter's atmosphere.
"""

import sys

import nodely.bin
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

from .ext.urth_import import get_nbextension_path


#: The installed nbextentensions/declarativewidgets directory path
DECLARATIVEWIDGETS_NBEXTENSION_PATH = Path(get_nbextension_path())

if DECLARATIVEWIDGETS_NBEXTENSION_PATH:
    # ensure that all urth component dependencies are correctly installed
    with (DECLARATIVEWIDGETS_NBEXTENSION_PATH):
        nodely.bin['bower'](['install'])


declarativewidgets.init()
