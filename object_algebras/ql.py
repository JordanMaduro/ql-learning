from ast.nodes import *


class QlAlg(object):

    def literal(self, value):
        return Literal(value)

    def boolean(self, value):
        return Boolean(value)

    def block(self, statements):
        return Block(statements)

    def ifElse(self, test, body, else_body=None):
        return If(test, body, else_body)

    def empty(self):
        return EmptyNode()

    def assign(self, variable, data_type, value):
        return Assign(variable, data_type, value)

    def variable(self, name, value):
        return Variable(name, value)

    def question(self, variable, label, value):
        return Question(variable, label, value)


class QlAlgView(object):

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

    def assign(self, variable, data_type, value):
        assign = type("Assign", (Assign,), {
            "view": lambda self: "Assign({},{},{})".format(self.variable.view(), self.data_type.view(), self.value.view())})
        return assign(variable, data_type, value)

    def variable(self, name, value):
        variable = type("Variable", (Variable,), {"view": lambda self: "Variable({}, {})".format(
            self.name.view(), self.value.view())})
        return variable(name, value)

    def question(self, variable, label, value):
        question = type("Question", (Question,), {"view": lambda self: "Question({}, {})".format(
            self.variable.view(), self.label.view())})
        return question(variable, label, value)


class QlAlgEval(object):

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

    def assign(self, name, data_type, value):
        assign = type("Assign", (Assign,), {
            "eval": lambda self: None})
        return assign(name, data_type, value)

    def variable(self, name, data_type, value):
        variable = type("Variable", (Variable,), {
            "eval": lambda self: self.value})
        return variable(name, value)
