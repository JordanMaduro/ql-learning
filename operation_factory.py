import ast.nodes
from singledispatch import singledispatch


class AlgebraFactory(object):

    def __init__(self):
        pass

    @classmethod
    def make(self, alg, tree):

        @singledispatch
        def handle_node(obj):
            # print obj
            #print "Don't know this type: ", type(obj), obj
            return obj

        @handle_node.register(ast.nodes.Form)
        def handle_Form(obj):
            return alg.form(**apply_alg(vars(obj)))

        @handle_node.register(ast.nodes.Block)
        def handle_Block(obj):
            return alg.block([self.make(alg, x) for x in obj.statements])

        @handle_node.register(ast.nodes.Question)
        def handle_Question(obj):
            return alg.question(**apply_alg(vars(obj)))

        @handle_node.register(ast.nodes.StringPrimitive)
        def handle_StringPrimitive(obj):
            return alg.stringPrimitive(**vars(obj))

        @handle_node.register(ast.nodes.BooleanType)
        def handle_BooleanType(obj):
            return alg.boolean_type(**vars(obj))

        @handle_node.register(ast.nodes.MoneyType)
        def handle_MoneyType(obj):
            return alg.money_type(**vars(obj))

        @handle_node.register(ast.nodes.StringType)
        def handle_StringType(obj):
            return alg.string_type(**vars(obj))

        @handle_node.register(ast.nodes.IntegerType)
        def handle_IntegerType(obj):
            return alg.integer_type(**vars(obj))

        @handle_node.register(ast.nodes.DateType)
        def handle_DateType(obj):
            return alg.date_type(**vars(obj))

        @handle_node.register(ast.nodes.Variable)
        def handle_Variable(obj):
            return alg.variable(**apply_alg(vars(obj)))

        @handle_node.register(ast.nodes.Label)
        def handle_Label(obj):
            return alg.label(**apply_alg(vars(obj)))

        def apply_alg(params):
            return {k: self.make(alg, v) for (k, v) in params.items()}

        return handle_node(tree)
