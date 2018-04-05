"""
Pythonic API for Urth channels.
"""

from moretools import isdict

import declarativewidgets

from .element import Element


class Meta(type(Element)):
    pass


class Channel(Element, metaclass=Meta):

    def __init__(self, name, items=None, **html_attrs):
        html_attrs.setdefault('name', name)
        children = []
        if items is not None:
            if isdict(items):
                items = items.items()
            for item in items:
                if not isinstance(item, Item):
                    key, value = item
                    item = Item(key, value)
                children.append(item)
        super().__init__('urth-core-channel', children=children,
                         **html_attrs)
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


class Item(Element):

    def __init__(self, key, value):
        super().__init__('urth-core-channel-item',
                         key=key, value=str(value))


Meta.Item = Item

Meta.default = Channel('default')
