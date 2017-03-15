import ast.nodes as nodes


class ParseActions(object):

    def question(self, string, location, tokens):
        node = nodes.Question(**tokens[0].asDict())
        return node

    def init_variable(self, string, location, tokens):
        node = nodes.Variable(**tokens[0].asDict())
        return node

    def variable(self, string, location, tokens):
        node = nodes.Variable(name=tokens[0], datatype=nodes.StringType())
        return node

    def label(self, string, location, tokens):
        node = nodes.Label(**tokens.asDict())
        return node

    def statements(self, string, location, tokens):
        return nodes.Block(tokens[0])

    def form(self, string, location, tokens):
        node = nodes.Form(**tokens[0].asDict())
        return node

    def string_primitive(self, string, location, tokens):
        return nodes.StringPrimitive(*tokens)

    def string_type(self, string, location, tokens):
        return nodes.StringType()

    def integer_type(self, string, location, tokens):
        return nodes.IntegerType()

    def boolean_type(self, string, location, tokens):
        return nodes.BooleanType()

    def money_type(self, string, location, tokens):
        return nodes.MoneyType()

    def date_type(self, string, location, tokens):
        return nodes.DateType()
