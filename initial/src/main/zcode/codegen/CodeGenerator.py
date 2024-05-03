from Emitter import *
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *


class CodeGenerator:
    def gen(self, ast, path):
        # ast: AST
        # dir_: String
        gc = CodeGenVisitor(ast, path)
        gc.visit(ast, None)

class Access():
    def __init__(self, frame, symbol, isLeft, isType = True, isFirst=False):
        self.frame = frame #* không gian stack và local cần dùng để chạy 1 hàm
        self.symbol = symbol #* giống phần param ở BTL3 nhưng này hiện thực list<list>> (có thể dùng list<dict> như btl3)
        self.isLeft = isLeft #* hiện tại vế trên trái hay bên phải để xác định get và put cho biến
        self.isFirst = isFirst
        self.isType = isType 

class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, path):
        self.astTree = astTree
        self.path = path
        self.className = "ZCodeClass"
        self.emit = Emitter(self.path + "/" + self.className  + ".j")
        self.Listfunction = []
        self.function = None
        self.Return = False
        self.arrayCell = ""

    
    def printListfunction(self):
        print(f"self.function: {str(self.function)}" )
        print(f"self.Return  : {str(self.Return)}" )
        print(f"listFunction :")
        for item in self.Listfunction:
            print(f"         : {str(item)}" )
            

    
    #* CẬP NHẬT TYPE
    def LHS_RHS(self, LHS, RHS, o):
        #* TRUYỀN isType = Flase -> nghĩa là chúng ta xét type trước, trước khi lấy stack
        _, rhsType = self.visit(RHS, Access(o.frame, o.symbol, False, False))
        _, lhsType = self.visit(LHS, Access(o.frame, o.symbol, True, False))
        print(f"LHS : {lhsType}")
        print(f"RHS : {rhsType}")
        if isinstance(lhsType, Zcode):
            lhsType.typ = rhsType
            self.emit.setType(lhsType) #* cập nhật lại type vì trước đó type là None
        elif isinstance(rhsType, Zcode):
           rhsType.typ = lhsType
           self.emit.setType(rhsType) #* cập nhật lại type vì trước đó type là None
    
    def visitProgram(self, ast:Program, o):
        #* khởi tạo chương trình ZCodeClass
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
    
        #* khởi tạo anh em biến toàn cục, hàm -> cho nó static giống java
        Symbol = [[]]
        Main = None
        function = None
        for item in ast.decl:
            if type(item) is VarDecl:
                Symbol[0].append(VarZcode(item.name.name, item.varType, -1))
                self.emit.printout(self.emit.emitATTRIBUTE(item.name.name, item.varType if item.varType else Symbol[0][-1], False, self.className))
                Symbol[0][-1].line = self.emit.printIndexNew()
            elif type(item) is FuncDecl and item.body is not None:
                self.Listfunction += [FuncZcode(item.name.name, None, [i.varType for i in item.param])]
                if item.name.name == "main":
                    function = self.Listfunction[-1]
                    Main = item
        
    
        #* hàm khởi tạo trong Zcode 
        frame = Frame("<init>", VoidType)
        self.emit.printout(self.emit.emitMETHOD(lexeme="<init>", in_=FuncZcode("init", VoidType(), []), isStatic=False, frame=frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", Zcode(), frame.getStartLabel(), frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR("this", self.className, 0, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))   
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()


        #* hàm khởi tạo biến static Zcode
        frame = Frame("<clinit>", VoidType)
        self.emit.printout(self.emit.emitMETHOD(lexeme="<clinit>", in_=FuncZcode("clinit", VoidType(), []), isStatic=True, frame=frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        for var in ast.decl:
            if type(var) is VarDecl and var.varInit is not None:
                self.visit(Assign(var.name, var.varInit), Access(frame, Symbol, False)) 
            elif type(var) is VarDecl and type(var.varType) is ArrayType:
                if len(var.varType.size) == 1:
                    self.emit.printout(self.visit(NumberLiteral(var.varType.size[0]), Access(frame, Symbol, False))[0])
                    self.emit.printout(self.emit.emitF2I(frame))
                    self.emit.printout(self.emit.emitNEWARRAY(var.varType.eleType, frame))
                    self.emit.printout(self.emit.emitPUTSTATIC(self.className + "." + var.name.name, var.varType, frame))
                else:
                    for i in var.varType.size:
                        self.emit.printout(self.visit(NumberLiteral(i), Access(frame, Symbol, False))[0])
                        self.emit.printout(self.emit.emitF2I(frame))
                    self.emit.printout(self.emit.emitMULTIANEWARRAY(var.varType, frame))
                    self.emit.printout(self.emit.emitPUTSTATIC(self.className + "." + var.name.name, var.varType, frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame)) 
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()    
    
    
        
        #* khởi tạo các hàm static
        i = 0
        for item in ast.decl:
            if type(item) is FuncDecl and item.body is not None and item.name.name != "main":
                self.function = self.Listfunction[i]
                self.visit(item, Symbol)
            if type(item) is FuncDecl and item.body is not None:
                i += 1
                
        
        #* khởi tạo hàm main
        frame = Frame("main", VoidType)
        self.emit.printout(self.emit.emitMETHOD(lexeme="main", in_=FuncZcode("main", VoidType(), [ArrayType([1], StringType())]), isStatic=True, frame=frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        self.function = function
        self.visit(Main.body, Access(frame, Symbol, False))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))   
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()    
                
                
        

         
        
        self.emit.emitEPILOG()
    
    def visitVarDecl(self, ast, o):
        pass
            
    def visitFuncDecl(self, ast, Symbol):
        self.Return = False
        
        frame = Frame(ast.name.name, VoidType)
        self.emit.printout(self.emit.emitMETHOD(lexeme=ast.name.name, in_=self.function, isStatic=True, frame=frame))
        self.function.line = self.emit.printIndexNew()
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        typeParam = []
        for param in ast.param:
            index = frame.getNewIndex()
            typeParam += [VarZcode(param.name.name, param.varType, index)]
            self.emit.printout(self.emit.emitVAR(index, param.name.name, param.varType, frame.getStartLabel(), frame.getEndLabel(), frame))
        self.visit(ast.body, Access(frame,[typeParam] +  Symbol, False))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))   
        if not self.Return:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
            self.LHS_RHS(self.function, VoidType(), Access(frame, Symbol, False))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()    

    def visitId(self, ast, o):
           pass

    def visitCallExpr(self, ast, o):
       pass
        
        # if ast.name.name in read:

    def visitReturn(self, ast, o):
        pass
    def visitAssign(self, ast, o):
       pass

        
    def visitCallStmt(self, ast, o):
        if ast.name.name in ["writeNumber", "writeBool", "writeString"]:
            if ast.name.name == "writeNumber": self.LHS_RHS(NumberType(), ast.args[0], o)
            elif ast.name.name == "writeBool": self.LHS_RHS(BoolType(), ast.args[0], o)
            elif ast.name.name == "writeString": self.LHS_RHS(StringType(), ast.args[0], o)
            
            argsCode, argsType = self.visit(ast.args[0], o)
            self.emit.printout(argsCode)
            self.emit.printout(self.emit.emitINVOKESTATIC(f"io/{ast.name.name}", FuncZcode(ast.name.name, VoidType(), [argsType]), o.frame))
            return
          
    def visitBlock(self, ast, o):
        symbolnew = [[]] + o.symbol #! tăng tầm vực
        o.frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(o.frame.getStartLabel(), o.frame))
        for item in ast.stmt: 
            self.visit(item,Access(o.frame, symbolnew, False))   
        self.emit.printout(self.emit.emitLABEL(o.frame.getEndLabel(), o.frame))
        o.frame.exitScope()

    def visitBinaryOp(self, ast, o):
       pass

    def visitUnaryOp(self, ast, o):
       pass
    def visitIf(self, ast, o):
         pass
        
    def visitFor(self, ast, o):
         pass

    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))

    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))

    def visitNumberLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, NumberType(), o.frame) if o.isType else None, NumberType()
    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, BoolType(), o.frame) if o.isType else None, BoolType()
    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST("\"" + ast.value + "\"", StringType(), o.frame) if o.isType else None, StringType()
    def visitArrayType(self, ast, param): return None, ast
    def visitNumberType(self, ast, param): return None, NumberType()
    def visitVoidType(self, ast, param): return None, VoidType()
    def visitBoolType(self, ast, param): return None, BoolType()
    def visitStringType(self, ast, param): return None, StringType()
    def visitFuncZcode(self, ast, param): return None, ast.typ if ast.typ else ast
    def visitVarZcode(self, ast, param): return None, ast.typ if ast.typ else ast
    