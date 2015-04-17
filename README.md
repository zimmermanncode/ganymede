

# ![](https://bitbucket.org/userzimmermann/ganymede/raw/default/ganymede/static/ganymede.svg) Ganymede



[![](https://travis-ci.org/userzimmermann/ganymede.svg)](https://travis-ci.org/userzimmermann/ganymede)



* https://bitbucket.org/userzimmermann/ganymede
* https://github.com/userzimmermann/ganymede
* https://www.openhub.net/p/jupyter-ganymede



## Hacking Jupyter's atmosphere



Have you also wondered where the fourth Galilean moon in [Jupyter](http://jupyter.org)'s logo has gone? Well, it is told that after many centuries of Ganymede's absence from Mount Olympus, Zeus felt a deep and painful longing. So he sent out his eagle again to find Ganymede and bring him back. But Ganymede always wanted to be more than just a servant for the pleasure of the gods. He turned to Jupyter with an offer. If Jupyter grant him shelter in his giant atmosphere then Ganymede would build him a new temple. A temple to attract a whole new generation of worshippers. Jupyter accepted...



Currently, the temple can only be visited from Python. There will soon be other ways to get there. Just use [pip](http://pip-installer.org) to automatically install the latest [gate](https://pypi.python.org/pypi/ganymede) with its dependencies from [PyPI](https://pypi.python.org):

    pip install ganymede



It can also be visited in development mode, directly from Ganymede's repository. The additional development dependencies are automatically resolved by running the following commands in the repository's root directory:

    pip install -r requirements.txt
    pip install -r requirements.dev.txt
    pip install -e .

You also need an installed [CoffeeScript](http://coffeescript.org) compiler for development mode.



Then open an IPython notebook in Jupyter's web interface and:



```python
%load_ext ganymede
```



You will see the header area with menu and tool bar disappear and the notebook area turn into a console with three handle bars at the bottom, the outer two for resizing and the inner one for combined vertical resizing and horizontal moving. A simple click on the latter toggles the console's visibility.



At the top left window corner you will see Ganymede's logo. Just grab and move it around. It will reveal the new tool and menu area. A simple click toggles slim mode, which only shows the tools.



You might wonder what's the essential advantage of these features. It will make more sense when you use the dynamic free background space to place some cell outputs there. Just grab an `Out[*]` prompt area and drag it around. This will undock the output from the console and you can drop it anywhere on the background. That won't change the cell's DOM hierarchy, so the output stays logically connected to the cell input and re-evaluating the cell will also update the undocked output.



You can go back to the default Jupyter interface any time by deleting the `%load_ext ganymede` cell or just its output. You can also `%reload_ext ganymede` at any time. Size, positions and state of the console, the menu area and the output cells are stored as notebook and cell metadata respectively.



Some of Jupyter's control elements are hidden, like the cell format and cell toolbar select boxes. They still need to find their new place, along with these additional features coming soon:

* Menu button in slim mode tool bar
* Redocking of cell outputs to the console
* Visual indicators for cell inputs on hovering their undocked outputs and vice versa and auto console scrolling to input
* Switchable virtual background screens for undocked outputs with selection bar in menu area
* A %terminal magic to embed Jupyter's remote terminals in notebooks
* Tabbed multi-notebook console and ability to mix undocked cell outputs from different notebooks and kernels


