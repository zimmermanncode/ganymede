"""Pythonic API for Urth templates."""

from .channel import ChannelBindable
from .component import Component
from .container import Container
from .element import Element


class Template(Element, ChannelBindable):

    def __init__(self, channel=None, children=None):
        html_attrs = {
            'is': 'urth-core-bind',
        }
        ChannelBindable.__init__(self, channel)
        if self.channel is not None:
            html_attrs['channel'] = self.channel.name
        super().__init__('template', children=children, **html_attrs)

    def urth_imports(self):
        links = set()
        for element in self.children:
            if isinstance(element, Container):
                links.update(element.urth_imports())
            if isinstance(element, Component):
                links.add(element.urth_import)
        return links

    def bower_endpoints(self):
        return {imp.bower_endpoint for imp in self.urth_imports()}

    def to_html(self):
        return "{}\n\n{}".format(
            "\n".join(imp.to_html() for imp in self.urth_imports()),
            super().to_html())
