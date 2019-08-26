"""Pythonic API for Urth channels."""

from collections import MutableMapping

import zetup
from moretools import isdict
from six import with_metaclass

import declarativewidgets

from .element import Element


CONTEXT_STACK = []


class ChannelBindable(zetup.object):

    def __init__(self, channel=None, key=None):
        if channel is None:
            if CONTEXT_STACK:
                channel = CONTEXT_STACK[-1]
        elif not isinstance(channel, Channel):
            channel = Channel(channel)
        self.channel = channel
        self.channel_key = key


class Meta(type(Element)):
    pass


class Channel(with_metaclass(Meta, Element, MutableMapping)):

    def __init__(self, name, items=None, **html_attrs):
        html_attrs.setdefault('name', name)
        children = []
        if items is None:
            self._items = {}
        else:
            self._items = dict(items)
        super(Channel, self).__init__(
            'urth-core-channel', children=children, **html_attrs)
        self._channel = declarativewidgets.channel(name)
        self._handlers = {}

    @property
    def name(self):
        return self._channel.chan

    def __enter__(self):
        CONTEXT_STACK.append(self)
        return self

    def __exit__(self, exc_type, exc, traceback):
        assert CONTEXT_STACK[-1] is self
        CONTEXT_STACK.pop(-1)
        if exc is not None:
            raise exc.with_traceback(traceback)

    def display(self):
        super(Channel, self).display()
        for key, value in self._items.items():
            self[key] = value

    def changed(self, key, _func=None):
        # TODO: generalize (duplicated in __setitem__)
        if key not in self._handlers:
            self._handlers[key] = []

            def watcher(old_value, new_value):
                self._items[key] = new_value
                for func in self._handlers[key]:
                    func(new_value, old_value)

            self._channel.watch(key, watcher)

        def deco(func):
            self._handlers[key].append(func)
            if key in self._items:
                func(self._items[key], None)
            return func

        if _func is not None:
            return deco(_func)

        return deco

    def __getitem__(self, key):
        value = self._items[key]
        self._channel.set(key, value)
        return value

    def __setitem__(self, key, value):
        if key not in self._handlers:
            self._handlers[key] = []

            def watcher(old_value, new_value):
                self._items[key] = new_value
                for func in self._handlers[key]:
                    func(new_value, old_value)

            self._channel.watch(key, watcher)
        self._channel.set(key, value)
        self._items[key] = value

    def __delitem__(self, key):
        raise NotImplementedError(
            "Cannot delete items of a {}".format(type(self)))

    def __iter__(self):
        return iter(self._items.items())

    def __len__(self):
        return len(self._items)


class Item(Element):

    def __init__(self, key, value):
        super(Item, self).__init__(
            'urth-core-channel-item', key=key, value=str(value))


Meta.Item = Item

Meta.default = Channel('default')
