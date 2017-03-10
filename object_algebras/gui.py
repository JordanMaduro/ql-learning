import ql
import ast.nodes as nodes
import ui.elements
from Tkinter import *


class QlAlgGUI(ql.QlAlg):
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

    def ifElse(self, test, body, else_body=None):
        def ifEval(o):
            if o.test.eval():
                return o.body.eval()
            else:
                return o.else_body.eval()
        ifElse = type("If", (nodes.If,), {"render": ifEval})
        return ifElse(test, body, else_body)

    def empty(self):
        empty = type("EmptyNode", (nodes.EmptyNode,), {
            "render": lambda self: None})
        return empty()

    def assign(self, variable, value):
        def _assign(self):
            self.variable.value = self.value.eval()
            return self.variable.value
        assign = type("Assign", (nodes.Assign,), {
            "render": _assign})
        return assign(variable, value)

    def variable(self, name, data_type, value):
        variable = type("Variable", (nodes.Variable,), {
            "render": lambda self: self.name.render()})
        return variable(name, value)

    def question(self, variable, label, value):
        def render(self, pane):
            self.value = IntVar()

            def show_state():
                print self.question.render(), self.value.get()
            checkbox = Checkbutton(
                pane, text=self.label.render(), variable=self.value, command=show_state)
            checkbox.pack()
            return checkbox
            # CheckBoxQuestion should be based on the data_type
        question = type("Question", (ui.elements.CheckBoxQuestion,), {
                        "render": render})
        return question(variable, label, value)

    def type(self, data_type):
        _typeClass = type("Type", (nodes.Type,), {
            "eval": lambda self: 0})
        return _typeClass(data_type)
