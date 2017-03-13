import ql
import ast.basic as nodes
import ui.elements
from Tkinter import *


class QlAlgGUI(ql.QlAlg):
    ''' TODO  Proper implementation of the Render functions '''
    """ Return form elements """

    def literal(self, value):
        literal = type("Literal", (nodes.Literal,), {
            "render": lambda self: str(self.value)})
        return literal(value)

    def boolean(self, value):
        boolean = type("Boolean", (nodes.Boolean,), {
            "render": lambda self: self.value})
        return boolean(value)

    def block(self, statements):
        def render(self, pane):
            self.widgets = [x.render(pane) for _, x in enumerate(statements)]
        block = type("Block", (nodes.Block,), {"render": render})
        return block(statements)

    def form(self, name, block):
        def render(self, pane):
            self.block.render(pane)

        form = type("Form", (nodes.Form,), {"render": render})
        return form(name, block)

    def stringPrimitive(self, value):
        string_primitive = type("StringPrimitive", (nodes.StringPrimitive,), {
            "render": lambda self: None})
        return string_primitive(value)

    def variable(self, name, datatype):
        variable = type("Variable", (nodes.Variable,), {
            "render": lambda self: self.name.render()})
        return variable(name, datatype)

    def question(self, variable, label):
        def render(self, pane):
            self.value = IntVar()

            def show_state():
                print self.question, self.value.get()
            checkbox = Checkbutton(
                pane, text=self.label, variable=self.value, command=show_state)
            checkbox.pack()
            return checkbox
            # CheckBoxQuestion should be based on the data_type
        question = type("Question", (ui.elements.CheckBoxQuestion,), {
                        "render": render})
        return question(variable, label)

    def type(self, data_type):
        _typeClass = type("Type", (nodes.Type,), {
            "eval": lambda self: 0})
        return _typeClass(data_type)
