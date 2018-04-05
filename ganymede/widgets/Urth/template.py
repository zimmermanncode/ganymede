"""
Pythonic API for Urth templates.
"""

from .element import Element
from .channel import Channel


class Template(Element):

    def __init__(self, channel=None):
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
        super().__init__('template', html_attrs)
