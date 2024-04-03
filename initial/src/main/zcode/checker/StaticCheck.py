from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class Zcode:
    pass

class FuncZcode(Zcode):
    def __init__(self, param = [], typ = None, body = False):
        self.param = param
        self.typ = typ
        self.body = body

class VarZcode(Zcode):
    def __init__(self, typ = None):
        self.typ = typ    


class StaticChecker(BaseVisitor, Utils):
    def __init__(self,ast, ):
        self.ast = ast
        self.BlockFor = 0
        self.function = None
        self.Return = False
        self.listFunction = [{
                "readNumber" : FuncZcode([], NumberType(), True),
                "readBool" : FuncZcode([], BoolType(), True),
                "readString" : FuncZcode([], StringType(), True),
                "writeNumber" : FuncZcode([NumberType()], VoidType(), True),
                "writeBool" : FuncZcode([BoolType()], VoidType(), True),
                "writeString" : FuncZcode([StringType()], VoidType(), True)
                }]
        
    def check(self):
        self.visit(self.ast, [{}])
        return None
    
    def comparType(self, LHS, RHS):
        #TODO: so sánh 2 biến type, kiểm tra array type sẽ kiểm tra size và eletype 
           
        if isinstance(LHS, ArrayType) and isinstance(RHS, ArrayType):
            return type(LHS.eleType) == type(RHS.eleType) and LHS.size == RHS.size
        else:
            return type(LHS) == type(RHS)

    def comparListType(self, LHS, RHS):
        #TODO: so sánh 2 list type, kiểm tra về độ dài và thứ tự của type trong đó
           
        if len(LHS) != len(RHS):
            return False

        for lhs_item, rhs_item in zip(LHS, RHS):
            if not self.comparType(lhs_item, rhs_item):
                return False

        return True
    
    def visitProgram(self, ast, param):
        #! duyệt qua các biến và hàm toàn cục
        for decl in ast.decl: self.visit(decl, param)
        
        #TODO check No definition for a function in param
        for decl_name, decl_desciption in self.listFunction[0].items():
            if not decl_desciption.body: raise NoDefinition(decl_name)
            
        #TODO  check No entry point in param
        main_func = self.listFunction[0].get('main')
        if (main_func is None) or (len(main_func.param) > 0) or (type(main_func.typ) != VoidType): 
            raise NoEntryPoint()

        return

    def visitVarDecl(self, ast, param):
        #TODO kiểm tra name có trong param[0] hay không nén ra lỗi Redeclared
        if param[0].get(ast.name.name) is not None: raise Redeclared(Variable(), ast.name.name)
        param[0][ast.name.name] = VarZcode(ast.varType)

        #TODO kiểm tra TypeCannotBeInferred và TypeMismatchInStatement xử lí ast.varInit nếu tồn tại
        if ast.varInit:
            LHS = self.visit(ast.varType, param) if ast.varType else param[0][ast.name.name]
            RHS = self.visit(ast.varInit, param)

            #  TH1 : cả 2 đều trả về Zcode -> TypeCannotBeInferred
            if isinstance(LHS, Zcode) and isinstance(RHS, Zcode):
                raise TypeCannotBeInferred(stmt=ast)
            # TH2, 3: nếu 1 trong 2 bên trả về Zcode bên kia xác định type thì gán type của Zcode với type đó
            elif not isinstance(LHS, Zcode) and isinstance(RHS, Zcode):
                RHS.typ = LHS
            elif isinstance(LHS, Zcode) and not isinstance(RHS, Zcode):
                LHS.typ = RHS
            # TH4 : cả 2 đều có type nên kiểm tra xem 2 type có giống nhau không
            elif not self.comparType(LHS, RHS):
                raise TypeMismatchInStatement(stmt=ast)
            
        return param

    def visitFuncDecl(self, ast, param):
        #TODO kiểm tra name có trong listFunction hay không nén ra lỗi Redeclared
        declared_function = self.listFunction[0].get(ast.name.name)
        
        #TODO kiểm tra Param trong hàm
        listParam = {} #! dạng Dict có name
        typeParam = [] #! dạng mảng không cần name
        for funcParam in ast.param:
            id = funcParam.name.name
            if listParam.get(id): raise Redeclared(Parameter(), id)
            # Update list param
            listParam[id] = VarZcode(funcParam.varType)
            typeParam += [funcParam.varType]
        
        self.Return = False
        body = True if ast.body else False

        #TODO chia làm 3 TH
        if declared_function:
            #* TH 1: là method đã so sẵn nghĩa là được khai báo 1 phần trước yêu cầu 
            # kiểm tra 2 list có giống nhau không nếu không nén ra Redeclared
            if not self.comparListType(typeParam, declared_function.param): 
                raise Redeclared(Function(), ast.name.name)
        
            #* TH2 : method tồn tại trước và khai báo 1 phần    
            elif not ast.body:
                raise Redeclared(Function(), ast.name.name)
            
            #* TH 3: là khai báo toàn bộ
            elif declared_function.body:
                raise Redeclared(Function(), ast.name.name)

            self.listFunction[0][ast.name.name].param = typeParam
            self.listFunction[0][ast.name.name].body = body

        else:
            
            self.listFunction[0][ast.name.name] = FuncZcode(typeParam, None, body)
            

        if ast.body:

            self.function = self.listFunction[0][ast.name.name]
            self.visit(ast.body, [listParam] + param)
            self.function = None


            if not self.Return:

                #! nếu không có type khi duyệt qua body thì là voidtype
                if self.listFunction[0][ast.name.name].typ is None:
                    self.listFunction[0][ast.name.name].typ = VoidType()

                #! type đã có so sánh nó với VoidType
                elif not self.comparType(self.listFunction[0][ast.name.name].typ, VoidType()): 
                    raise TypeMismatchInStatement(Return(None))


        return self.listFunction

    def visitId(self, ast, param):
        #TODO kiểm tra xem name có trong toàn bộ param nén lỗi Undeclared
        for scope in param:
            id = scope.get(ast.name)
            if id:
                if isinstance(id, FuncZcode): raise Undeclared(Identifier(), ast.name)
                if not id.typ: return id
                else: return id.typ
        
        raise Undeclared(Identifier(), ast.name)

    def visitCallStmt(self, ast, param):
        #TODO kiểm tra xem name có trong toàn bộ listFunction nén lỗi Undeclared
        found = self.listFunction[0].get(ast.name.name)
        
        # Cannot find the function declaration
        if not found:  
            raise Undeclared(Function(), ast.name.name)
        
        listLHS = found.param
        listRHS = ast.args

        # Check param and args
        if len(listLHS) != len(listRHS):
            raise TypeMismatchInStatement(ast)
        
        for i in range(len(listLHS)):

            LHS = self.visit(listLHS[i], param)
            RHS = self.visit(listRHS[i], param)

            if isinstance(RHS, Zcode):
                RHS.typ = LHS
            elif not self.comparType(LHS, RHS):
                raise TypeMismatchInStatement(ast)

        # Check return type
        function_found = found
        if function_found.typ is None: function_found.typ = VoidType()
        elif not self.comparType(function_found.typ, VoidType()):
            raise TypeMismatchInStatement(ast)

        return function_found.typ

    def visitCallExpr(self, ast, param):
        #TODO kiểm tra xem name có trong toàn bộ listFunction nén lỗi Undeclared
        found = self.listFunction[0].get(ast.name.name)
        
        # Cannot find the function declaration
        if not found:  
            raise Undeclared(Function(), ast.name.name)
        
        listLHS = found.param
        listRHS = ast.args

        # Check param and args
        if len(listLHS) != len(listRHS):
            raise TypeMismatchInExpression(ast)
        
        for i in range(len(listLHS)):

            LHS = self.visit(listLHS[i], param)
            RHS = self.visit(listRHS[i], param)

            if isinstance(RHS, Zcode):
                RHS.typ = LHS
            elif not self.comparType(LHS, RHS):
                raise TypeMismatchInExpression(ast)

        # Check return type
        function_found = found
        if function_found.typ is None: return function_found
        if self.comparType(function_found.typ, VoidType()):
            raise TypeMismatchInExpression(ast)

        return function_found.typ


    def visitBlock(self, ast, param):
        for item in ast.stmt:
            #! trường hợp gặp block
            if type(item) is Block: self.visit(item, [{}] + param)
            else: self.visit(item, param)


    def visitFor(self, ast, param):

        #TODO Check type
        listLHS = [NumberType(), BoolType(), NumberType()]
        listRHS = [
            self.visit(ast.name, param), 
            self.visit(ast.condExpr, param),
            self.visit(ast.updExpr, param)
        ]
        
        for i in range(3):

            LHS = listLHS[i]
            RHS = listRHS[i]

            if isinstance(RHS, Zcode):
                RHS.typ = LHS
            elif not self.comparType(LHS, RHS):
                raise TypeMismatchInStatement(ast)


        self.BlockFor += 1 #! vào trong vòng for nào anh em
        self.visit(ast.body, [{}] + param)
        self.BlockFor -= 1 #! cút khỏi vòng for nào anh em
        
    def visitContinue(self, ast, param):
        #! kiểm tra đang ở vòng for hay không
        if self.BlockFor == 0: raise MustInLoop(ast)

    def visitBreak(self, ast, param):
        #! kiểm tra đang ở vòng for hay không
        if self.BlockFor == 0: raise MustInLoop(ast)


    def visitNumberType(self, ast, param): return ast
    def visitBoolType(self, ast, param): return ast
    def visitStringType(self, ast, param): return ast
    def visitArrayType(self, ast, param): return ast
    def visitNumberLiteral(self, ast, param): return NumberType()
    def visitBooleanLiteral(self, ast, param): return BoolType()
    def visitStringLiteral(self, ast, param): return StringType()
    def visitArrayLiteral(self, ast, param):

        for lit in ast.value: self.visit(lit, param)
        typ = self.visit(ast.value[0], param)

        if type(typ) in [StringType, BoolType, NumberType]:
            return ArrayType([len(ast.value)], typ)
        return ArrayType([len(ast.value)] + typ.size, typ.eleType)

    def visitBinaryOp(self, ast, param):
        LHS = self.visit(ast.left, param)
        RHS = self.visit(ast.right, param)

        type_0 = ['+', '-', '*', '/', '%']
        type_1 = ['=', '!=', '<', '>', '>=', '<=']
        type_2 = ['and', 'or']
        type_3 = ['==']
        type_4 = ['...']

        def checkTypeHelper(input_type, output_type):

            if not isinstance(LHS, Zcode) and not isinstance(RHS, Zcode):
                if not self.comparType(LHS, RHS):
                    raise TypeMismatchInExpression(ast)
                if not self.comparType(LHS, input_type) or not self.comparType(RHS, input_type):
                    raise TypeMismatchInExpression(ast)
                
            elif not isinstance(LHS, Zcode) and isinstance(RHS, Zcode):
                RHS.typ = LHS

                if not self.comparType(LHS, input_type):
                    raise TypeMismatchInExpression(ast)
                
            elif isinstance(LHS, Zcode) and not isinstance(RHS, Zcode):
                LHS.typ = RHS

                if not self.comparType(RHS, input_type):
                    raise TypeMismatchInExpression(ast)
                
            else:
                LHS.typ = input_type
                RHS.typ = input_type

            return output_type
        
        if ast.op in type_0:
            return checkTypeHelper(NumberType(), NumberType())
        elif ast.op in type_1:
            return checkTypeHelper(NumberType(), BoolType())
        elif ast.op in type_2:
            return checkTypeHelper(BoolType(), BoolType()) 
        elif ast.op in type_3:
            return checkTypeHelper(StringType(), BoolType())
        elif ast.op in type_4:
            return checkTypeHelper(StringType(), StringType())
        
        return Zcode()

    def visitUnaryOp(self, ast, param):
        
        operand = self.visit(ast.operand, param)

        type_0 = ['+', '-']
        type_1 = ['not']

        def checkTypeHelper(input_type, output_type):
            
            if isinstance(operand, Zcode):
                operand.typ = input_type
            elif not self.comparType(operand, input_type):
                raise TypeMismatchInExpression(ast)

            return output_type
        
        if ast.op in type_0:
            return checkTypeHelper(NumberType(), NumberType())
        elif ast.op in type_1:
            return checkTypeHelper(BoolType(), BoolType()) 
        
        return Zcode()

    def visitArrayCell(self, ast, param):
        
        arr = self.visit(ast.arr, param)
        #TODO Không thể suy diễn kiểu từ ArrayType nên cần hỏi thầy !!!!
        if not isinstance(arr, ArrayType):
            raise TypeMismatchInExpression(ast)
        
        # Check idx
        for index in ast.idx:
            expr = self.visit(index, param)

            if isinstance(expr, Zcode):
                expr.typ = NumberType()
            elif not self.comparType(expr, NumberType()):
                raise TypeMismatchInExpression(ast)
            
        left = len(arr.size)
        right = len(ast.idx)
        if left < right:
            raise TypeMismatchInExpression(ast)
        elif left == right:
            return arr.eleType
        elif left > right:
            return ArrayType(size=arr.size[right:], eleType=arr.eleType)

    def visitIf(self, ast, param):
        
        # Check first condition
        expr = self.visit(ast.expr, param)
        if isinstance(expr, Zcode):
            expr.typ = BoolType()
        elif not self.comparType(expr, BoolType()):
            raise TypeMismatchInStatement(ast)
        
        # visit thenStmt
        self.visit(ast.thenStmt, [{}] + param)

        # visit all elifStmt
        for ele in ast.elifStmt:

            # Check condition type
            elif_expr = self.visit(ele[0], param)

            if isinstance(elif_expr, Zcode):
                elif_expr.typ = BoolType()
            elif not self.comparType(elif_expr, BoolType()):
                raise TypeMismatchInStatement(ast)
            
            # visit stmt of elif
            self.visit(ele[1], [{}] + param)
        
        # Visit elseStmt
        if ast.elseStmt:
            self.visit(ast.elseStmt, [{}] + param)
        
        return

        

    def visitAssign(self, ast, param):
        
        LHS = self.visit(ast.lhs, param)
        RHS = self.visit(ast.rhs, param)

        # TH1 : cả 2 đều trả về Zcode -> TypeCannotBeInferred
        if isinstance(LHS, Zcode) and isinstance(RHS, Zcode):
            raise TypeCannotBeInferred(stmt=ast)
        # TH2, 3: nếu 1 trong 2 bên trả về Zcode bên kia xác định type thì gán type của Zcode với type đó
        elif not isinstance(LHS, Zcode) and isinstance(RHS, Zcode):
            RHS.typ = LHS
        elif isinstance(LHS, Zcode) and not isinstance(RHS, Zcode):
            LHS.typ = RHS
        # TH4 : cả 2 đều có type nên kiểm tra xem 2 type có giống nhau không
        elif not self.comparType(LHS, RHS):
            raise TypeMismatchInStatement(stmt=ast)

    def visitReturn(self, ast, param):

        self.Return = True
        
        LHS = None
        if self.function.typ:
            LHS = self.visit(self.function.typ, param) if not self.comparType(self.function.typ, VoidType()) else self.function.typ
        else: LHS = self.function

        RHS = self.visit(ast.expr, param) if ast.expr else VoidType()

        # TH1 : cả 2 đều trả về Zcode -> TypeCannotBeInferred
        if isinstance(LHS, Zcode) and isinstance(RHS, Zcode):
            raise TypeCannotBeInferred(stmt=ast)
        # TH2, 3: nếu 1 trong 2 bên trả về Zcode bên kia xác định type thì gán type của Zcode với type đó
        elif not isinstance(LHS, Zcode) and isinstance(RHS, Zcode):
            RHS.typ = LHS
        elif isinstance(LHS, Zcode) and not isinstance(RHS, Zcode):
            LHS.typ = RHS
        # TH4 : cả 2 đều có type nên kiểm tra xem 2 type có giống nhau không
        elif not self.comparType(LHS, RHS):
            raise TypeMismatchInStatement(stmt=ast)





