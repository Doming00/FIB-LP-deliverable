import sys
from antlr4 import *
from logo3dLexer import logo3dLexer
from logo3dParser import logo3dParser
from Visitor import Visitor

input_stream = FileStream(sys.argv[1])
lexer = logo3dLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = logo3dParser(token_stream)
tree = parser.root()

funcname = 'main'
var = []

if len(sys.argv) > 2:
    funcname = sys.argv[2]
    for i in range(3, len(sys.argv)):
        var.append(float(sys.argv[i]))

visitor = Visitor(funcname, var)
visitor.visit(tree)
visitor.iniExec()
