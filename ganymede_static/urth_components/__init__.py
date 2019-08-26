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
Setup proxy to ``ganymede-declarativewidgets/elements``.

``__path__`` gets extended with the above, and ``BOWER_DEPENDENCIES`` get
collected from all contained ``urth-*`` components
"""

import json

from path import Path

from ganymede.widgets import DECLARATIVEWIDGETS_REPO
from ganymede_static import explorer


__path__.append(DECLARATIVEWIDGETS_REPO / 'elements')


BOWER_DEPENDENCIES = dict({
    dep for urth_path in list(__path__[-1].dirs()) + [explorer.__path__[-1]]
    for dep in (json.loads((urth_path / 'bower.json').text())
                .get('dependencies', {}).items())})

# restrict polymer to <1.6 for urth-core-bind compatibility
BOWER_DEPENDENCIES['polymer'] += " <1.6"
