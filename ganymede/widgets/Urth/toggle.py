"""Pythonic API for Polymer toggle buttons."""

from .channel import ChannelBindable
from .polymer import Polymer


class ToggleButton(Polymer.Component, ChannelBindable):

    def __init__(
        self, text=None, channel=None, channel_key=None, interval=None,
        html_class=None, **html_attrs):

        super().__init__(
            'paper-toggle-button', html_class=html_class, **html_attrs)
        ChannelBindable.__init__(self, channel, key=channel_key)

        if text is not None:
            self.text = text
        self.interval = interval

    def __call__(self, func):
        assert self.channel is not None, "{!r} has no channel".format(self)

        if self.text is None:
            self.text = " ".join(func.__name__.capitalize().split('_'))

        key = self.channel_key
        if key is None:
            key = 'do_{}'.format('_'.join(self.text.lower().split()))
        self.channel[key] = False

        # TODO: Element.changed() deco
        self._element.set('onChange', """
        if (this.checked) {{
            this.interval = setInterval(() => {{
                (($) => {{
                    $("urth-core-channel[name='{name}']")[0].set(
                        '{key}', true);

                }})(window.jQuery);
            }}, {msec});
        }}
        else {{
            clearInterval(this.interval);
            delete this.interval;
        }};
        """.format(name=self.channel.name, key=key, msec=self.interval))

        @self.channel.changed(key)
        def handler(do_call, _):
            if do_call:
                try:
                    func()
                finally:
                    self.channel[key] = False

        return self
