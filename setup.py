import sys
import os

from setuptools import setup

ROOT = os.path.dirname(os.path.realpath(__file__))

sys.path.insert(0, ROOT)


if os.path.exists(os.path.join(
  ROOT, 'ganymede', 'static', 'ganymede.coffee'
  )):
    # trigger ganymede.coffee-->.js compilation
    import ganymede.static


setup(
  name='ganymede',
  version=ganymede.__version__,
  description="Hacking Jupyter's atmosphere",

  author="Stefan Zimmermann",
  author_email="<zimmermann.code@gmail.com>",
  url="https://bitbucket.org/userzimmermann/ganymede",

  license='LGPLv3',

  install_requires=open(os.path.join(ROOT, 'requirements.txt')).read(),

  packages=[
    'ganymede',
    'ganymede.static',
    ],
  package_data={
    'ganymede.static': ['*.svg', '*.css', '*.js'],
    },

  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved'
    ' :: GNU Library or Lesser General Public License (LGPL)',
    'Operating System :: OS Independent',
    'Topic :: Software Development',
    'Topic :: Utilities',
    ],
  keywords=[
    'ganymede', 'jupyter', 'ipython', 'notebook',
    ],
  )
