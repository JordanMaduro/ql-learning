from pyparsing import *
import ast.basic as nodes
import ast.types as types
'''
form taxOfficeExample {
  "Did you sell a house in 2010?"
    hasSoldHouse: boolean
  "Did you buy a house in 2010?"
    hasBoughtHouse: boolean
  "Did you enter a loan?"
    hasMaintLoan: boolean
  if (hasSoldHouse) {
    "What was the selling price?"
      sellingPrice: money
    "Private debts for the sold house:"
      privateDebt: money
    "Value residue:"
      valueResidue: money =
        (sellingPrice - privateDebt)
  }
  "Is this questions being printed?"
    isPrinted: boolean
}
'''

'''
BNF
<form> ::= <type> <identifier> '{' <block_body> '}'
<block_body> ::= <question> | <conditional>
<conditional> ::= 'if' '(' <exp> | <boolean> ')' '{' <block_body> '}'
<question> ::= <label> <variable> ':' <data_type>
<question_value> ::= expr | data_type
<type> ::= <Ident>
<identifier> ::= <Ident>
<data_type> ::= <boolean>|<money>
<boolean> ::= 'true' | 'false'
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

        def question_node(string, location, tokens):
            print "-----Question---"
            print string
            print tokens.asDict()
            print "==============="
            node = nodes.Question(**tokens[0].asDict())
            return node

        def init_variable_node(string, location, tokens):
            print "-----Init Variable---"
            print string
            print "==============="
            node = nodes.Variable(**tokens[0].asDict())
            return node

        def statements_action(string, location, tokens):
            print "-----Statements Body---"
            print tokens[0]
            print "==============="
            return nodes.Block(tokens[0])

        def form_action(string, location, tokens):
            print "-----Form Node---"
            print tokens.asDict()
            print "==============="
            node = nodes.Form(**tokens[0].asDict())
            return node

        def string_value_action(string, location, tokens):
            print "-----String value Node---"
            print tokens.asDict()
            print "==============="
            return nodes.StringPrimitive(*tokens)

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
        boolean_type = Literal('boolean')("datatype")
        data_type = boolean_type
        question_value = data_type("data_type")

        init_variable = Group(variable + colon + data_type)('variable')

        question = Group(label + init_variable)

        block_body = Forward()

        block_body << ZeroOrMore(Group(question))

        statements = Group(OneOrMore(question))('block')

        string_literal = identifier('string_literal')
        form_name = string_literal("name")
        form = Group(formType.suppress() + form_name.addParseAction(string_value_action) +
                     lbrace + statements + rbrace)("form")

        # def label_node(string, location, tokens):

        init_variable.addParseAction(init_variable_node)
        question.addParseAction(question_node)
        statements.addParseAction(statements_action)
        form.addParseAction(form_action)

        # label.addParseAction(label_node)
        grammar << (form | question)("ast")
        return grammar

    def parse(self, input_string):
        return self.grammar.parseString(input_string)
