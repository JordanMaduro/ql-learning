from ast.nodes import *
from abc import ABCMeta, abstractmethod


class QlAlg(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def literal(self, value):
        pass

    @abstractmethod
    def boolean(self, value):
        pass

    @abstractmethod
    def block(self, statements):
        pass

    @abstractmethod
    def ifElse(self, test, body, else_body=None):
        pass

    @abstractmethod
    def empty(self):
        pass

    @abstractmethod
    def assign(self, variable, value):
        pass

    @abstractmethod
    def variable(self, name, data_type, value):
        pass

    @abstractmethod
    def question(self, variable, label, value):
        pass

    @abstractmethod
    def type(self, data_type):
        pass


class QlAlgView(QlAlg):

    def literal(self, value):
        literal = type("Literal", (Literal,), {
                       "view": lambda self: "Literal({})".format(str(self.value))})
        return literal(value)

    def boolean(self, value):
        boolean = type("Boolean", (Boolean,), {
                       "view": lambda self: "Boolean({})".format(str(self.value))})
        return boolean(value)

    def block(self, statements):
        block = type("Block", (Block,), {
            "view": lambda self: "Block(\n{}\n)".format(str(("\n").join([k.view() for _, k in enumerate(self.statements)])))
        })
        return block(statements)

    def ifElse(self, test, body, else_body=None):
        ifElse = type("If", (If,), {"view": lambda self: "If({}, {}, {})".format(
            self.test.view(), self.body.view(), self.else_body.view())})
        return ifElse(test, body, else_body)

    def empty(self):
        return type("EmptyNode", (EmptyNode,), {
            "view": lambda self: "EmptyNode()"})

    def assign(self, variable, value):
        assign = type("Assign", (Assign,), {
            "view": lambda self: "Assign({},{})".format(self.variable.view(),  self.value.view())})
        return assign(variable, value)

    def variable(self, name, data_type, value):
        variable = type("Variable", (Variable,), {"view": lambda self: "Variable(name={}, data_type={}, value={})".format(
            self.name.view(), self.data_type.view(), self.value.view())})
        return variable(name, data_type, value)

    def question(self, variable, label, value):
        question = type("Question", (Question,), {"view": lambda self: "Question(variable={}, label={})".format(
            self.variable.view(), self.label.view())})
        return question(variable, label, value)

    def type(self, data_type):
        _typeClass = type("Type", (Type,), {
            "view": lambda self: "Type({})".format(str(self.data_type.__class__.__name__ ))})
        return _typeClass(data_type)


class QlAlgEval(QlAlg):

    def literal(self, value):
        literal = type("Literal", (Literal,), {
            "eval": lambda self: self.value})
        return literal(value)

    def boolean(self, value):
        boolean = type("Boolean", (Boolean,), {
            "eval": lambda self: self.value})
        return boolean(value)

    def block(self, statements):
        block = type("Block", (Block,), {
            "eval": lambda self: 0})
        return block(statements)

    def ifElse(self, test, body, else_body=None):
        def ifEval(o):
            if o.test.eval():
                return o.body.eval()
            else:
                return o.else_body.eval()
        ifElse = type("If", (If,), {"eval": ifEval})
        return ifElse(test, body, else_body)

    def empty(self):
        empty = type("EmptyNode", (EmptyNode,), {
            "eval": lambda self: None})
        return empty()

    def assign(self, variable, value):
        def _assign(self):
            self.variable.value = self.value.eval()
            return self.variable.value
        assign = type("Assign", (Assign,), {
            "eval": _assign})
        return assign(variable, value)

    def variable(self, name, data_type, value):
        variable = type("Variable", (Variable,), {
            "eval": lambda self: self.value.eval()})
        return variable(name, value)

    def question(self, variable, label, value):
        question = type("Question", (Question,), {"eval": lambda self: self.value.eval()})
        return question(variable, label, value)

    def type(self, data_type):
        _typeClass = type("Type", (Type,), {
            "eval": lambda self: 0 })
        return _typeClass(data_type)