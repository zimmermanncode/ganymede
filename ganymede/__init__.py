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

__version__ = '0.2.0.post1'


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
    from ganymede.static import CSS, JS, TOUCH_PUNCH_JS, SVG

    if logo_src is None:
        # load Ganymede's default logo
        logo_src = 'data:image/svg+xml;base64,%s' \
            % b64encode(SVG.bytes()).decode('ascii')

    # import locally to make this module importable in setup.py
    # without further dependencies
    from IPython.display import HTML

    return HTML(u"""
        <style id="ganymede-style" type="text/css">
            {style}
        </style>
        <script type="text/javascript">
            {touch_punch}
        </script>
        <script type="text/javascript">
            {script}
            window.ganymede = new Ganymede({logo_src});
        </script>
        <script type="text/javascript">
            $('#ganymede-style').on('remove', function () {{
                window.ganymede.unload();
            }});
        </script>
    """.format(style=CSS.text('ascii'), script=JS.text('ascii'),
               logo_src=json.dumps(logo_src),
               touch_punch=TOUCH_PUNCH_JS.text('utf8')))


def load_ipython_extension(shell):
    """
    Called from IPython on ``%load_ext ganymede`` and ``%reload_ext ganymede``

    Calls :func:`ganymede.load` which does the actual magic.
    """
    # import locally to make this module importable in setup.py
    # without further dependencies
    from IPython.display import display

    display(load(shell))
