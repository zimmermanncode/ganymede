from fnmatch import fnmatch
# from glob import glob
import os
import sys

from setuptools import find_packages


ROOT = os.path.dirname(os.path.realpath(__file__))

sys.path.insert(0, ROOT)

if os.path.exists(os.path.join(
        ROOT, 'ganymede', 'static', 'ganymede.coffee'
)):
    # # ==> trigger ganymede.coffee-->.js compilation
    # # (which needs version)
    # from setuptools_scm import get_version
    # get_version(local_scheme=lambda _: '',
    #             write_to='ganymede/__version__.py')

    import ganymede.static


DECLARATIVEWIDGETS_ROOT = os.path.join(ROOT, 'ganymede-declarativewidgets')

if os.path.exists(DECLARATIVEWIDGETS_ROOT):
    # ==> trigger bower.json creation
    import ganymede.static.urth


DECLARATIVEWIDGETS_EXPLORER_ROOT = os.path.join(
    ROOT, 'ganymede-declarativewidgets_explorer')


PACKAGES = [
    'ganymede',
    'ganymede.static',
    'ganymede.widgets',
]


DECLARATIVEWIDGETS_PACKAGE_ROOT = os.path.join(
    DECLARATIVEWIDGETS_ROOT, 'kernel-python')

PACKAGES.extend(find_packages(DECLARATIVEWIDGETS_PACKAGE_ROOT))

PACKAGE_DIRS = {
    pkg: os.path.relpath(
        os.path.join(DECLARATIVEWIDGETS_PACKAGE_ROOT, pkg),
        ROOT)
    for pkg in ['declarativewidgets', 'urth']}


PACKAGES.append('ganymede.widgets.ext')

PACKAGE_DIRS['ganymede.widgets.ext'] = os.path.relpath(
    os.path.join(
        DECLARATIVEWIDGETS_ROOT, 'nb-extension', 'python',
        'urth', 'widgets', 'ext'),
    ROOT)


STATIC_URTH = {
    'ganymede.static.' + subpkg: os.path.relpath(
        os.path.join(DECLARATIVEWIDGETS_ROOT, dirname),
        ROOT)
    for subpkg, dirname in [
        ('urth',  'nb-extension'),
        ('urth_components', 'elements'),
    ]}
STATIC_URTH['ganymede.static.explorer'] = DECLARATIVEWIDGETS_EXPLORER_ROOT

PACKAGES.extend(STATIC_URTH)

PACKAGE_DIRS.update(STATIC_URTH)


def find_package_data(pkgdir, *patterns):
    """
    Recursively find files matching any of given `patterns` under `pkgdir`.

    :return:
        A list of all matching data file paths relative to given package dir
    """
    return [
        # os.path.relpath(path, pkgdir) for pattern in patterns
        os.path.relpath(os.path.join(dirname, f), pkgdir)
        for dirname, _, filenames in os.walk(pkgdir)
        for f in filenames if any(fnmatch(f, p) for p in patterns)]
        # for path in glob(os.path.join(pkgdir, '**', pattern),
        #                  recursive=True)]


PACKAGE_DATA = {
    pkg: find_package_data(
        PACKAGE_DIRS.get(pkg, pkg.replace('.', os.path.sep)),
        '.*rc', '*.css', '*.html', '*.js', '*.json', '*.png', '*.svg')
    for pkg in ['ganymede.static'] + list(STATIC_URTH)}


def setup_package_keywords(dist):
    for data in (dist, dist.metadata):
        data.packages = PACKAGES
        data.package_dir = PACKAGE_DIRS
        data.package_data = PACKAGE_DATA
