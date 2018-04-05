"""
Pythonic API for Urth channels.
"""

import declarativewidgets

from .element import Element


class Meta(type(Element)):
    pass


class Channel(Element, metaclass=Meta):

    def __init__(self, name, **html_attrs):
        html_attrs.setdefault('name', name)
        super().__init__('urth-core-channel', html_attrs)
        self._channel = declarativewidgets.channel(name)

    @property
    def name(self):
        return self._channel.chan

    def changed(self, key, _func=None):
        def deco(func):
            self._channel.watch(key, func)
            return func

        if _func is not None:
            return deco(_func)

        return deco

    def __setitem__(self, key, value):
        self._channel.set(key, value)

    def to_html(self):
        return str(self)


Meta.default = Channel('default')
