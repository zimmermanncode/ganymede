"""Pythonic API for WebComponents."""

from .element import Element

__all__ = ('Element', 'Import')


class Component(Element):

    def __init__(
            self, tag, html_class=None,
            package_owner=None, version_spec=None,
            **html_attrs):
        super(Component, self).__init__(
            tag, html_class=html_class, **html_attrs)
        self.package_owner = package_owner
        self.version_spec = version_spec

    def __eq__(self, other):
        return (
            super(Component, self).__eq__(other) and
            self.package_owner == other.package_owner and
            self.version_spec == other.version_spec)

    @property
    def urth_import(self):
        return Import(
            self._element.tag, package_owner=self.package_owner,
            version_spec=self.version_spec)

    @property
    def bower_endpoint(self):
        return self.urth_import.bower_endpoint

    def to_html(self):
        return "{}\n\n{}".format(
            self.urth_import.to_html(), super(Component, self).to_html())


class Import(Element):

    def __init__(self, tag, package_owner=None, version_spec=None):
        package = tag
        if package_owner is not None:
            package = '/'.join((package_owner, package))
        if version_spec is not None:
            package = '#'.join((package, version_spec))
        super(Import, self).__init__('link', **{
            'rel': 'import',
            'is': 'urth-core-import',
            'package': package,
            'href': 'urth_components/{name}/{name}.html'.format(name=tag),
        })

    @property
    def bower_endpoint(self):
        return self._element.get('package')
