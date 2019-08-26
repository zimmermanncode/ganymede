from path import Path
from IPython.display import HTML

import ganymede
import ganymede_static


def test_ganymede():
    """Test internal functionality of the ganymede python package.
    """
    COFFEE, JS = [
      Path(ganymede_static.__file__).realpath().dirname() / 'ganymede' + ext
      for ext in ['.coffee', '.js']]
    if COFFEE.exists():
        # make sure that no javascript exists
        # to check auto-generation from coffeescript
        JS.remove_p()
        assert not JS.exists()

    html = ganymede.load() # triggers coffeescript-->javascript compilation
    assert JS.exists()
    assert isinstance(html, HTML)
