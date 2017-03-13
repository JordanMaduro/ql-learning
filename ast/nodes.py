class ASTNode(object):

    def alg(self, _alg):
        pass


class Expression(ASTNode):
    pass


class Statement(ASTNode):
    pass


class Value(ASTNode):

    def __init__(self, value):
        self.value = value


class Label(ASTNode):

    def __init__(self, label):
        self.label = label

    def alg(self, _alg):
        return _alg.label(self.label)


class Literal(ASTNode):

    def __init__(self, value):
        self.value = value


class Primitive(ASTNode):

    def __init__(self, value):
        self.value = value


class Variable(ASTNode):

    def __init__(self, name, datatype):
        self.name = name
        self.datatype = datatype

    def alg(self, _alg):
        return _alg.variable(self.name, self.datatype.alg(_alg))


class Form(ASTNode):

    def __init__(self, name, block):
        self.name = name
        self.block = block

    def alg(self, _alg):
        return _alg.form(self.name.alg(_alg), self.block.alg(_alg))


class Question(Statement):

    def __init__(self, variable, label):
        self.variable = variable
        self.label = label

    def alg(self, _alg):
        return _alg.question(self.variable.alg(_alg), self.label)


class StringPrimitive(Primitive):
    def alg(self, _alg):
        return _alg.stringPrimitive(self.value)


class BooleanPrimitive(Primitive):
    pass


class DatePrimitive(Primitive):
    pass


class MoneyPrimitive(Primitive):
    pass


class Type(ASTNode):

    def __init__(self):
        pass


class BooleanType(ASTNode):

    def alg(self, _alg):
        return _alg.boolean_type()


class StringType(ASTNode):

    def alg(self, _alg):
        return _alg.string_type()


class IntegerType(ASTNode):

    def alg(self, _alg):
        return _alg.integer_type()


class MoneyType(ASTNode):

    def alg(self, _alg):
        return _alg.money_type()


class DateType(ASTNode):

    def alg(self, _alg):
        return _alg.date_type()


class Block(ASTNode):

    def __init__(self, statements):
        self.statements = statements

    def alg(self, _alg):
        return _alg.block([x.alg(_alg) for x in self.statements])
