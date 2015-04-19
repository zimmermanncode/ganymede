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

from path import Path


DIR = Path(__file__).dirname()

SVG = DIR / 'ganymede.svg'

CSS = DIR / 'ganymede.css'

COFFEE = DIR / 'ganymede.coffee'
JS = DIR / 'ganymede.js'

TOUCH_PUNCH_JS = DIR / 'jquery.ui.touch-punch.min.js'


if COFFEE.exists(): #==> development mode (not installed) ==> compile
    # import conditionally to avoid general dependency
    from coffeetools import coffee

    JS.write_text(coffee.compile(COFFEE.text(), bare=True))
