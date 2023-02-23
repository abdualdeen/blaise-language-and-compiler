from asts import AbstractVisitor




class Project2Visitor(AbstractVisitor):
    print_flag = True
    def printIndent(self, depth):
        for i in range(depth):
            print("    ", end='')
            
    def getDepth(self, node, count) -> int:
        if node != None:
            return self.getDepth(node.parent, count+1)
        else:
            return count

    def print_node(self, node):
        if node.error and self.print_flag:
            print("Error: unexpected token '" + node.token.text + "'")
            self.print_flag = False
        if self.print_flag:
            self.printIndent(self.getDepth(node.parent, 0))
            print(node.returnExpressionName())

    def visitTerminalNode(self, node):
        if node.error and self.print_flag:
            print("Error: unexpected token '" + node.token.text + "'")
            self.print_flag = False
            
    def visitProgramNode(self, node):
        self.print_node(node)
        
    def visitBlockNode(self, node):
        self.print_node(node)
    
    def visitVariablesNode(self, node):
        self.print_node(node)
    
    def visitVariableDeclarationNode(self, node):
        self.print_node(node)
    
    def visitProceduresNode(self, node):
        self.print_node(node)
    
    def visitProcedureDeclarationNode(self, node):
        self.print_node(node)
    
    def visitFormalParametersNode(self, node):
        self.print_node(node)
    
    def visitStatemendNode(self, node):
        self.print_node(node)
    
    def visitAssignmentStatementNode(self, node):
        self.print_node(node)
    
    def visitCallStatementNode(self, node):
        self.print_node(node)
    
    def visitActualParametersNode(self, node):
        self.print_node(node)
    
    def visitCompoundStatementNode(self, node):
        self.print_node(node)
    
    def visitIfStatementNode(self, node):
        self.print_node(node)
    
    def visitWhileStatementNode(self, node):
        self.print_node(node)
    
    def visitConditionNode(self, node):
        self.print_node(node)
    
    def visitExpressionNode(self, node):
        self.print_node(node)
    
    def visitTermNode(self, node):
        self.print_node(node)
    
    def visitFactorNode(self, node):
        self.print_node(node)
    
    def visitParenthesisFactorNode(self, node):
        self.print_node(node)
