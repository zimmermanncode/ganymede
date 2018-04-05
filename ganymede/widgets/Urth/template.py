"""
Pythonic API for Urth templates.
"""

from .channel import Channel
from .component import Component
from .container import Container
from .element import Element


class Template(Element):

    def __init__(self, content, channel=None):
        html_attrs = {
            'is': 'urth-core-bind',
        }
        if channel is not None:
            if isinstance(channel, Channel):
                channel_name = channel.name
            else:
                channel_name = channel
                channel = Channel(channel_name)
            html_attrs['channel'] = channel_name
        self.channel = channel
        super().__init__('template', children=content, **html_attrs)

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
        return "{}\n{}".format(
            "\n".join(imp.to_html() for imp in self.urth_imports()),
            super().to_html())
