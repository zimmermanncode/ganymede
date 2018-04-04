"""
WebComponents in Jupyter's atmosphere.
"""

import sys

from path import Path

import ganymede


DECLARATIVEWIDGETS_REPO = (
    Path(ganymede.__file__).realpath().dirname().dirname() /
    'ganymede-declarativewidgets')

if DECLARATIVEWIDGETS_REPO.exists():
    sys.path.insert(0, DECLARATIVEWIDGETS_REPO / 'kernel-python')


DECLARATIVEWIDGETS_EXPLORER_REPO = (
    DECLARATIVEWIDGETS_REPO.dirname() /
    'ganymede-declarativewidgets_explorer')


def init_declarativewidgets():
    """
    Initialize the bundled declarativewidgets extension.

    Run _bower_ to resolve all dependencies of the _urth_ components and call
    ``declarativewidgets.init()``
    """
    import nodely.bin

    import declarativewidgets

    from .ext.urth_import import get_nbextension_path

    ext_path = get_nbextension_path()

    if ext_path is not None:
        with Path(ext_path):
            nodely.bin['bower'](['install'])

    declarativewidgets.init()
