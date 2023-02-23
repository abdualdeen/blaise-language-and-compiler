class AbstractNode:
    def accept(self, v, arg):
        pass


class AbstractVisitor:
    def visitProgram(self, node, arg):
        if node.b:
            node.b.accept(self, arg)

    def visitBlock(self, node, arg):
        if node.vars:
            node.vars.accept(self, arg)
        if node.procs:
            node.procs.accept(self, arg)
        if node.s:
            node.s.accept(self, arg)

    def visitVariables(self, node, arg):
        if node.vars:
            for d in node.vars:
                if d:
                    d.accept(self, arg)

    def visitVariableDeclaration(self, node, arg):
        pass

    def visitProcedures(self, node, arg):
        if node.procs:
            for d in node.procs:
                if d:
                    d.accept(self, arg)

    def visitProcedureDeclaration(self, node, arg):
        if node.params:
            node.params.accept(self, arg)
        if node.b:
            node.b.accept(self, arg)

    def visitFormalParameters(self, node, arg):
        if node.params:
            for p in node.params:
                if p:
                    p.accept(self, arg)

    def visitStatement(self, node, arg):
        if node.assign:
            node.assign.accept(self, arg)
        if node.call:
            node.call.accept(self, arg)
        if node.compound:
            node.compound.accept(self, arg)
        if node.ifs:
            node.ifs.accept(self, arg)
        if node.whiles:
            node.whiles.accept(self, arg)

    def visitAssignmentStatement(self, node, arg):
        if node.e:
            node.e.accept(self, arg)

    def visitCallStatement(self, node, arg):
        if node.params:
            node.params.accept(self, arg)

    def visitCompoundStatement(self, node, arg):
        if node.stats:
            for s in node.stats:
                if s:
                    s.accept(self, arg)

    def visitIfStatement(self, node, arg):
        if node.c:
            node.c.accept(self, arg)
        if node.t:
            node.t.accept(self, arg)
        if node.f:
            node.f.accept(self, arg)

    def visitWhileStatement(self, node, arg):
        if node.c:
            node.c.accept(self, arg)
        if node.s:
            node.s.accept(self, arg)

    def visitActualParameters(self, node, arg):
        if node.params:
            for e in node.params:
                if e:
                    e.accept(self, arg)

    def visitCondition(self, node, arg):
        if node.lhs:
            node.lhs.accept(self, arg)
        if node.rhs:
            node.rhs.accept(self, arg)

    def visitExpression(self, node, arg):
        if node.t:
            node.t.accept(self, arg)
        if node.e:
            node.e.accept(self, arg)

    def visitTerm(self, node, arg):
        if node.f:
            node.f.accept(self, arg)
        if node.t:
            node.t.accept(self, arg)

    def visitFactor(self, node, arg):
        if node.f:
            node.f.accept(self, arg)

    def visitParenthesisFactor(self, node, arg):
        if node.e:
            node.e.accept(self, arg)


class ActualParameters(AbstractNode):
    def __init__(self):
        self.params = []

    def accept(self, v, arg):
        return v.visitActualParameters(self, arg)


class AssignmentStatement(AbstractNode):
    def __init__(self):
        self.id = None
        self.e = None

    def accept(self, v, arg):
        return v.visitAssignmentStatement(self, arg)


class Block(AbstractNode):
    def __init__(self):
        self.vars = None
        self.procs = None
        self.s = None

    def accept(self, v, arg):
        return v.visitBlock(self, arg)


class CallStatement(AbstractNode):
    def __init__(self):
        self.id = None
        self.params = None

    def accept(self, v, arg):
        return v.visitCallStatement(self, arg)


class CompoundStatement(AbstractNode):
    def __init__(self):
        self.stats = []

    def accept(self, v, arg):
        return v.visitCompoundStatement(self, arg)


class Condition(AbstractNode):
    def __init__(self):
        self.lhs = None
        self.op = None
        self.rhs = None

    def accept(self, v, arg):
        return v.visitCondition(self, arg)


class Expression(AbstractNode):
    def __init__(self):
        self.t = None
        self.op = None
        self.e = None

    def accept(self, v, arg):
        return v.visitExpression(self, arg)


class Factor(AbstractNode):
    def __init__(self):
        self.id = None
        self.num = None
        self.f = None

    def accept(self, v, arg):
        return v.visitFactor(self, arg)


class FormalParameters(AbstractNode):
    def __init__(self):
        self.params = []

    def accept(self, v, arg):
        return v.visitFormalParameters(self, arg)


class IfStatement(AbstractNode):
    def __init__(self):
        self.c = None
        self.t = None
        self.f = None

    def accept(self, v, arg):
        return v.visitIfStatement(self, arg)


class ParenthesisFactor(AbstractNode):
    def __init__(self):
        self.e = None

    def accept(self, v, arg):
        return v.visitParenthesisFactor(self, arg)


class ProcedureDeclaration(AbstractNode):
    def __init__(self):
        self.id = None
        self.params = None
        self.b = None

    def accept(self, v, arg):
        return v.visitProcedureDeclaration(self, arg)


class Procedures(AbstractNode):
    def __init__(self):
        self.procs = []

    def accept(self, v, arg):
        return v.visitProcedures(self, arg)


class Program(AbstractNode):
    def __init__(self):
        self.b = None

    def accept(self, v, arg):
        return v.visitProgram(self, arg)


class Statement(AbstractNode):
    def __init__(self):
        self.assign = None
        self.call = None
        self.compound = None
        self.ifs = None
        self.whiles = None

    def accept(self, v, arg):
        return v.visitStatement(self, arg)


class Term(AbstractNode):
    def __init__(self):
        self.f = None
        self.op = None
        self.t = None

    def accept(self, v, arg):
        return v.visitTerm(self, arg)


class VariableDeclaration(AbstractNode):
    def __init__(self):
        self.id = None

    def accept(self, v, arg):
        return v.visitVariableDeclaration(self, arg)


class Variables(AbstractNode):
    def __init__(self):
        self.vars = []

    def accept(self, v, arg):
        return v.visitVariables(self, arg)


class WhileStatement(AbstractNode):
    def __init__(self):
        self.c = None
        self.s = None

    def accept(self, v, arg):
        return v.visitWhileStatement(self, arg)
