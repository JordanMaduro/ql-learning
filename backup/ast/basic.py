class ASTNode(object):

    def __str__(self):
        return str(vars(self))


class Expression(ASTNode):
    pass


class Statement(ASTNode):
    pass


class Value(ASTNode):

    def __init__(self, value):
        self.value = value


class Literal(ASTNode):

    def __init__(self, value):
        self.value = value

class Primitive(ASTNode):

    def __init__(self, value):
        self.value = value


class Form(ASTNode):

    def __init__(self, name, block):
        self.name = name
        self.block = block


class Question(Statement):

    def __init__(self, variable, label):
        self.variable = variable
        self.label = label


class Variable(ASTNode):

    def __init__(self, name, datatype):
        self.name = name
        self.datatype = datatype


class StringPrimitive(Primitive):
    pass


class Block(ASTNode):

    def __init__(self, statements):
        self.statements = statements
