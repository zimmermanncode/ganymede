# ganymede
#
# Hacking Jupyter's atmosphere
#
# Copyright (C) 2017 Stefan Zimmermann <user@zimmermann.co>
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

"""
Setup proxy to ``ganymede-declarativewidgets/nb-extension``.

``__path__`` gets extended with the above, and a ``bower.json`` is written
there, which contains all dependencies from all ``urth-*`` components
"""

import json

from path import Path

from ganymede.widgets import DECLARATIVEWIDGETS_REPO
# from ganymede_static.urth_components import BOWER_DEPENDENCIES


__path__.append(DECLARATIVEWIDGETS_REPO / 'nb-extension')


# urth_components/ formerly handled below have moved to server-only
# jupyter_path('ganymede', 'declarativewidgets')
# and initialization now happens in ganymede.load_jupyter_server_extension()


# _BOWERRC = __path__[-1] / '.bowerrc'

# _BOWERRC.write_text(json.dumps({
#     'analytics': False,
#     'interactive': False,
#     'directory': 'urth_components',
# }, indent=2))


# BOWER_JSON = __path__[-1] / 'bower.json'

# BOWER_JSON.write_text(json.dumps({
#     'name': 'jupyer-declarativewidgets',
#     'dependencies': BOWER_DEPENDENCIES,
# }, indent=2))
