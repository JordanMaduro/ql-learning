class ASTNode(object):
    pass


class ASTree(ASTNode):
    pass


class Expression(ASTNode):
    def __init__(self, value):
        self.value = value


class Statement(ASTNode):
    pass


class EmptyNode(ASTNode):
    pass


class Block(ASTNode):
    def __init__(self, statements):
        self.statements = statements


class Assign(Statement):
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value


class Question(Statement):
    def __init__(self, variable, label, value):
        self.variable = variable
        self.label = label
        self.value = value


class If(Statement):
    def __init__(self, test, body, else_body=EmptyNode()):
        self.test = test
        self.body = body
        self.else_body = else_body


class Variable(Expression):
    def __init__(self, name, data_type, value=EmptyNode()):
        self.name = name
        self.data_type = data_type
        self.value = value


class BinaryOperation(Expression):
    pass


class Literal(Expression):
    pass


class Boolean(Expression):
    pass

class Type(ASTNode):
    def __init__(self, data_type):
        self.data_type = data_type
