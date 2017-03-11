from ast.nodes import *
from object_algebras.ql import *
from object_algebras.gui import *
import ast.types
from Tkinter import *
from singledispatch import singledispatch
from grammars import ql
import sys

parser = ql.Parser()
parsed_ast = parser.parse('form aaa {  "Did you sell a house in 2010?" hasSoldHouse: boolean }')
print parsed_ast
sys.exit()
def makeExpr(OAlg):

    # return OAlg.ifElse(OAlg.boolean(True), OAlg.literal(21), OAlg.literal(78))
    # return OAlg.ifElse(OAlg.boolean(True), OAlg.block([
    #      OAlg.assign(OAlg.literal("Works"),OAlg.literal("Money"),OAlg.literal(99))
    # ]), OAlg.literal(78))
    # return OAlg.assign(OAlg.variable(OAlg.literal("Foo"),
    # OAlg.literal("bar")), OAlg.literal('money'), OAlg.literal(78))
    return OAlg.block([
        OAlg.question(
            OAlg.variable(
                OAlg.literal("hasSoldHouse"),
                OAlg.type(ast.stypes.Boolean()),
                OAlg.literal(None)),
            OAlg.literal("Have you sold a house?"),
            OAlg.boolean(False)
        ),
        OAlg.question(
            OAlg.variable(
                OAlg.literal("hasBoughtHouse"),
                OAlg.type(ast.types.Boolean()),
                OAlg.literal(None)),
            OAlg.literal("Did you buy a house in 2016?"),
            OAlg.boolean(False)
        ),
        OAlg.question(
            OAlg.variable(
                OAlg.literal("hasBoughtHouse"),
                OAlg.type(ast.types.Boolean()),
                OAlg.literal(None)),
            OAlg.literal("Did you buy a house in 2016?"),
            OAlg.boolean(False)
        ),
        OAlg.question(
            OAlg.variable(
                OAlg.literal("hasBoughtHouse"),
                OAlg.type(ast.types.Boolean()),
                OAlg.literal(None)),
            OAlg.literal("Did you buy a house in 2016?"),
            OAlg.boolean(False)
        ),        OAlg.question(
            OAlg.variable(
                OAlg.literal("hasBoughtHouse"),
                OAlg.type(ast.types.Boolean()),
                OAlg.literal("aaa")),
            OAlg.literal("Did you buy a house in 2016?"),
            OAlg.boolean(False)
        ),        OAlg.question(
            OAlg.variable(
                OAlg.literal("hasBoughtHouse"),
                OAlg.type(ast.types.Boolean()),
                OAlg.literal(None)),
            OAlg.literal("Did you buy a house in 2016?"),
            OAlg.boolean(False)
        ),        OAlg.question(
            OAlg.variable(
                OAlg.literal("hasBoughtHouse"),
                OAlg.type(ast.types.Boolean()),
                OAlg.literal(None)),
            OAlg.literal("Did you buy a house in 2016?"),
            OAlg.boolean(False)
        ),        OAlg.question(
            OAlg.variable(
                OAlg.literal("hasBoughtHouse"),
                OAlg.type(ast.types.Boolean()),
                OAlg.literal(None)),
            OAlg.literal("Did you buy a house in 2016?"),
            OAlg.boolean(False)
        ),        OAlg.question(
            OAlg.variable(
                OAlg.literal("hasBoughtHouse"),
                OAlg.type(ast.types.Boolean()),
                OAlg.literal(None)),
            OAlg.literal("Did you buy a house in 2016?"),
            OAlg.boolean(False)
        ),        OAlg.question(
            OAlg.variable(
                OAlg.literal("hasBoughtHouse"),
                OAlg.type(ast.types.Boolean()),
                OAlg.literal(None)),
            OAlg.literal("Did you buy a house in 2016?"),
            OAlg.boolean(False)
        )
    ])

example_ast = Question(
    variable=ast.nodes.Variable(
        Literal("hasBoughtCar"),
        Literal(True),  # Type(ast.types.Boolean()),
        Literal(True)
    ),
    label=Literal("Did you buy a car in 2020?"),
    value=Big(False)
)


class AlgebraFactory(object):

    def __init__(self):
        pass

    @classmethod
    def make(self, alg, tree):

        @singledispatch
        def handle_node(obj):
            print obj
            print "Got a Nothing"

        @handle_node.register(Question)
        def handle_Question(obj):
            return alg.question(**apply_alg(vars(obj)))

        @handle_node.register(Literal)
        def handle_Literal(obj):
            return alg.literal(**vars(obj))

        @handle_node.register(ast.nodes.Variable)
        def handle_Variable(obj):
            return alg.variable(**apply_alg(vars(obj)))

        @handle_node.register(Boolean)
        def handle_Boolean(obj):
            return alg.boolean(**vars(obj))
        
        @handle_node.register(Big)
        def handle_Big(obj):
            return alg.big(**vars(obj))

        def apply_alg(params):
            return {k: self.make(alg, v) for (k, v) in params.items()}

        return handle_node(tree)




# expr = makeExpr(QlAlgView())

# print(expr.view())

# expr = makeExpr(QlAlgEval())

# print(expr.eval())


def alg_to_ast(tree):

    @singledispatch
    def handle_node(obj):
        print "Got a Nothing"

    @handle_node.register(Question)
    def handle_Question(obj):
        print "Got a question"

    return handle_node(tree)

action = QlAlgView
instance_alg = AlgebraFactory.make(action(), Literal("Apple"))
print instance_alg.view()


class Application(Frame):

    def say_hi(self):
        print "hi there, everyone!"

    def show_state(self):
        print self.var.get()

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi
        self.var = IntVar()
        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


root = Tk()
root.maxsize(root.maxsize(1000, 400), 400)
root.minsize(400, 400)
app = Application(master=root)

# Register variables and create Hashmap
# Should create a context with reference to the Hashmap and pass it to the Render Algebra
# A context could be a State object
# Create a renderable AST with method Render()
expr = makeExpr(QlAlgGUI())
# Render AST to Window!
expr.render(root)

app.mainloop()
root.destroy()
