import ast.nodes as nodes


class ParseActions(object):

    def question(self, string, location, tokens):
        print "-----Question---"
        print string
        print tokens.asDict()
        print "==============="
        node = nodes.Question(**tokens[0].asDict())
        return node

    def init_variable(self, string, location, tokens):
        print "-----Init Variable---"
        node = nodes.Variable(**tokens[0].asDict())
        return node

    def variable(self, string, location, tokens):
        print "-----Use Variable---"
        print tokens
        node = nodes.Variable(name=tokens[0], datatype=nodes.StringType())
        return node

    def label(self, string, location, tokens):
        print "-----Label Variable---"
        print tokens
        node = nodes.Label(**tokens.asDict())
        return node

    def statements(self, string, location, tokens):
        print "-----Statements Body---"
        print tokens[0]
        print "==============="
        return nodes.Block(tokens[0])

    def form(self, string, location, tokens):
        print "-----Form Node---"
        print tokens.asDict()
        print "==============="
        node = nodes.Form(**tokens[0].asDict())
        return node

    def string_primitive(self, string, location, tokens):
        print "-----String value Node---"
        print tokens.asDict()
        print "==============="
        return nodes.StringPrimitive(*tokens)

    def string_type(self, string, location, tokens):
        print "-----string type Node---"
        print tokens.asDict()
        print "==============="
        return nodes.StringType()

    def integer_type(self, string, location, tokens):
        print "-----integer type Node---"
        print tokens.asDict()
        print "==============="
        return nodes.IntegerType()

    def boolean_type(self, string, location, tokens):
        return nodes.BooleanType()

    def money_type(self, string, location, tokens):
        return nodes.MoneyType()

    def date_type(self, string, location, tokens):
        print "-----date type Node---"
        print tokens.asDict()
        print "==============="
        return nodes.DateType()
