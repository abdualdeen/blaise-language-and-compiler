"""
CSCE 425/825 Semester Project
Project 4: Code Generation

Author: Robert Dyer <rdyer@unl.edu>
"""
import sys
from antlr4 import FileStream, InputStream
from BlaiseLexer import BlaiseLexer
from BlaiseParser import BlaiseParser
from Project3Visitor import Project3Visitor
from Project4Visitor import Project4Visitor
from syms import SymbolTable, Int, BindingList, Procedure


def main(logger, inputfile=None, inputstr=None):
    if inputfile is not None:
        input_stream = FileStream(inputfile)
    elif inputstr is not None:
        input_stream = InputStream(inputstr)
    else:
        logger.error('must specify either inputfile or inputstr')
        sys.exit(-2)

    lexer = BlaiseLexer(input_stream)
    parser = BlaiseParser(lexer)
    p = parser.parseProgram()

    if parser.err:
        print(parser.err)
        sys.exit(-3)

    try:
        #add the out() function globally
        syms = SymbolTable()
        args = BindingList()
        args.bindings.append(Int())
        syms.bind('out', Procedure(args))

        p.accept(Project3Visitor(), syms)

        syms_proj4 = SymbolTable(scope = [])
        print(p.accept(Project4Visitor(), syms_proj4))
    except Exception as e:
        print(e)
