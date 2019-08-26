"""Setup for Python ``ganymede`` package distribution."""

from __future__ import print_function

from setuptools import setup


dist = None
try:
    dist = setup(
        # long_description=open(os.path.join(ROOT, 'README.rst')).read(),

        setup_requires=open("requirements.setup.txt").read(),

        use_zetup = True,

        require_node_modules=['bower'],
    )

finally:
    if dist is not None and hasattr(dist, 'zetup_made'):
        dist.zetup_made.clean()
