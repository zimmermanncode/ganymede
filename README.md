
# ![](https://bitbucket.org/userzimmermann/ganymede/raw/default/ganymede/static/ganymede.svg) Ganymede | Hacking Jupyter's atmosphere

[![](http://www.gnu.org/graphics/gplv3-88x31.png)](
  https://gnu.org/licenses/lgpl.html)
[![](https://img.shields.io/pypi/pyversions/ganymede.svg)](
  https://python.org)
[![](https://img.shields.io/pypi/v/ganymede.svg)](
  https://pypi.python.org/pypi/ganymede)
[![](https://img.shields.io/pypi/dd/ganymede.svg)](
  https://pypi.python.org/pypi/ganymede)

[![](https://travis-ci.org/zimmermanncode/ganymede.svg)](
  https://travis-ci.org/zimmermanncode/ganymede)
[![](https://ci.appveyor.com/api/projects/status/49sp18ovmcpp9tmg?svg=true)](
  https://ci.appveyor.com/project/userzimmermann/ganymede)

> https://www.openhub.net/p/jupyter-ganymede

> Includes [jQuery UI Touch Punch](http://touchpunch.furf.com)

**Git** repository:

* https://github.com/zimmermanncode/ganymede
* https://gitlab.com/zimmermanncode/ganymede

**Hg** repository: https://bitbucket.org/zimmermanncode/ganymede

Have you also wondered where the fourth Galilean moon in [Jupyter](http://jupyter.org)'s logo has gone? Well, it is told that after many centuries of Ganymede's absence from Mount Olympus, Zeus felt a deep and painful longing. So he sent out his eagle again to find Ganymede and bring him back. But Ganymede always wanted to be more than just a servant for the pleasure of the gods. He turned to Jupyter with an offer. If Jupyter grant him shelter in his giant atmosphere then Ganymede would build him a new temple. A temple to attract a whole new generation of worshippers. Jupyter accepted...

Currently, the temple can only be visited from Python. There will soon be other ways to get there. Just use [pip](http://pip-installer.org) to automatically install the latest [gate](https://pypi.python.org/pypi/ganymede) with its dependencies from [PyPI](https://pypi.python.org):

    pip install ganymede

It can also be visited in development mode, directly from Ganymede's repository. The additional development dependencies are automatically resolved by running the following commands in the repository's root directory:

    pip install -r requirements.txt
    pip install -r requirements.dev.txt
    pip install -e .

You also need an installed [CoffeeScript](http://coffeescript.org) compiler for development mode.

Then open an IPython notebook in Jupyter's web interface and:


![](https://bitbucket.org/userzimmermann/ganymede/raw/default/screenshot.png)

Some of Jupyter's control elements are hidden, like the cell format and cell toolbar select boxes. They still need to find their new place, along with these additional features coming soon:

* Menu button in slim mode tool bar
* Redocking of cell outputs to the console
* Visual indicators for cell inputs on hovering their undocked outputs and vice versa and auto console scrolling to input
* Switchable virtual background screens for undocked outputs with selection bar in menu area
* A %terminal magic to embed Jupyter's remote terminals in notebooks
* Tabbed multi-notebook console and ability to mix undocked cell outputs from different notebooks and kernels

