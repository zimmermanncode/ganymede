import sys
import os

from setuptools import setup


ROOT = os.path.dirname(os.path.realpath(__file__))

sys.path.insert(0, ROOT)

import ganymede
if os.path.exists(os.path.join(
  ROOT, 'ganymede', 'static', 'ganymede.coffee'
  )):
    # trigger ganymede.coffee-->.js compilation
    import ganymede.static


setup(
    name='ganymede',
    description="Hacking Jupyter's atmosphere",
    long_description=open(os.path.join(ROOT, 'README.rst')).read(),

    author="Stefan Zimmermann",
    author_email="user@zimmermann.co",
    url="https://github.com/zimmermanncode/ganymede",

    license='GPLv3',

    setup_requires=open(os.path.join(ROOT, 'requirements.setup.txt')).read(),
    install_requires=open(os.path.join(ROOT, 'requirements.txt')).read(),

    use_scm_version={'write_to': 'ganymede/__version__.py'},

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
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: JavaScript',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
    keywords=[
        'ganymede', 'jupyter', 'ipython', 'notebook',
    ],
)
