"""Pythonic API for Polymer buttons."""

from .channel import ChannelBindable
from .polymer import Polymer


class Meta(type(Polymer.Component), type(ChannelBindable)):

    def raised(cls, text=None, html_class=None, **html_attrs):
        html_attrs.setdefault('raised', None)
        return cls(text, html_class=html_class, **html_attrs)


class Button(Polymer.Component, ChannelBindable, metaclass=Meta):

    def __init__(
            self, text=None, channel=None, channel_key=None,
            html_class=None, **html_attrs):

        super().__init__(
            'paper-button', html_class=html_class, **html_attrs)
        ChannelBindable.__init__(self, channel)
        if text is not None:
            self.text = text

    def __call__(self, func):
        assert self.channel is not None, "{!r} has no channel".format(self)

        if self.text is None:
            self.text = " ".join(func.__name__.capitalize().split('_'))

        channel_key = 'do_{}'.format('_'.join(self.text.lower().split()))
        self.channel[channel_key] = False
        self._element.set('onClick', """
        (($) => {{
            $("urth-core-channel[name='{}']")[0].set('{}', true);
        }})(window.jQuery);
        """.format(self.channel.name, channel_key))

        @self.channel.changed(channel_key)
        def handler(do_call, _):
            if do_call:
                try:
                    func()
                finally:
                    self.channel[channel_key] = False

        return self
