from asts import AbstractVisitor

class Project4Visitor(AbstractVisitor):
    label_inc = -1
    fields = []
    methods = []
    name_space = []

    ids_set = {}

    syms_table = None

    def getLabel(self):
        self.label_inc += 1
        return "L" + str(self.label_inc)

    def newNameSpace(self, name):
        self.name_space.append(name+"_")

    def removeNameSpace(self):
        self.name_space = self.name_space[:-1]

    def getname(self, id):
        ret = ""
        scope, id = self.syms_table.lookup4(id)
        for i in scope:
            ret = ret + i
        return ret + id

    def transop(self, op, label = None):
        # when it's a comparison
        if label:
            if op == '<>':
                return '   if_icmpeq ' + label + '\n'
            if op == '=':
                return '   if_icmpne ' + label + '\n'
            if op == '<':
                return '   if_icmpge ' + label + '\n'
            if op == '>':
                return '   if_icmple ' + label + '\n'
            if op == '<=':
                return '   if_icmpgt ' + label + '\n'
            if op == '>=':
                return '   if_icmplt ' + label + '\n'
            
        # when it's math
        if op == '+':
            return '   iadd' + '\n'
        if op == '-':
            return '   isub' + '\n'
        if op == '/':
            return '   idiv' + '\n'
        if op == '*':
            return '   imul' + '\n'
            
        # if for some reason none of the code above works, return nothing.
        return None
        

    def generateMethod(self, name, args, body):
        ret = ".method static public " + name + " : (" + args + ")V\n"
        ret = ret + ".code stack 32 locals 32\n"
        ret = ret + body
        ret = ret + "   return\n"
        ret = ret + ".end code\n"
        return ret + ".end method\n\n"

    def generateClass(self, body):
        ret = ".version 59 0\n.class super Blaise\n.super java/lang/Object\n\n.method public <init> : ()V\n.code stack 1 locals 1\n   aload_0\n   invokespecial Method java/lang/Object <init> ()V\n   return\n.end code\n.end method\n\n"
        return ret + body + ".sourcefile 'Blaise.java'\n.end class"

    def visitProgram(self, node, arg=None):
        self.syms_table = arg
        body = self.visitBlock(node.b)
        c1 = ""
        for f in self.fields:
            c1 = c1 + f
        if len(c1) > 0:
            c1 = c1 + "\n"
        for m in self.methods:
            c1 = c1 + m
        c1 = c1 + self.generateMethod("main", "[Ljava/lang/String;", body)
        return self.generateClass(c1)

    def visitBlock(self, node, arg=None):
        if node.vars:
            self.visitVariables(node.vars)
        if node.procs:
            self.visitProcedures(node.procs)
        return self.visitStatement(node.s)

    def visitVariables(self, node, arg=None):
        for var in node.vars:
            self.visitVariableDeclaration(var)
        return ""

    def visitVariableDeclaration(self, node, arg=None):
        self.syms_table.bind(node.id, node.id)
        self.fields.append(".field static public " + self.getname(node.id) + " I\n")
        return ""

    def visitProcedures(self, node, arg=None):
        for p in node.procs:
            self.visitProcedureDeclaration(p)
        return ""

    def visitProcedureDeclaration(self, node, arg=None):
        self.newNameSpace(node.id)
        new_name_space = []
        for name in self.name_space:
            new_name_space.append(name)

        self.syms_table = self.syms_table.enter(new_name_space)

        if node.params:
            self.visitFormalParameters(node.params)
        c1 = ""
        args = ""
        if node.params:
            for i in range(len(node.params.params)):
                args = args + "I"
                c1 = c1 + "   iload_" + str(i) + "\n"
                c1 = c1 + "   putstatic Blaise "+ self.getname(node.params.params[i].id) + " I\n"
        block_str = self.visitBlock(node.b)
        self.removeNameSpace()
        self.syms_table = self.syms_table.exit()
        self.syms_table.bind(node.id,node.id)
        scope, b = self.syms_table.lookup4(node.id)
        self.methods.append(self.generateMethod(self.getname(node.id), args, c1 + block_str))
        return ""

    def visitFormalParameters(self, node, arg=None):
        for param in node.params:
                self.visitVariableDeclaration(param)
        return ""

    def visitAssignmentStatement(self, node, arg=None):
        return self.visitExpression(node.e) + "   putstatic Blaise " + self.getname(node.id) + " I\n"

    def visitCallStatement(self, node, arg=None):
        c1 = ""
        if node.params:
            c1 = self.visitActualParameters(node.params)
        if node.id == "out":
            return "   getstatic java/lang/System " + "out Ljava/io/PrintStream;\n" + c1 + "   invokevirtual " + "java/io/PrintStream println " +  "(I)V\n"
        else:
            args = ""
            if node.params:
                for e in node.params.params:
                    args = args + "I"
            return c1 + "   invokestatic Blaise " + self.getname(node.id) + " (" + args + ")V\n"

    def visitActualParameters(self, node, arg=None):
        c1 = ""
        for param in node.params:
            c1 = c1 + self.visitExpression(param)
        return c1

    def visitStatement(self, node, arg=None):
        if node.assign:
            return self.visitAssignmentStatement(node.assign)
        elif node.call:
            return self.visitCallStatement(node.call)
        elif node.compound:
            return self.visitCompoundStatement(node.compound)
        elif node.ifs:
            return self.visitIfStatement(node.ifs)
        elif node.whiles:
            return self.visitWhileStatement(node.whiles)

    def visitCompoundStatement(self, node, arg=None):
        c1 = self.visitStatement(node.stats[0])
        for state in node.stats[1:]:
            c1 = c1 + self.visitStatement(state)
        return c1

    def visitIfStatement(self, node, arg=None):
        L1 = self.getLabel()
        L2 = self.getLabel()
        c1 = self.visitCondition(node.c, L1)
        c2 = self.visitStatement(node.t)
        c3 = self.visitStatement(node.f)
        return c1 + c2 + "   goto " + L2 + "\n" + ".stack same\n" + L1 + ":\n" + c3 + ".stack same\n" + L2 + ":\n"

    def visitWhileStatement(self, node, arg=None):
        L1 = self.getLabel()
        L2 = self.getLabel()
        c1 = self.visitCondition(node.c, L2)
        c2 = self.visitStatement(node.s)
        return ".stack same\n" + L1 + ":\n" + c1 + c2 + "   goto " + L1 + "\n" + ".stack same\n" + L2 + ":\n"

    def visitCondition(self, node, arg=None):
        return self.visitExpression(node.lhs) + self.visitExpression(node.rhs) + self.transop(node.op, arg)

    def visitExpression(self, node, arg=None):
        c1 = self.visitTerm(node.t)
        if node.e:
            c1 = c1 + self.visitExpression(node.e)
            c1 = c1 + self.transop(node.op)
        return c1

    def visitTerm(self, node, arg=None):
        c1 = self.visitFactor(node.f)
        if node.t:
            c1 = c1 + self.visitTerm(node.t)
            c1 = c1 + self.transop(node.op)
        return c1

    def visitFactor(self, node, arg=None):
        if node.id:
            return "   getstatic Blaise " + self.getname(node.id) + " I\n"
        elif node.num:
            return "   ldc " + node.num + "\n"
        elif node.f:
            return self.visitExpression(node.f.e)
