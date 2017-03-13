import ast.basic
from object_algebras.ql import *
from object_algebras.guiv2 import *
import ast.types
from Tkinter import *
from singledispatch import singledispatch
from grammars import qlv2 as ql
import sys


parser = ql.Parser()
parsed_ast = parser.parse(
    'form exampleTaxForm {  "Did you have a Dog in 2020?" hasADog: boolean "Did you sell a Car in 2011?" hasSoldCar: boolean "Did you sell a house in 2010?" hasSoldHouse: boolean }')
print parsed_ast.asDict()

AST = parsed_ast.ast


class AlgebraFactory(object):

    def __init__(self):
        pass

    @classmethod
    def make(self, alg, tree):

        @singledispatch
        def handle_node(obj):
            # print obj
            # print type(obj)
            # print "Got a Nothing"
            return obj

        @handle_node.register(ast.basic.Form)
        def handle_Form(obj):
            return alg.form(**apply_alg(vars(obj)))

        @handle_node.register(ast.basic.Block)
        def handle_Block(obj):
            return alg.block([self.make(alg, x) for x in obj.statements])

        @handle_node.register(ast.basic.Question)
        def handle_Question(obj):
            return alg.question(**apply_alg(vars(obj)))

        @handle_node.register(ast.basic.StringPrimitive)
        def handle_StringPrimitive(obj):
            return alg.stringPrimitive(**vars(obj))

        @handle_node.register(ast.basic.Variable)
        def handle_Variable(obj):
            return alg.variable(**apply_alg(vars(obj)))

        def apply_alg(params):
            print params
            return {k: self.make(alg, v) for (k, v) in params.items()}

        return handle_node(tree)


# expr = makeExpr(QlAlgView())

# print(expr.view())

# expr = makeExpr(QlAlgEval())

# print(expr.eval())


# def alg_to_ast(tree):

#     @singledispatch
#     def handle_node(obj):
#         print "Got a Nothing AST"

#     @handle_node.register(Question)
#     def handle_Question(obj):
#         print "Got a question"

#     return handle_node(tree)

action = QlAlgView
# instance_alg = AlgebraFactory.make(action(), ast.basic.StringPrimitive("Apple"))
instance_alg = AlgebraFactory.make(action(), AST)
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

instance_alg = AlgebraFactory.make(QlAlgGUI(), AST)
instance_alg.render(root)

# Register variables and create Hashmap
# Should create a context with reference to the Hashmap and pass it to the Render Algebra
# A context could be a State object
# Create a renderable AST with method Render()

# Render AST to Window!
# expr.render(root)

app.mainloop()
root.destroy()
