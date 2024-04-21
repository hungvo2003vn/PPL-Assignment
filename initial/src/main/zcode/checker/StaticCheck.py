from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class Zcode(Type):
    pass

class FuncZcode(Zcode):
    def __init__(self, param = [], typ = None, body = False):
        self.param = param
        self.typ = typ
        self.body = body

class VarZcode(Zcode):
    def __init__(self, typ = None):
        self.typ = typ    

class ArrayZcode(Type):
    #* eleType: List[Type]
    #* Type can be Zcode, ArrayZcode, String, bool, number, arraytype
    def __init__(self, eleType):
        self.eleType = eleType

class CannotBeInferredZcode(Type):
    def __str__(self):
        return "CannotBeInferredZcode()"


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
    
    def LHS_RHS_stmt(self, LHS : Type, RHS : Type, ctx):
        if isinstance(LHS, CannotBeInferredZcode) or isinstance(RHS, CannotBeInferredZcode):
            raise TypeCannotBeInferred(ctx)
        elif isinstance(LHS, Zcode) and isinstance(RHS, Zcode):
            raise TypeCannotBeInferred(ctx)
        elif isinstance(LHS, Zcode) and isinstance(RHS, ArrayZcode):
            raise TypeCannotBeInferred(ctx)
        elif isinstance(LHS, ArrayType) and isinstance(RHS, ArrayZcode):
            if not self.setTypeArray(LHS, RHS):
                raise TypeMismatchInStatement(ctx)
        elif isinstance(RHS, ArrayZcode):
            raise TypeCannotBeInferred(ctx)
        elif isinstance(LHS, Zcode):
            LHS.typ = RHS
        elif isinstance(RHS, Zcode):
            RHS.typ = LHS
        elif not self.comparType(LHS, RHS):
            raise TypeMismatchInStatement(ctx)
        else:
            return False
    
    def LHS_RHS_expr(self, LHS : Type, RHS : Type, ctx) -> bool:
        if isinstance(LHS, CannotBeInferredZcode) or isinstance(RHS, CannotBeInferredZcode):
            return True
        elif isinstance(LHS, Zcode) and isinstance(RHS, Zcode):
            return True
        elif isinstance(LHS, Zcode) and isinstance(RHS, ArrayZcode):
            return True
        elif isinstance(LHS, ArrayType) and isinstance(RHS, ArrayZcode):
            if not self.setTypeArray(LHS, RHS):
                raise TypeMismatchInExpression(ctx)
        elif isinstance(RHS, ArrayZcode):
            return True
        elif isinstance(LHS, Zcode):
            LHS.typ = RHS
        elif isinstance(RHS, Zcode):
            RHS.typ = LHS
        elif not self.comparType(LHS, RHS):
            raise TypeMismatchInExpression(ctx)
        else:
            return False
    
    def setTypeArray(self, typeArray: ArrayType, typeArrayZcode: ArrayZcode):
        #* Trường hợp size khác nhau
        if int(typeArray.size[0]) != len(typeArrayZcode.eleType):
            return False
        
        #* trường hợp bên trong array là các kiểu nguyên thủy (array 1 chiều)
           #^ nếu typeArrayZcode.eleType[i] là Zcode : gán typeArrayZcode.eleType[i].typ = typeArray.eleType
           #^ nếu typeArrayZcode.eleType[i] là arrayZcode : trả về False (vì 1 chiều mà bắt gán 2 chiều :) )
        if len(typeArray.size) == 1:
            #TODO implement
            size_1stD = len(typeArrayZcode.eleType)

            for i in range(size_1stD):
                RHS = typeArrayZcode.eleType[i]

                if isinstance(RHS, Zcode):
                    RHS.typ = typeArray.eleType
                elif isinstance(RHS, ArrayZcode):
                    return False

        #* trường hợp bên trong array là các arrayType (array >= 2 chiều)
           #^ nếu typeArrayZcode.eleType[i] là Zcode : gán typeArrayZcode.eleType[i].typ = typeArray.eleType
           #^ nếu typeArrayZcode.eleType[i] là arrayZcode : gọi đệ quy self.setTypeArray(ArrayType(typeArray.size[1:], typeArray.eleType),typeArrayZcode[i]) để vào bên trong xem có lỗi gì không       
        else:
            #TODO implement
            size_1stD = len(typeArrayZcode.eleType)

            for i in range(size_1stD):
                RHS = typeArrayZcode.eleType[i]

                if isinstance(RHS, Zcode):
                    RHS.typ = ArrayType(typeArray.size[1:], typeArray.eleType)
                elif isinstance(RHS, ArrayZcode):

                    check = self.setTypeArray(
                        ArrayType(typeArray.size[1:], typeArray.eleType),
                        RHS
                    )
                    if check == False:
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
            RHS = self.visit(ast.varInit, param)
            LHS = self.visit(ast.varType, param) if ast.varType else param[0][ast.name.name]

            # Check
            self.LHS_RHS_stmt(LHS, RHS, ast)
            
        return

    def visitFuncDecl(self, ast, param):
        #TODO kiểm tra name có trong listFunction hay không nén ra lỗi Redeclared
        declared_function = self.listFunction[0].get(ast.name.name)
        
        #TODO kiểm tra Param trong hàm
        listParam = {} #! dạng Dict có name
        typeParam = [] #! dạng mảng không cần name
        for funcParam in ast.param:
            id = funcParam.name.name
            if listParam.get(id) and ast.body: raise Redeclared(Parameter(), id)
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
            self.LHS_RHS_stmt(LHS, RHS, ast)

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

            if self.LHS_RHS_expr(LHS, RHS, ast): return CannotBeInferredZcode()

        # Check return type
        function_found = found
        if function_found.typ is None: return function_found
        if self.comparType(function_found.typ, VoidType()):
            raise TypeMismatchInExpression(ast)

        return function_found.typ


    def visitBlock(self, ast, param):
        paramNew = [{}] + param
        for item in ast.stmt:
            self.visit(item, paramNew)

    def visitFor(self, ast, param):

        #TODO Check type
        listLHS = [NumberType(), BoolType(), NumberType()]
        listRHS = [
            ast.name,
            ast.condExpr,
            ast.updExpr
        ]
        
        for i in range(3):

            LHS = listLHS[i]
            RHS = self.visit(listRHS[i], param)
            self.LHS_RHS_stmt(LHS, RHS, ast)


        self.BlockFor += 1
        self.visit(ast.body, param)
        self.BlockFor -= 1
        
    def visitContinue(self, ast, param):
        if self.BlockFor == 0: raise MustInLoop(ast)

    def visitBreak(self, ast, param):
        if self.BlockFor == 0: raise MustInLoop(ast)


    def visitNumberType(self, ast, param): return ast
    def visitBoolType(self, ast, param): return ast
    def visitStringType(self, ast, param): return ast
    def visitArrayType(self, ast, param): return ast
    def visitNumberLiteral(self, ast, param): return NumberType()
    def visitBooleanLiteral(self, ast, param): return BoolType()
    def visitStringLiteral(self, ast, param): return StringType()
    def visitArrayLiteral(self, ast, param):

        # Step 1: Check type of the ArrayLiteral, catch the first Type()!!
        typ = None
        listTyp = []
        for lit in ast.value:

            checkTyp = self.visit(lit, param)
            listTyp += [checkTyp]

            # Don't care if visit Zcode and ArrayZcode
            if not (isinstance(checkTyp, Zcode) or isinstance(checkTyp, ArrayZcode)):
                typ = checkTyp
                break
        
        # Case 1: typ is None -> ArrayZcode
        if typ is None: 
            return ArrayZcode(eleType=listTyp)
        
        # Case 2: typ is Normal
        elif type(typ) in [StringType, BoolType, NumberType]:
            LHS = typ
            for lit in ast.value:
                RHS = self.visit(lit, param)
                if self.LHS_RHS_expr(LHS, RHS , ast): return CannotBeInferredZcode()
                
            return ArrayType(size=[len(ast.value)], eleType=LHS)
        
        # Case 3: typ is ArrayType()
        else:
            LHS = typ
            for lit in ast.value:
                RHS = self.visit(lit, param)
                if self.LHS_RHS_expr(LHS, RHS , ast): return CannotBeInferredZcode()
                
            return ArrayType(size=[len(ast.value)] + LHS.size, eleType=LHS.eleType)

    def visitBinaryOp(self, ast, param):

        type_0 = ['+', '-', '*', '/', '%']
        type_1 = ['=', '!=', '<', '>', '>=', '<=']
        type_2 = ['and', 'or']
        type_3 = ['==']
        type_4 = ['...']

        def checkTypeHelper(input_type, output_type, left, right, param):

            LHS = self.visit(left, param)
            if self.LHS_RHS_expr(input_type, LHS, ast): return CannotBeInferredZcode()
            
            RHS = self.visit(right, param)
            if self.LHS_RHS_expr(input_type, RHS, ast): return CannotBeInferredZcode()

            return output_type
        
        left, right = ast.left, ast.right

        if ast.op in type_0:
            return checkTypeHelper(NumberType(), NumberType(), left, right, param)
        elif ast.op in type_1:
            return checkTypeHelper(NumberType(), BoolType(), left, right, param)
        elif ast.op in type_2:
            return checkTypeHelper(BoolType(), BoolType(), left, right, param) 
        elif ast.op in type_3:
            return checkTypeHelper(StringType(), BoolType(), left, right, param)
        elif ast.op in type_4:
            return checkTypeHelper(StringType(), StringType(), left, right, param)
        
        return Zcode()

    def visitUnaryOp(self, ast, param):
        
        operand = self.visit(ast.operand, param)

        type_0 = ['+', '-']
        type_1 = ['not']

        def checkTypeHelper(input_type, output_type):
            if self.LHS_RHS_expr(input_type, operand, ast): return CannotBeInferredZcode()
            
            return output_type
        
        if ast.op in type_0:
            return checkTypeHelper(NumberType(), NumberType())
        elif ast.op in type_1:
            return checkTypeHelper(BoolType(), BoolType()) 
        
        return Zcode()

    def visitArrayCell(self, ast, param):
        
        arr = self.visit(ast.arr, param)
        
        if isinstance(arr, (BoolType, StringType, NumberType)):
            raise TypeMismatchInExpression(ast)
        elif not isinstance(arr, ArrayType):
            return CannotBeInferredZcode()
        
        # Check idx
        for index in ast.idx:
            expr = self.visit(index, param)
            if self.LHS_RHS_expr(NumberType(), expr, ast): return CannotBeInferredZcode()
            
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
        self.LHS_RHS_stmt(BoolType(), expr, ast)
        
        # visit thenStmt
        self.visit(ast.thenStmt, param)

        # visit all elifStmt
        for ele in ast.elifStmt:

            # Check condition type
            elif_expr = self.visit(ele[0], param)
            self.LHS_RHS_stmt(BoolType(), elif_expr, ast)
            
            # visit stmt of elif
            self.visit(ele[1], param)
        
        # Visit elseStmt
        if ast.elseStmt:
            self.visit(ast.elseStmt, param)
        
        return

        

    def visitAssign(self, ast, param):
        
        RHS = self.visit(ast.rhs, param)
        LHS = self.visit(ast.lhs, param)

        self.LHS_RHS_stmt(LHS, RHS, ast)

    def visitReturn(self, ast, param):

        self.Return = True
        
        RHS = self.visit(ast.expr, param) if ast.expr else VoidType()
        LHS = None
        
        if self.function.typ:
            LHS = self.visit(self.function.typ, param) if not self.comparType(self.function.typ, VoidType()) else self.function.typ
        else: LHS = self.function

        self.LHS_RHS_stmt(LHS, RHS, ast)





