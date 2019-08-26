# ganymede
#
# Hacking Jupyter's atmosphere
#
# Copyright (C) 2015 Stefan Zimmermann <zimmermann.code@gmail.com>
#
# ganymede is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ganymede is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ganymede. If not, see <http://www.gnu.org/licenses/>.

import sys
from base64 import b64encode
import json

from path import Path

from .__version__ import version as __version__


def load(shell=None, logo_src=None):
    """
    Generate and return Ganymede HTML containing CSS and JavaScript
    for modifying the Jupyter notebook web interface,
    wrapped in a ``IPython.display.HTML`` object:

    * Must be called with IPython `shell` instance as first argument.
    * Optionally takes a custom `logo_src` value for the ``src=`` attribute
      of Ganymede's HTML logo ``<img>`` element.
    """
    # make sure that .static pkg gets reloaded on %reload_ext ganymede
    # to recompile ganymede.coffee in development (non-installed) mode
    sys.modules.pop('ganymede.static', None)
    from ganymede.static import TOUCH_PUNCH_JS

    # import locally to make this module importable in setup.py
    # without further dependencies
    from IPython.display import HTML

    return HTML(u"""
    <script type="text/javascript">
        {touch_punch}
    </script>
    <script type="text/javascript">
        if (Ganymede.temple != null) {{
            Ganymede.temple.unload();
        }}
        Ganymede.temple = new Ganymede({logo_src});
    </script>
    """.format(
        logo_src=(json.dumps(logo_src) if logo_src is not None else ""),
        touch_punch=TOUCH_PUNCH_JS.text('utf-8')))


def load_ipython_extension(shell):
    """
    Called from IPython on ``%load_ext ganymede`` and ``%reload_ext ganymede``

    Calls :func:`ganymede.load` which does the actual magic.
    """
    # import locally to make this module importable in setup.py
    # without further dependencies
    from IPython.display import display

    import ganymede.widgets

    ganymede.widgets.init_declarativewidgets()

    display(load(shell))


def load_jupyter_server_extension(app):
    from jupyter_core.paths import jupyter_path

    for path in map(Path, jupyter_path('ganymede', 'declarativewidgets')):
        if path.normpath().normcase().startswith(
                Path(sys.prefix).normpath().normcase()):
            break
    else:
        raise RuntimeError("no jupyter_path() under sys.prefix found")

    (path / 'urth_components').makedirs_p()

    from ganymede.static.urth_components import BOWER_DEPENDENCIES

    (path / '.bowerrc').write_text(json.dumps({
        'analytics': False,
        'interactive': False,
        'directory': 'urth_components',
    }, indent=2))

    (path / 'bower.json').write_text(json.dumps({
        'name': 'jupyer-declarativewidgets',
        'dependencies': BOWER_DEPENDENCIES,
    }, indent=2))

    import nodely.bin

    with path:
        nodely.bin['bower']('--allow-root', 'install')

    from ganymede.widgets.ext import urth_import

    urth_import.load_jupyter_server_extension(app)


def _jupyter_nbextension_paths():
    from ganymede.static import urth, urth_components, explorer

    return [
        {
            'section': 'notebook',
            'src': 'static',
            'dest': 'ganymede',
            'require': 'ganymede/ganymede',
        },
        {
            'section': 'notebook',
            'src': list(urth.__path__)[-1],
            'dest': 'declarativewidgets',
            'require': 'declarativewidgets/js/main',
        },
        {
            'section': 'notebook',
            'src': list(urth_components.__path__)[-1],
            'dest': 'declarativewidgets/urth_components',
            'require': 'declarativewidgets/js/main',
        },
        {
            'section': 'notebook',
            'src': list(explorer.__path__)[-1],
            'dest': (
                'declarativewidgets/urth_components/'
                'declarativewidgets-explorer'
            ),
            'require': 'declarativewidgets/js/main',
        },
    ]


def _jupyter_server_extension_paths():
    return [{'module': 'ganymede'}]
