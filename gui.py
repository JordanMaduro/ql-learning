import ast.nodes
import operations.ql
import operations.gui
from singledispatch import singledispatch
from Tkinter import *
from parsers import ql
from operation_factory import AlgebraFactory
import sys

# Read QL file to string
with open('tax_office_example.ql', 'r') as ql_file:
    ql_string = ql_file.read().replace('\n', '')


# init parser
parser = ql.Parser()


# build AST
form_ast = parser.parse(ql_string).ast

test_ast = parser.parse('form apple {   "How many people are there in your household?" numberInHoushold: integer}').ast
action = operations.ql.QlAlgView


isinstance_alg = form_ast.alg(action())
print isinstance_alg.view()

# Make printable AST
action = operations.ql.QlAlgView
instance_alg = AlgebraFactory.make(action(), form_ast)
print instance_alg.view()

action = operations.gui.QlAlgGUI
instance_alg = AlgebraFactory.make(action(), form_ast)


class Section(Frame):

    def createWidgets(self):
        [x.render(self) for x in self.widgets]
        self.label = Label(self, text="Section: 1").pack()

    def add_widget(self, widget):
        self.widgets.append(widget)

    def __init__(self, master=None,  **args):
        ''' API: widgets, isVisible, hide, render, show  '''
        Frame.__init__(self, master, args)
        self.widgets = []
        self.pack()
        self.createWidgets()


class Application(Frame):

    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.pack()

        self.section1 = Section(self, bg="blue")
        self.section1.pack({"fill": "both"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
root.maxsize(root.maxsize(1000, 400), 400)
root.minsize(400, 400)
app = Application(master=root)

instance_alg = AlgebraFactory.make(operations.gui.QlAlgGUI(), form_ast)
instance_alg.render(app.section1)


# Register variables and create Hashmap
# Should create a context with reference to the Hashmap and pass it to the Render Algebra
# A context could be a State object
# Create a renderable AST with method Render()

# Render AST to Window!
# expr.render(root)

app.mainloop()
root.destroy()


print instance_alg.render(root)
