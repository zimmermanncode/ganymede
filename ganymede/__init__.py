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

__version__ = '0.1.dev'


def load():
    """Generate and return Ganymede HTML containing CSS and JavaScript
       for modifying the Jupyter notebook web interface.
    """
    # make sure that .static pkg gets reloaded on %reload_ext ganymede
    # to recompile ganymede.coffee in development (non-installed) mode
    sys.modules.pop('ganymede.static', None)
    from ganymede.static import CSS, JS, SVG

    # import locally to make this module importable in setup.py
    # without further dependencies
    from IPython.display import HTML

    return HTML("""
      <style id="ganymede-style" type="text/css">%s</style>
      <script type="text/javascript">
        %s
        window.ganymede = new Ganymede(%s);
      </script>
      <script type="text/javascript">
        $('#ganymede-style').on('remove', function () {
            window.ganymede.unload();
        });
      </script>
      """ % (CSS.text(), JS.text(),
             json.dumps('data:image/svg+xml;base64,%s'
                        % b64encode(SVG.bytes()).decode('ascii'))))


def load_ipython_extension(shell):
    """Called on ``%load_ext ganymede`` and ``%reload_ext ganymede``
    """
    # import locally to make this module importable in setup.py
    # without further dependencies
    from IPython.display import display

    display(load())
