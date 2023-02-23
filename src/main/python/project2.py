"""
CSCE 425/825 Semester Project
Project 2: Parsing

Author: Robert Dyer <rdyer@unl.edu>
"""
import sys
from antlr4 import FileStream, InputStream
from BlaiseLexer import BlaiseLexer
from BlaiseParser import BlaiseParser
from Project2Visitor import Project2Visitor


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

    p.accept(Project2Visitor())
