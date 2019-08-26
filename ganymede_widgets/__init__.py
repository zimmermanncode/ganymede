"""
WebComponents in Jupyter's atmosphere.
"""

import sys

from path import Path


DECLARATIVEWIDGETS_REPO = (
    Path(__file__).realpath().dirname().dirname() /
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
    import declarativewidgets

    declarativewidgets.init()
