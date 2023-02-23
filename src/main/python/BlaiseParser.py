"""
This is the manually defined recursive descent parser, as required by the
project.

Note that my solution is overly complex when handling errors, because I
wanted to just parse what I could and *then* print the tree.  It is much
easier if you print while trying to parse!
"""
from antlr4 import Token
from asts import Program, Block, Variables, VariableDeclaration, Procedures, ProcedureDeclaration, FormalParameters,\
    Statement, AssignmentStatement, CallStatement, ActualParameters, CompoundStatement, IfStatement, WhileStatement,\
    Condition, Expression, Term, Factor, ParenthesisFactor
from BlaiseLexer import BlaiseLexer


class BlaiseParser:
    err = None

    lexer = None
    curToken = None

    def __init__(self, lexer):
        self.lexer = lexer
        self.curToken = lexer.nextToken()

    def error(self, msg):
        if self.err:
            raise Exception(self.err)
        self.err = msg
        raise Exception(msg)

    def accept(self, expected):
        if self.curToken.type != expected:
            return False
        self.curToken = self.lexer.nextToken()
        return True

    def expect(self, expected):
        if self.accept(expected):
            return True
        self.error("Error: unexpected token '" + self.curToken.text + "'")
        return False

    def parseProgram(self):
        if self.err:
            return
        node = Program()
        try:
            node.b = self.parseBlock()
            self.expect(BlaiseLexer.DOT)
            self.expect(Token.EOF)
        finally:
            return node

    def parseBlock(self):
        if self.err:
            return
        node = Block()
        try:
            if self.curToken.type == BlaiseLexer.VAR:
                node.vars = self.parseVariables()
            if self.curToken.type == BlaiseLexer.PROCEDURE:
                node.procs = self.parseProcedures()
            node.s = self.parseStatement()
        finally:
            return node

    def parseVariables(self):
        if self.err:
            return
        node = Variables()
        try:
            self.expect(BlaiseLexer.VAR)
            node.vars.append(self.parseVariableDeclaration())
            while not self.err and self.curToken.type == BlaiseLexer.COMMA:
                self.expect(BlaiseLexer.COMMA)
                node.vars.append(self.parseVariableDeclaration())
            self.expect(BlaiseLexer.SEMICOLON)
        finally:
            return node

    def parseVariableDeclaration(self):
        if self.err:
            return
        node = VariableDeclaration()
        try:
            node.id = self.curToken.text
            self.expect(BlaiseLexer.ID)
        finally:
            return node

    def parseProcedures(self):
        if self.err:
            return
        node = Procedures()
        try:
            node.procs.append(self.parseProcedureDeclaration())
            while not self.err and self.curToken.type == BlaiseLexer.PROCEDURE:
                node.procs.append(self.parseProcedureDeclaration())
        finally:
            return node

    def parseProcedureDeclaration(self):
        if self.err:
            return
        node = ProcedureDeclaration()
        try:
            self.expect(BlaiseLexer.PROCEDURE)
            node.id = self.curToken.text
            self.expect(BlaiseLexer.ID)
            self.expect(BlaiseLexer.LPAREN)
            if self.curToken.type == BlaiseLexer.ID:
                node.params = self.parseFormalParameters()
            self.expect(BlaiseLexer.RPAREN)
            node.b = self.parseBlock()
            self.expect(BlaiseLexer.SEMICOLON)
        finally:
            return node

    def parseFormalParameters(self):
        if self.err:
            return
        node = FormalParameters()
        try:
            node.params.append(self.parseVariableDeclaration())
            while not self.err and self.curToken.type == BlaiseLexer.COMMA:
                self.expect(BlaiseLexer.COMMA)
                node.params.append(self.parseVariableDeclaration())
        finally:
            return node

    def parseStatement(self):
        if self.err:
            return
        node = Statement()
        try:
            if self.curToken.type == BlaiseLexer.ID:
                node.assign = self.parseAssignmentStatement()
            elif self.curToken.type == BlaiseLexer.CALL:
                node.call = self.parseCallStatement()
            elif self.curToken.type == BlaiseLexer.BEGIN:
                node.compound = self.parseCompoundStatement()
            elif self.curToken.type == BlaiseLexer.IF:
                node.ifs = self.parseIfStatement()
            elif self.curToken.type == BlaiseLexer.WHILE:
                node.whiles = self.parseWhileStatement()
            else:
                self.error("Error: unexpected token '" + self.curToken.text + "'")
        finally:
            return node

    def parseAssignmentStatement(self):
        if self.err:
            return
        node = AssignmentStatement()
        try:
            node.id = self.curToken.text
            self.expect(BlaiseLexer.ID)
            self.expect(BlaiseLexer.ASSIGN)
            node.e = self.parseExpression()
        finally:
            return node

    def parseCallStatement(self):
        if self.err:
            return
        node = CallStatement()
        try:
            self.expect(BlaiseLexer.CALL)
            node.id = self.curToken.text
            self.expect(BlaiseLexer.ID)
            self.expect(BlaiseLexer.LPAREN)
            if self.curToken.type == BlaiseLexer.ID or\
                    self.curToken.type == BlaiseLexer.NUMBER or\
                    self.curToken.type == BlaiseLexer.LPAREN:
                node.params = self.parseActualParameters()
            self.expect(BlaiseLexer.RPAREN)
        finally:
            return node

    def parseActualParameters(self):
        if self.err:
            return
        node = ActualParameters()
        try:
            node.params.append(self.parseExpression())
            while not self.err and self.curToken.type == BlaiseLexer.COMMA:
                self.expect(BlaiseLexer.COMMA)
                node.params.append(self.parseExpression())
        finally:
            return node

    def parseCompoundStatement(self):
        if self.err:
            return
        node = CompoundStatement()
        try:
            self.expect(BlaiseLexer.BEGIN)
            node.stats.append(self.parseStatement())
            while not self.err and self.curToken.type == BlaiseLexer.SEMICOLON:
                self.expect(BlaiseLexer.SEMICOLON)
                if self.curToken.type != BlaiseLexer.ID and\
                        self.curToken.type != BlaiseLexer.CALL and\
                        self.curToken.type != BlaiseLexer.BEGIN and\
                        self.curToken.type != BlaiseLexer.IF and\
                        self.curToken.type != BlaiseLexer.WHILE:
                    break
                node.stats.append(self.parseStatement())
            self.expect(BlaiseLexer.END)
        finally:
            return node

    def parseIfStatement(self):
        if self.err:
            return
        node = IfStatement()
        try:
            self.expect(BlaiseLexer.IF)
            node.c = self.parseCondition()
            self.expect(BlaiseLexer.THEN)
            node.t = self.parseStatement()
            self.expect(BlaiseLexer.ELSE)
            node.f = self.parseStatement()
        finally:
            return node

    def parseWhileStatement(self):
        if self.err:
            return
        node = WhileStatement()
        try:
            self.expect(BlaiseLexer.WHILE)
            node.c = self.parseCondition()
            self.expect(BlaiseLexer.DO)
            node.s = self.parseStatement()
        finally:
            return node

    def parseCondition(self):
        if self.err:
            return
        node = Condition()
        try:
            node.lhs = self.parseExpression()
            node.op = self.curToken.text
            if self.curToken.type == BlaiseLexer.EQ:
                self.expect(BlaiseLexer.EQ)
            elif self.curToken.type == BlaiseLexer.NE:
                self.expect(BlaiseLexer.NE)
            elif self.curToken.type == BlaiseLexer.LT:
                self.expect(BlaiseLexer.LT)
            elif self.curToken.type == BlaiseLexer.LTE:
                self.expect(BlaiseLexer.LTE)
            elif self.curToken.type == BlaiseLexer.GT:
                self.expect(BlaiseLexer.GT)
            elif self.curToken.type == BlaiseLexer.GTE:
                self.expect(BlaiseLexer.GTE)
            else:
                self.error("Error: unexpected token '" + self.curToken.text + "'")
            node.rhs = self.parseExpression()
        finally:
            return node

    def parseExpression(self):
        if self.err:
            return
        node = Expression()
        try:
            node.t = self.parseTerm()
            if self.curToken.type == BlaiseLexer.PLUS:
                node.op = self.curToken.text
                self.expect(BlaiseLexer.PLUS)
                node.e = self.parseExpression()
            elif self.curToken.type == BlaiseLexer.MINUS:
                node.op = self.curToken.text
                self.expect(BlaiseLexer.MINUS)
                node.e = self.parseExpression()
        finally:
            return node

    def parseTerm(self):
        if self.err:
            return
        node = Term()
        try:
            node.f = self.parseFactor()
            if self.curToken.type == BlaiseLexer.MULT:
                node.op = self.curToken.text
                self.expect(BlaiseLexer.MULT)
                node.t = self.parseTerm()
            elif self.curToken.type == BlaiseLexer.DIV:
                node.op = self.curToken.text
                self.expect(BlaiseLexer.DIV)
                node.t = self.parseTerm()
        finally:
            return node

    def parseFactor(self):
        if self.err:
            return
        node = Factor()
        try:
            if self.curToken.type == BlaiseLexer.ID:
                node.id = self.curToken.text
                self.expect(BlaiseLexer.ID)
            elif self.curToken.type == BlaiseLexer.NUMBER:
                node.num = self.curToken.text
                self.expect(BlaiseLexer.NUMBER)
            elif self.curToken.type == BlaiseLexer.LPAREN:
                node.f = self.parseParenthesisFactor()
            else:
                self.error("Error: unexpected token '" + self.curToken.text + "'")
        finally:
            return node

    def parseParenthesisFactor(self):
        if self.err:
            return
        node = ParenthesisFactor()
        try:
            self.expect(BlaiseLexer.LPAREN)
            node.e = self.parseExpression()
            self.expect(BlaiseLexer.RPAREN)
        finally:
            return node
