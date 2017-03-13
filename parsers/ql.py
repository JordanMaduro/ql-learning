from pyparsing import *
import ast.nodes as nodes
from parsers.actions import ParseActions

'''
form taxOfficeExample {
  "Did you sell a house in 2010?"
    hasSoldHouse: boolean
  "Did you buy a house in 2010?"
    hasBoughtHouse: boolean
  "Did you enter a loan?"
    hasMaintLoan: boolean
  "Is this questions being printed?"
    isPrinted: boolean
}
'''


class Parser(object):
    'Grammar class'

    def __init__(self):
        self.grammar = self.compileGrammar()

    def compileGrammar(self):

        def te(*ag):
            print "---------------"
            print "\n".join([str(a) for k, a in enumerate(ag)])
            print "==============="

        actions = ParseActions()

        grammar = Forward()
        # Literals to be ignored
        lbrace = Literal('{').suppress()
        rbrace = Literal('}').suppress()
        lpar = Literal('(').suppress()
        rpar = Literal(')').suppress()
        colon = Literal(':').suppress()
        equals = Literal('=').suppress()

        # Keywords
        if_key = Keyword("if")

        true_key = Keyword("true")
        false_key = Keyword("false")

        identifier = Word(alphanums)
        variable = identifier("name")
        formType = identifier("type")
        label = QuotedString('"')("label")

        # DataTypes
        boolean_type = Literal('boolean').addParseAction(actions.boolean_type)
        money_type = Literal('money').addParseAction(actions.money_type)
        string_type = Literal('string').addParseAction(actions.string_type)
        integer_type = Literal('integer').addParseAction(actions.integer_type)

        data_type = Or(boolean_type | money_type |
                       string_type | integer_type)("datatype")

        question_value = data_type("data_type")

        init_variable = Group(variable + colon + data_type)('variable')

        question = Group(label + init_variable)

        operator = Group(Literal("+") | Literal("-") |
                         Literal("/") | Literal("*"))
        operand = variable('variable')

        block_body = Forward()

        block_body << ZeroOrMore(Group(question))

        statements = Group(OneOrMore(question))('block')

        string_literal = identifier('string_literal')
        form_name = string_literal("name")
        form = Group(formType.suppress() + form_name.addParseAction(actions.string_primitive) +
                     lbrace + statements + rbrace)("form")

        # def label_node(string, location, tokens):

        # Attach actions
        #operand.addParseAction(actions.variable)
        init_variable.addParseAction(actions.init_variable)
        question.addParseAction(actions.question)
        statements.addParseAction(actions.statements)
        form.addParseAction(actions.form)

        # label.addParseAction(actions.label)

        grammar << (form | question)("ast")
        return grammar

    def parse(self, input_string):
        return self.grammar.parseString(input_string)
