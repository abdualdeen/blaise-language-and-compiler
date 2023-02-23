from asts import AbstractVisitor
from syms import Bool, Int, BindingList, Procedure


class Project3Visitor(AbstractVisitor):
    def error(self, err):
        raise Exception(err)

    def getname(self, node):
        return node.id

    def visitProgram(self, node, syms):
        if node.b:
            return node.b.accept(self, syms)
        return None

    def visitBlock(self, node, syms):
        if node.vars:
            node.vars.accept(self, syms)
        if node.procs:
            node.procs.accept(self, syms)
        if node.s:
            return node.s.accept(self, syms)
        return None

    def visitVariables(self, node, syms):
        if node.vars:
            for v in node.vars:
                if v:
                    v.accept(self, syms)
        return None

    def visitVariableDeclaration(self, node, syms):
        name = self.getname(node)
        syms.bind(name, Int())
        return syms.lookup(name)

    def visitProcedures(self, node, syms):
        if node.procs:
            for p in node.procs:
                if p:
                    p.accept(self, syms)
        return None

    def visitProcedureDeclaration(self, node, syms):
        sym = syms.enter()

        if node.params:
            lst = node.params.accept(self, sym)
        else:
            lst = BindingList()

        name = self.getname(node)
        syms.bind(name, Procedure(lst))

        if node.b:
            node.b.accept(self, sym)

        syms = sym.exit()
        return syms.lookup(name)

    def visitFormalParameters(self, node, syms):
        lst = BindingList()
        if node.params:
            for p in node.params:
                if p:
                    lst.bindings.append(p.accept(self, syms))
        return lst

    def visitStatement(self, node, syms):
        if node.assign:
            return node.assign.accept(self, syms)
        if node.call:
            return node.call.accept(self, syms)
        if node.compound:
            return node.compound.accept(self, syms)
        if node.ifs:
            return node.ifs.accept(self, syms)
        if node.whiles:
            return node.whiles.accept(self, syms)
        return None

    def visitAssignmentStatement(self, node, syms):
        t1 = syms.lookup(self.getname(node))
        if t1 is None:
            self.error(node.id + ' undeclared')
        if isinstance(t1, Procedure):
            self.error(node.id + ' can not be assigned to, as it is a procedure')
        t2 = None
        if node.e:
            t2 = node.e.accept(self, syms)
        if t1 != t2:
            self.error(node.id + ' has type ' + str(t1) + ' but trying to assign type ' + str(t2))
        return t1

    def visitCallStatement(self, node, syms):
        name = self.getname(node)
        t = syms.lookup(name)
        if not isinstance(t, Procedure):
            self.error(node.id + ' not a procedure')
        if node.params:
            lst = node.params.accept(self, syms)
            if len(lst.bindings) != len(t.lst.bindings):
                self.error('procedure ' + node.id + ' requires ' + str(len(t.lst.bindings)) +
                           ' parameters but given ' + str(len(lst.bindings)))
            for i in range(0, len(t.lst.bindings)):
                if t.lst.bindings[i] != lst.bindings[i]:
                    self.error('argument type does not match')
            return t
        return None

    def visitActualParameters(self, node, syms):
        lst = BindingList()
        if node.params:
            for e in node.params:
                if e:
                    lst.bindings.append(e.accept(self, syms))
        return lst

    def visitCompoundStatement(self, node, syms):
        t = None
        if node.stats:
            for s in node.stats:
                if s:
                    t = s.accept(self, syms)
        return t

    def visitIfStatement(self, node, syms):
        if node.c:
            t1 = node.c.accept(self, syms)
            if not isinstance(t1, Bool):
                self.error('condition must be boolean')
            t2 = None
            if node.t:
                t2 = node.t.accept(self, syms)
            if node.f:
                node.f.accept(self, syms)
            return t2
        return None

    def visitWhileStatement(self, node, syms):
        if node.c:
            node.c.accept(self, syms)
        if node.s:
            node.s.accept(self, syms)
        if node.c:
            t1 = node.c.accept(self, syms)
            if not isinstance(t1, Bool):
                self.error('condition must be boolean')
            if node.s:
                return node.s.accept(self, syms)
        return None

    def visitCondition(self, node, syms):
        if node.lhs:
            t1 = node.lhs.accept(self, syms)
            t2 = None
            if node.rhs:
                t2 = node.rhs.accept(self, syms)
            if t1 != t2:
                self.error('operands not same type')
            if not isinstance(t1, Int):
                self.error('operands must be int')
            return Bool()
        return None

    def visitExpression(self, node, syms):
        if node.t:
            t1 = node.t.accept(self, syms)
            if node.e:
                t2 = node.e.accept(self, syms)
                if t1 != t2:
                    self.error('operands not same type')
                if not isinstance(t1, Int):
                    self.error('operands must be int')
            return t1
        return None

    def visitTerm(self, node, syms):
        if node.f:
            t1 = node.f.accept(self, syms)
            if node.t:
                t2 = node.t.accept(self, syms)
                if t1 != t2:
                    self.error('operands not same type')
                if not isinstance(t1, Int):
                    self.error('operands must be int')
            return t1
        return None

    def visitFactor(self, node, syms):
        if node.f:
            return node.f.accept(self, syms)
        if node.id:
            name = self.getname(node)
            b = syms.lookup(name)
            if b:
                return b
            self.error(node.id + ' undeclared')
        if node.num:
            return Int()
        return None

    def visitParenthesisFactor(self, node, syms):
        if node.e:
            return node.e.accept(self, syms)
        return None
