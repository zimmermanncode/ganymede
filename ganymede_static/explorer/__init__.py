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
Setup proxy to ``ganymede-declarativewidgets_explorer``.

``__path__`` gets extended with the above, and contained ``bower.json``
is used by ``.urth_components`` to extend its ``BOWER_DEPENDENCIES``
"""

from ganymede_widgets import DECLARATIVEWIDGETS_EXPLORER_REPO


__path__.append(DECLARATIVEWIDGETS_EXPLORER_REPO)
