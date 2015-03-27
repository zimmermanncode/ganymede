# ganymede
#
# Hacking Jupyter's atmosphere
#
# Copyright (C) 2015 Stefan Zimmermann <zimmermann.code@gmail.com>
#
# ganymede is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ganymede is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with ganymede. If not, see <http://www.gnu.org/licenses/>.

import sys
from base64 import b64encode
import json

from IPython.display import display, HTML


def load():
    # make sure that .static pkg gets reloaded on %reload_ext ganymede
    # to recompile ganymede.coffee in development (non-installed) mode
    sys.modules.pop('ganymede.static', None)
    from ganymede.static import CSS, JS, SVG

    return HTML("""
      <style type="text/css">%s</style>
      <script type="text/javascript">
        %s
        window.ganymede = new Ganymede(%s);
      </script>
      """ % (CSS.text(), JS.text(),
             json.dumps('data:image/svg+xml;base64,%s'
                        % b64encode(SVG.bytes()).decode('ascii'))))


def load_ipython_extension(shell):
    display(load())
