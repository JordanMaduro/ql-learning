from ast.nodes import *
from object_algebras.ql import *
from object_algebras.gui import *
import ast.types
from Tkinter import *
from singledispatch import singledispatch


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
                OAlg.type(ast.types.Boolean()),
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


print alg_to_ast(Question("a","a","c"))


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
