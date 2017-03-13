from ast.basic import *
from abc import ABCMeta, abstractmethod


class QlAlg(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def literal(self, value):
        pass

    @abstractmethod
    def stringPrimitive(self, value):
        pass

    @abstractmethod
    def block(self, statements):
        pass

    @abstractmethod
    def form(self, statements):
        pass

    @abstractmethod
    def variable(self, name, datatype):
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

    def stringPrimitive(self, value):
        string_primitive = type("StringPrimitive", (StringPrimitive,), {
            "view": lambda self: "StringPrimitive({})".format(str(self.value))})
        return string_primitive(value)

    def form(self, name, block):
        _form = type("Form", (Form,), {
            "view": lambda self: "Form({}, {})".format(str(self.name.view()), self.block.view())})
        return _form(name, block)

    def block(self, statements):
        def print_me(obj):
            print obj
            return "Block(\n{}\n)".format((("\n").join([k.view() for _, k in enumerate(obj.statements)])))
        block = type("Block", (Block,), {
            # "view": lambda self: "Block(\n{}\n)".format((("\n").join([k.view() for _, k in enumerate(self.statements)])))
            "view": print_me
        })
        return block(statements)

    def variable(self, name, datatype):
        variable = type("Variable", (Variable,), {"view": lambda self: "Variable(name={}, datatype={})".format(
            str(self.name), str(self.datatype))})
        return variable(name, datatype)

    def question(self, variable, label):
        question = type("Question", (Question,), {"view": lambda self: "Question(variable={}, label={})".format(
            self.variable.view(), str(self.label))})
        return question(variable, label)

    def type(self, data_type):
        _typeClass = type("Type", (Type,), {
            "view": lambda self: "Type({})".format(str(self.data_type.__class__.__name__))})
        return _typeClass(data_type)


class QlAlgEval(QlAlg):

    def literal(self, value):
        literal = type("Literal", (Literal,), {
            "eval": lambda self: self.value})
        return literal(value)

    def stringPrimitive(self, value):
        string_primitive = type("StringPrimitive", (StringPrimitive,), {
            "eval": lambda self: self.value})
        return string_primitive(value)

    # def boolean(self, value):
    #     boolean = type("Boolean", (Boolean,), {
    #         "eval": lambda self: self.value})
    #     return boolean(value)

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

    # def empty(self):
    #     empty = type("EmptyNode", (EmptyNode,), {
    #         "eval": lambda self: None})
    #     return empty()

    # def assign(self, variable, value):
    #     def _assign(self):
    #         self.variable.value = self.value.eval()
    #         return self.variable.value
    #     assign = type("Assign", (Assign,), {
    #         "eval": _assign})
    #     return assign(variable, value)

    def variable(self, name, data_type, value):
        variable = type("Variable", (Variable,), {
            "eval": lambda self: self.value.eval()})
        return variable(name, value)

    def question(self, variable, label, value):
        question = type("Question", (Question,), {
                        "eval": lambda self: self.value.eval()})
        return question(variable, label, value)

    # def type(self, data_type):
    #     _typeClass = type("Type", (Type,), {
    #         "eval": lambda self: 0 })
    #     return _typeClass(data_type)


class QlAlgV2(QlAlg):
    __metaclass__ = ABCMeta

    @abstractmethod
    def big(self, value):
        pass


class QlAlgV2View(QlAlgView):

    def big(self, value):
        big = type("Big", (Big,), {
            "view": lambda self: "Big({})".format(str(self.value))})
        return big(value)
