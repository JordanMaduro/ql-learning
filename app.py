from ast.nodes import *
from object_algebras.ql import *
import ast.types

def makeExpr(OAlg):

    # return OAlg.ifElse(OAlg.boolean(True), OAlg.literal(21), OAlg.literal(78))
    # return OAlg.ifElse(OAlg.boolean(True), OAlg.block([
    #      OAlg.assign(OAlg.literal("Works"),OAlg.literal("Money"),OAlg.literal(99))
    # ]), OAlg.literal(78))
    # return OAlg.assign(OAlg.variable(OAlg.literal("Foo"), OAlg.literal("bar")), OAlg.literal('money'), OAlg.literal(78))
    return OAlg.question(
        OAlg.variable(
            OAlg.literal("hasSoldHouse"), 
            OAlg.type(ast.types.Boolean()),
            OAlg.literal(None)), 
        OAlg.literal("Have you sold a house?"), 
        OAlg.boolean(False)
        )


# expr = makeExpr(QlAlgView())

# print(expr.view())

expr = makeExpr(QlAlgEval())

print(expr.eval())
