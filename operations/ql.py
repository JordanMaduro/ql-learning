from ast.nodes import *
from abc import ABCMeta, abstractmethod


class ExpressionAlg(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def literal(self, value):
        pass

    @abstractmethod
    def stringPrimitive(self, value):
        pass

    @abstractmethod
    def variable(self, name, datatype):
        pass


class StatementAlg(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def question(self, variable, label):
        pass

    @abstractmethod
    def block(self, statements):
        pass

class QlAlg(ExpressionAlg, StatementAlg):
    __metaclass__ = ABCMeta

    @abstractmethod
    def form(self, statements):
        pass

    @abstractmethod
    def type(self, data_type):
        pass


class QlAlgView(QlAlg):

    def literal(self, value):
        literal = type("Literal", (Literal,), {
                       "view": lambda self: "Literal({})".format(str(self.value))})
        return literal(value)

    def label(self, label):
        _node = type("Literal", (Label,), {
                       "view": lambda self: "Label({})".format(str(self.label))})
        return _node(label)

    def boolean_type(self):
        _node = type("BooleanType", (BooleanType,), {
            "view": lambda self: "BooleanType()"})
        return _node()

    def string_type(self):
        _node = type("StringType", (StringType,), {
            "view": lambda self: "StringType()"})
        return _node()

    def integer_type(self):
        _node = type("IntegerType", (IntegerType,), {
            "view": lambda self: "IntegerType()"})
        return _node()

    def money_type(self):
        _node = type("MoneyType", (MoneyType,), {
            "view": lambda self: "MoneyType()"})
        return _node()

    def date_type(self):
        _node = type("DateType", (DateType,), {
            "view": lambda self: "DateType()"})
        return _node()

    def stringPrimitive(self, value):
        string_primitive = type("StringPrimitive", (StringPrimitive,), {
            "view": lambda self: "StringPrimitive({})".format(str(self.value))})
        return string_primitive(value)

    def form(self, name, block):
        _form = type("Form", (Form,), {
            "view": lambda self: "Form({}, {})".format(str(self.name.view()), self.block.view())})
        return _form(name, block)

    def block(self, statements):
        def _view(obj):
            return "Block(\n{}\n)".format((("\n").join([k.view() for _, k in enumerate(obj.statements)])))
        block = type("Block", (Block,), {
            "view": _view
        })
        return block(statements)

    def variable(self, name, datatype):
        variable = type("Variable", (Variable,), {"view": lambda self: "Variable(name={}, datatype={})".format(
            str(self.name), self.datatype.view())})
        return variable(name, datatype)

    def question(self, variable, label):
        question = type("Question", (Question,), {"view": lambda self: "Question(variable={}, label='{}')".format(
            self.variable.view(), str(self.label))})
        return question(variable, label)

    def type(self, data_type):
        _typeClass = type("Type", (Type,), {
            "view": lambda self: "Type({})".format(str(self.data_type.__class__.__name__))})
        return _typeClass(data_type)
