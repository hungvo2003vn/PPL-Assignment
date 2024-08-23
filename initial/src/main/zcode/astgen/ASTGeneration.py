from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *
from functools import reduce

class ASTGeneration(ZCodeVisitor):
    # program: NEWLINE* list_declared EOF;
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.list_declared()))


    # list_declared: declared list_declared | declared;
    def visitList_declared(self, ctx:ZCodeParser.List_declaredContext):
        if ctx.list_declared():
            return [self.visit(ctx.declared())] + self.visit(ctx.list_declared())
        return [self.visit(ctx.declared())]


    # declared:  function | variables ignore;
    def visitDeclared(self, ctx:ZCodeParser.DeclaredContext):
        return self.visit(ctx.getChild(0))


    # variables: implicit_var | keyword_var | implicit_dynamic; 
    def visitVariables(self, ctx:ZCodeParser.VariablesContext):
        return self.visit(ctx.getChild(0))


    # implicit_var: VAR ID ASSIGN expression;
    def visitImplicit_var(self, ctx:ZCodeParser.Implicit_varContext):
        return VarDecl( Id(ctx.ID().getText()), None , "var", self.visit(ctx.expression()))


    # keyword_var: prim_type (ID | array_declared) (ASSIGN expression)?;
    def visitKeyword_var(self, ctx:ZCodeParser.Keyword_varContext):

        name = None
        typ = self.visit(ctx.prim_type())
        if ctx.ID():

            name = Id(ctx.ID().getText())

        elif ctx.array_declared():

            res = self.visitArray_declared(ctx.array_declared())
            name = res["ID"]

            res["typ"].eleType = typ
            typ = res["typ"]

        if ctx.getChildCount() == 4:
            return VarDecl(name, typ, None, self.visit(ctx.expression()))

        return VarDecl(name, typ)


    # implicit_dynamic: DYNAMIC ID (ASSIGN expression)?;
    def visitImplicit_dynamic(self, ctx:ZCodeParser.Implicit_dynamicContext):

        if ctx.getChildCount() == 4:
            return VarDecl(Id(ctx.ID().getText()), None, "dynamic", self.visit(ctx.expression()))
        
        return VarDecl(Id(ctx.ID().getText()), None, "dynamic")


    # prim_type: BOOL | NUMBER | STRING;
    def visitPrim_type(self, ctx:ZCodeParser.Prim_typeContext):

        if ctx.BOOL():
            return BoolType()
        elif ctx.NUMBER():
            return NumberType()
        return StringType()


    # array_declared: ID (LBRACKET list_NUMBER_LIT RBRACKET);
    def visitArray_declared(self, ctx:ZCodeParser.Array_declaredContext):

        arr_ID = Id(ctx.ID().getText())
        arr_dimensions = self.visit(ctx.list_NUMBER_LIT())

        return {
            "ID": arr_ID,
            "typ": ArrayType(arr_dimensions, None)
        }


    # list_NUMBER_LIT: NUMBER_LIT (COMMA list_NUMBER_LIT) | NUMBER_LIT;
    def visitList_NUMBER_LIT(self, ctx:ZCodeParser.List_NUMBER_LITContext):
        if ctx.list_NUMBER_LIT():
            return [float(ctx.NUMBER_LIT().getText())] + self.visit(ctx.list_NUMBER_LIT())
        return [float(ctx.NUMBER_LIT().getText())]


    # function: FUNC ID LPARENT prameters_list? RPARENT (ignore? return_statement | ignore? block_statement | ignore);
    def visitFunction(self, ctx:ZCodeParser.FunctionContext):
        params = [] if not ctx.prameters_list() else self.visit(ctx.prameters_list())
        
        stmt = None
        if ctx.return_statement():
            stmt = self.visit(ctx.return_statement())
        elif ctx.block_statement():
            stmt = self.visit(ctx.block_statement())

        return FuncDecl(Id(ctx.ID().getText()), params, stmt)


    # prameters_list: prim_type (ID | array_declared) COMMA prameters_list
	#			| prim_type (ID | array_declared);
    def visitPrameters_list(self, ctx:ZCodeParser.Prameters_listContext):
       
        name = None
        typ = self.visit(ctx.prim_type())
        if ctx.ID():
            name = Id(ctx.ID().getText())
        elif ctx.array_declared():

            res = self.visitArray_declared(ctx.array_declared())
            name = res["ID"]

            res["typ"].eleType = typ
            typ = res["typ"]
        keyword_var = VarDecl(name, typ)

        if ctx.prameters_list():
            return [keyword_var] + self.visit(ctx.prameters_list())
        return [keyword_var]


    # statement_list: statement statement_list | ;
    def visitStatement_list(self, ctx:ZCodeParser.Statement_listContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.statement())] + self.visit(ctx.statement_list())


    # statement: declaration_statement | assignment_statement 
    #        | if_statement | for_statement 
    #        | break_statement | continue_statement 
    #        | return_statement  | call_statement | block_statement;
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visit(ctx.getChild(0))


    # declaration_statement: variables ignore;
    def visitDeclaration_statement(self, ctx:ZCodeParser.Declaration_statementContext):
        return self.visit(ctx.variables())


    # assignment_statement: (ID | ID index_operators) ASSIGN expression ignore;
    def visitAssignment_statement(self, ctx:ZCodeParser.Assignment_statementContext):
        
        lhs = None
        if ctx.index_operators():
            lhs = ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.index_operators()))
        else:
            lhs = Id(ctx.ID().getText())

        return Assign(lhs, self.visit(ctx.expression()))


    # if_statement: (IF LPARENT expression RPARENT statement_block_if) elif_statement_list else_statement;
    def visitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        
        cond = self.visit(ctx.expression())
        tstmt = self.visit(ctx.statement_block_if())
        Elif = self.visit(ctx.elif_statement_list())
        fstmt = self.visit(ctx.else_statement())

        return If(cond, tstmt, Elif, fstmt)


    # elif_statement: ELIF LPARENT expression RPARENT statement_block_if;
    def visitElif_statement(self, ctx:ZCodeParser.Elif_statementContext):
        return tuple([self.visit(ctx.expression()), self.visit(ctx.statement_block_if())])

    # elif_statement_list: elif_statement elif_statement_list | ;
    def visitElif_statement_list(self, ctx:ZCodeParser.Elif_statement_listContext):
        
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.elif_statement())] + self.visit(ctx.elif_statement_list())


    # else_statement: ELSE statement_block_if | ;
    def visitElse_statement(self, ctx:ZCodeParser.Else_statementContext):
        return None if (not ctx.statement_block_if()) else self.visit(ctx.statement_block_if())


    # statement_block_if: (ignore? statement);
    def visitStatement_block_if(self, ctx:ZCodeParser.Statement_block_ifContext):
        return self.visit(ctx.statement())

    # for_statement: FOR ID UNTIL expression BY expression (ignore? statement);
    def visitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        
        init = Id(ctx.ID().getText())
        cond = self.visit(ctx.expression(0))
        upd = self.visit(ctx.expression(1))
        stmt = self.visit(ctx.statement())

        return For(init, cond, upd, stmt)

    # break_statement: BREAK ignore;
    def visitBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        return Break()


    # continue_statement: CONTINUE ignore;
    def visitContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        return Continue()


    # return_statement: RETURN (expression | ) ignore;
    def visitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        expr = None if not ctx.expression() else self.visit(ctx.expression()) 
        return Return(expr)

    # call_statement: func_call ignore;
    def visitCall_statement(self, ctx:ZCodeParser.Call_statementContext):
        res = self.visit(ctx.func_call())
        return CallStmt(res.name, res.args)

    # func_call: ID (LPARENT expression_list? RPARENT);
    def visitFunc_call(self, ctx:ZCodeParser.Func_callContext):
        args = [] if not ctx.expression_list() else self.visit(ctx.expression_list())
        name  = Id(ctx.ID().getText())
        return CallExpr(name, args)

    # block_statement: BEGIN ignore statement_list END ignore;
    def visitBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        return Block(self.visit(ctx.statement_list()))

    # expression_list: expression COMMA expression_list | expression;
    def visitExpression_list(self, ctx:ZCodeParser.Expression_listContext):
        
        if not ctx.expression_list():
            return [self.visit(ctx.expression())]
        return [self.visit(ctx.expression())] + self.visit(ctx.expression_list())

    # expression: expression1 CONCAT expression1 | expression1;
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):

        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression1(0))

        op = ctx.CONCAT().getText()
        left = self.visit(ctx.expression1(0))
        right = self.visit(ctx.expression1(1))

        return BinaryOp(op, left, right)


    # expression1: expression2 (EQUAL | STRCMP | NOT_EQUAL | LT | GT | LE | GE) expression2 | expression2;
    def visitExpression1(self, ctx:ZCodeParser.Expression1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression2(0))

        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expression2(0))
        right = self.visit(ctx.expression2(1))

        return BinaryOp(op, left, right)

    # expression2: expression2 (AND | OR) expression3 | expression3;
    def visitExpression2(self, ctx:ZCodeParser.Expression2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression3())

        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expression2())
        right = self.visit(ctx.expression3())

        return BinaryOp(op, left, right)


    # expression3: expression3 (ADD | SUB) expression4 | expression4;
    def visitExpression3(self, ctx:ZCodeParser.Expression3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression4())

        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expression3())
        right = self.visit(ctx.expression4())

        return BinaryOp(op, left, right)


    # expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
    def visitExpression4(self, ctx:ZCodeParser.Expression4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression5())

        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expression4())
        right = self.visit(ctx.expression5())

        return BinaryOp(op, left, right)


    # expression5: NOT expression5 | expression6;
    def visitExpression5(self, ctx:ZCodeParser.Expression5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression6())
        
        op = ctx.getChild(0).getText()
        val = self.visit(ctx.expression5())

        return UnaryOp(op, val)


    # expression6: SUB expression6 | expression7;
    def visitExpression6(self, ctx:ZCodeParser.Expression6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression7())
        
        op = ctx.getChild(0).getText()
        val = self.visit(ctx.expression6())

        return UnaryOp(op, val)


    # expression7: array_element | literal | ID | (LPARENT expression RPARENT) | func_call;
    def visitExpression7(self, ctx:ZCodeParser.Expression7Context):
        
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.expression():
            return self.visit(ctx.expression())
        else:
            return self.visit(ctx.getChild(0))


    # literal: NUMBER_LIT | STRING_LIT | TRUE | FALSE | array_literal;
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        if ctx.NUMBER_LIT():
            return NumberLiteral(float(ctx.NUMBER_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        
        return self.visit(ctx.array_literal())


    # array_literal: LBRACKET expression_list RBRACKET;
    def visitArray_literal(self, ctx:ZCodeParser.Array_literalContext):
        return ArrayLiteral(self.visit(ctx.expression_list()))


    # array_element: (ID | func_call) index_operators;
    def visitArray_element(self, ctx:ZCodeParser.Array_elementContext):
        name = Id(ctx.ID().getText()) if ctx.ID() else self.visit(ctx.func_call())
        cell = self.visit(ctx.index_operators())

        return ArrayCell(name, cell)

    # index_operators: (LBRACKET expression_list RBRACKET);
    def visitIndex_operators(self, ctx:ZCodeParser.Index_operatorsContext):
        return self.visit(ctx.expression_list())


    # Visit a parse tree produced by ZCodeParser#ignore.
    def visitIgnore(self, ctx:ZCodeParser.IgnoreContext):
        return None