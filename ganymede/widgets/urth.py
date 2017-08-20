from six.moves import builtins
from inspect import getargspec

from moretools import camelize
import lxml.etree

from IPython import get_ipython
from IPython.display import display, HTML, Javascript


class component(object):

    def render(self, id=None):
        return lxml.etree.tounicode(self.xml(id=id))

    def display(self, id=None):
        element = lxml.etree.Element('template', {
            'is': 'urth-core-bind',
        })
        element.append(self.xml(id=id))
        display(HTML(lxml.etree.tounicode(element)))


class Input(component):

    def __init__(self, value, label=None):
        self.value = value
        self.label = label

    def xml(self, id=None):
        element = lxml.etree.Element(widget, {
            k: str(v) for k, v in options.items()})
        if label is None:
            label = camelize(self.value.name, joiner=' ')
            element.set('label', label)
            element.set('value', '{{%s-%s}}' % (self.ref, name))
        return element


class function(component):

    class arg(object):

        def __init__(self, function, name):
            self.function = function
            self.name = name

        # def input(self, widget='paper-input', label=None):
        #     return Input(

    def __init__(self, func, args=None, id=None):
        self.func = func
        get_ipython().user_ns[self.ref] = func
        self.__dict__['args'] = args

    @property
    def ref(self):
        return '_ganymede_%i' % builtins.id(self.func)

    @property
    def args(self):
        if self.__dict__.get('args') is not None:
            return self.__dict__['args']
        spec = getargspec(self.func)
        return spec.args

    def xml(self, id=None):
        ref = self.ref
        element = lxml.etree.Element('urth-core-function', {
            'id': id or ref,
            'ref': ref,
        })
        for argname in self.args:
            element.set('arg-%s' % argname, '{{%s-%s}}' % (ref, argname))
        return element

    def button(self, icon=None):
        element = lxml.etree.Element('paper-button', {
            'onClick': "%s.invoke()" % self.ref,
        })
        if icon is not None:
            element.append(lxml.etree.Element('iron-icon', {
                'src': icon,
            }))
        return element
