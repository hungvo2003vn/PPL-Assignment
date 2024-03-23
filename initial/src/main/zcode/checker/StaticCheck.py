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
        self.io = [{
                "readNumber" : FuncZcode([], NumberType(), True),
                "readBool" : FuncZcode([], BoolType(), True),
                "readString" : FuncZcode([], StringType(), True),
                "writeNumber" : FuncZcode([NumberType()], VoidType(), True),
                "writeBool" : FuncZcode([BoolType()], VoidType(), True),
                "writeString" : FuncZcode([StringType()], VoidType(), True)
                }]
        
    def check(self):
        self.visit(self.ast, self.io)
        return "successful"    
    
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
        for decl_name, decl_desciption in param[0].items():
            if not isinstance(decl_desciption, FuncZcode): continue
            if not decl_desciption.body: raise NoDefinition(decl_name)
            
        #TODO  check No entry point in param
        main_func = param[0].get('main')
        if (main_func is None) or not isinstance(main_func, FuncZcode) or (len(main_func.param) > 0): 
            raise NoEntryPoint()

        return

    def visitVarDecl(self, ast, param):
        #TODO kiểm tra name có trong param[0] hay không nén ra lỗi Redeclared
        if param[0].get(ast.name.name) is not None: raise Redeclared(Variable(), ast.name.name)
    
        param[0][ast.name.name] = VarZcode(ast.varType) #! cập nhật param mới

        #! phần này xử lí nhiều hơn ở task2
        if ast.varInit: self.visit(ast.varInit, param)
        return param

    def visitFuncDecl(self, ast, param):
        #TODO kiểm tra name có trong param[0] hay không nén ra lỗi Redeclared
        declared_function = param[0].get(ast.name.name)
        if declared_function and not self.comparType(FuncZcode(), declared_function): 
            raise Redeclared(Function(), ast.name.name)

        #TODO kiểm tra Param trong hàm
        listParam = {} #! dạng Dict có name
        typeParam = [] #! dạng mảng không cần name
        for funcParam in ast.param:
            id = funcParam.name.name
            if listParam.get(id): raise Redeclared(Parameter(), id)
            # Update list param
            listParam[id] = VarZcode(funcParam.varType)
            typeParam += [funcParam.varType]
        
        #TODO chia làm 3 TH
        #* TH 1: là method đã so sẵn nghĩa là được khai báo 1 phần trước yêu cầu kiểm tra 2 list có giống nhau không nếu không nén ra Redeclared
        if self.comparType(FuncZcode(), declared_function) and not self.comparListType(typeParam, declared_function.param): 
            raise Redeclared(Function(), ast.name.name)
        
        #* TH 2: là khai báo 1 phần ast.body is None
        if self.comparType(FuncZcode(), declared_function) and declared_function.body:
            raise Redeclared(Function(), ast.name.name)

        #* TH 3: là khai báo toàn bộ
        if ast.body: 
            param[0][ast.name.name] = FuncZcode(typeParam, None, True)
            self.visit(ast.body, [listParam] + param)
        else:
            param[0][ast.name.name] = FuncZcode(typeParam, None, False)

        #! nếu không có type khi duyệt qua body thì là voidtype
        if param[0][ast.name.name].typ is None:
            param[0][ast.name.name].typ = VoidType()
        return param

    def visitId(self, ast, param):
        #TODO kiểm tra xem name có trong toàn bộ param nén lỗi Undeclared
        for scope in param:
            id = scope.get(ast.name)
            if id:
                if isinstance(id, FuncZcode): Undeclared(Identifier(), ast.name)
                else: return
        
        raise Undeclared(Identifier(), ast.name)

    def visitCallStmt(self, ast, param):
        #TODO kiểm tra xem name có trong toàn bộ param nén lỗi Undeclared
        found = False
        for scope in param:
            decl = scope.get(ast.name.name)
            if not decl: continue
            if not self.comparType(FuncZcode(), decl): raise Undeclared(Function(), ast.name.name)
            found = True
            break

        # Cannot find the function declaration
        if not found:  
            raise Undeclared(Function(), ast.name.name)
        
        # Visit args:
        for arg in ast.args:
            self.visit(arg, param)

    def visitCallExpr(self, ast, param):
        #TODO kiểm tra xem name có trong toàn bộ param nén lỗi Undeclared
        found = False
        for scope in param:
            decl = scope.get(ast.name.name)
            if not decl: continue
            if not self.comparType(FuncZcode(), decl): raise Undeclared(Function(), ast.name.name)
            found = True
            break

        # Cannot find the function declaration
        if not found:  
            raise Undeclared(Function(), ast.name.name)
        
        # Visit args:
        for arg in ast.args:
            self.visit(arg, param)


    def visitBlock(self, ast, param):
        for item in ast.stmt:
            #! trường hợp gặp block
            if type(item) is Block: self.visit(item, [{}] + param)
            else: self.visit(item, param)


    def visitFor(self, ast, param):
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
    def visitNumberLiteral(self, ast, param): return NumberLiteral(ast.value)
    def visitBooleanLiteral(self, ast, param): return BooleanLiteral(ast.value)
    def visitStringLiteral(self, ast, param): return StringLiteral(ast.value)
    def visitArrayLiteral(self, ast, param):
        for lit in ast.value:
            lit = self.visit(lit, [{}] + param)
        typ = ast.value[0]
        if self.comparListType([typ]*3, [NumberType(), BoolType(), StringType()]):
            return ArrayType([len(ast.value)], typ)
        elif isinstance(typ, ArrayType):
            return ArrayType([len(ast.value)] + typ.size, typ.eleType)

    def visitBinaryOp(self, ast, param):
        pass

    def visitUnaryOp(self, ast, param):
        pass

    def visitArrayCell(self, ast, param):
        pass

    def visitIf(self, ast, param):
        pass

    def visitAssign(self, ast, param):
        pass

    def visitReturn(self, ast, param):
        pass

