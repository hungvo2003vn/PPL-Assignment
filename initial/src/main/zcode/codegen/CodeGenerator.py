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
    def __init__(self, frame, symbol, isLeft, checkTypeLHS_RHS = False):
        self.frame = frame #* không gian stack và local cần dùng để chạy 1 hàm
        self.symbol = symbol #* giống phần param ở BTL3 nhưng này hiện thực list<list>> (có thể dùng list<dict> như btl3)
        self.isLeft = isLeft #* hiện tại vế trên trái hay bên phải để xác định get và put cho biến
        self.checkTypeLHS_RHS = checkTypeLHS_RHS  #* kiểm tra kiểu đúng không

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
        #* TRUYỀN checkTypeLHS_RHS = Flase -> nghĩa là chúng ta xét type trước, trước khi lấy stack
        _, rhsType = self.visit(RHS, Access(o.frame, o.symbol, False, True))
        _, lhsType = self.visit(LHS, Access(o.frame, o.symbol, True, True))
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
                index = -1
                Symbol[0].append(VarZcode(item.name.name, item.varType, -1, True if item.varInit else False))
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
        index = frame.getNewIndex()
        typeParam = [VarZcode("for", NumberType(), index, True)]
        self.emit.printout(self.emit.emitVAR(index, "for", NumberType(), frame.getStartLabel(), frame.getEndLabel(), frame))
        self.function = function
        self.visit(Main.body, Access(frame, [typeParam] + Symbol, False))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))   
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()    
        self.emit.emitEPILOG()
    
    def visitVarDecl(self, ast, o):
        """#TODO: Implement
        #* tạo emitVAR và o.symbol[0].append, cập nhật o.symbol[0][-1].line
        #* if ast.varInit is not None:
            #* self.visit(Assign(ast.name, ast.varInit), o) 
        #* elif type(ast.varType) is ArrayType:
            #* giống phần khai báo biến static gần giống ý tưởng
        """
      
                              
    def visitFuncDecl(self, ast, Symbol):
        self.Return = False
        """TODO: Implement
        #* giống hàm main, nhưng phần này có param
        """
     

    def visitId(self, ast, o):
            frame = o.frame
            Symbol = o.symbol
            
            #* cập nhật type lhs or RHS giống btl3
            if o.checkTypeLHS_RHS:
                for item in Symbol:
                    for sym in item:
                        if sym.name == ast.name:
                            return None, sym.typ if sym.typ else sym
                                        

    def visitCallExpr(self, ast, o):
        #* phần io -> gọi qua class io.java trong phần lib
        if ast.name.name in ["readNumber", "readBool", "readString"]:
            if ast.name.name == "readNumber": 
                if o.checkTypeLHS_RHS: return None, NumberType()
                return self.emit.emitINVOKESTATIC(f"io/{ast.name.name}", FuncZcode(ast.name.name, NumberType(), []), o.frame), NumberType
            elif ast.name.name == "readBool": 
                if o.checkTypeLHS_RHS: return None, BoolType()
                return self.emit.emitINVOKESTATIC(f"io/{ast.name.name}", FuncZcode(ast.name.name, BoolType(), []), o.frame), NumberType
            elif ast.name.name == "readString": 
                if o.checkTypeLHS_RHS: return None, StringType()
                return self.emit.emitINVOKESTATIC(f"io/{ast.name.name}", FuncZcode(ast.name.name, StringType(), []), o.frame), NumberType

        #* tìm function trong self.Listfunction
        function = None
        for item in self.Listfunction:
            if item.name == ast.name.name:
                function = item
                
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            for i in range(len(function.param)):
                self.LHS_RHS(function.param[i], ast.args[i], o)
            return None, function.typ if function.typ else function            
            
        
        """#TODO : gọi emitINVOKESTATIC
        ví dụ : 
        .line 12 -> foo(1,true)
        0: iconst_1
        1: iconst_1
        2: invokestatic ZCodeClass/foo(IZ)V        
        """
     

    def visitBinaryOp(self, ast, o):
        op = ast.op
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            if op in ['+', '-', '*', '/', '%']:
                self.LHS_RHS(ast.left, NumberType(), o)
                self.LHS_RHS(ast.right, NumberType(), o)
                return None, NumberType()
            elif op in ['=', '!=', '<', '>', '>=', '<=']:
                self.LHS_RHS(ast.left, NumberType(), o)
                self.LHS_RHS(ast.right, NumberType(), o)
                return None, BoolType()
            elif op in ['and', 'or']:
                self.LHS_RHS(ast.left, BoolType(), o)
                self.LHS_RHS(ast.right, BoolType(), o)
                return None, BoolType()
            elif op in ['==']:
                self.LHS_RHS(ast.left, StringType(), o)
                self.LHS_RHS(ast.right, StringType(), o)
                return None, BoolType()
            elif op in ['...']:
                self.LHS_RHS(ast.left, StringType(), o)
                self.LHS_RHS(ast.right, StringType(), o)
                return None, StringType()
        
        codeLeft, _ = self.visit(ast.left, o)
        codeRight, _ = self.visit(ast.right, o)
        """#TODO emitADDOP, emitMULOP, emitREOP, emitANDOP,emitOROP, emitREOP, emitINVOKEVIRTUAL (dùng java/lang/String/concat và java/lang/String/equals)
        #^ mọi năm có tính toán lười cho and và or năm này thấy thầy ko mô tả lạ thật :((
        #* khó nhất chắc là % ta dùng như sau 
            codeLeft
            codeRight
            codeLeft
            codeRight
            '/'
            emitF2I -> ép kiểu sang int
            emitI2F -> từ in ép kiểu ngược lại
            '*'
            '-'
        """
       

    def visitUnaryOp(self, ast, o):
        op = ast.op
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            if op in ['-']:
                self.LHS_RHS(ast.operand, NumberType(), o)
                return None, NumberType()
            elif op in ['not']:
                self.LHS_RHS(ast.operand, BoolType(), o)
                return None, BoolType()
        """#TODO mitNEGOP, emitNOT
        """

    
    def visitArrayLiteral(self, ast, o):
        frame = o.frame
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            mainTyp = None
            for item in ast.value:
                _, checkTyp = self.visit(item, o)
                if mainTyp is None and isinstance(checkTyp, (BoolType, StringType, NumberType, ArrayType)):
                    mainTyp = checkTyp
                    break
        
            for item in ast.value:
                self.LHS_RHS(mainTyp, item, o)
            
            if isinstance(mainTyp, (BoolType, StringType, NumberType)):
                return None, ArrayType([len(ast.value)], mainTyp)
            return None, ArrayType([float(len(ast.value))] + mainTyp.size, mainTyp.eleType)

        """#TODO:
        #* trường hợp mảng 1 chiều
            emitPUSHCONST -> giá trị khởi tạo của mảng
            emitF2I -> ép kiểu sang int
            emitNEWARRAY -> khởi tạo mảng
            for
                emitDUP -> nhân 2 ở đây là địa chỉ của mảng khởi tạo phía trên
                emitPUSHCONST -> giá trị index trong mảng
                emitF2I
                visit -> giá trị biến
                emitASTORE -> lưu trữ
    
        #* trường hợp mảng nhiều chiều
            emitPUSHCONST -> giá trị khởi tạo của mảng
            emitF2I -> ép kiểu sang int
            emitANEWARRAY -> khởi tạo mảng
            for
                emitDUP -> nhân 2 ở đây là địa chỉ của mảng khởi tạo phía trên
                emitPUSHCONST -> giá trị index trong mảng
                emitF2I
                visit -> giá trị biến
                emitASTORE -> lưu trữ             
        """
       
    def visitArrayCell(self, ast, o):
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            _, arr = self.visit(ast.arr, Access(o.frame, o.symbol, False, False))
            for i in ast.idx:
                self.LHS_RHS(NumberType(), i, o)
            if len(arr.size) == len(ast.idx): return None, arr.eleType
            return None, ArrayType(arr.size[len(ast.idx):], arr.eleType)   


        """#TODO:
        #* trường trả về giá trị khác mảng
            visit(ast.arr) -> lấy ra get/put/read/write
            for 0 -> size - 1
               giá trị tại index
               f2i
               aload
            giá trị tại index = -1
            f2i
            float/bload/aload(string)  (nếu o.isLeft thì bỏ qua không gọi mà gán self.arrayCell = typ)  
    
        #* trường hợp tra về magnr
            visit(ast.arr) -> lấy ra get/put/read/write
            for 0 -> size - 1
               giá trị tại index
               f2i
               aload
            giá trị tại index = -1
            f2i
            aload -> địa chỉ   (nếu o.isLeft thì bỏ qua không gọi mà gán self.arrayCell = typ)            
        """
        
       
        
    def visitNumberLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, NumberType(), o.frame) if not o.checkTypeLHS_RHS else None, NumberType()
    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, BoolType(), o.frame) if not o.checkTypeLHS_RHS else None, BoolType()
    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST("\"" + ast.value + "\"", StringType(), o.frame) if not o.checkTypeLHS_RHS else None, StringType()
    def visitArrayType(self, ast, param): return None, ast
    def visitNumberType(self, ast, param): return None, NumberType()
    def visitVoidType(self, ast, param): return None, VoidType()
    def visitBoolType(self, ast, param): return None, BoolType()
    def visitStringType(self, ast, param): return None, StringType()
    def visitFuncZcode(self, ast, param): return None, ast.typ if ast.typ else ast
    def visitVarZcode(self, ast, param): return None, ast.typ if ast.typ else ast
    def visitReturn(self, ast, o):
        #* CHECK TYPE BTL3
        self.LHS_RHS(self.function, ast.expr if ast.expr else VoidType(),o)
        
        self.Return = True #* đã có return
        frame = o.frame
        
        """#TODO emitRETURN
        #* TH1 : nếu  ast.expr is None
        #* TH2 : Ngc lại
        vd : return 1
        iconst_1
        freturn
        """


    def visitAssign(self, ast, o):
        self.LHS_RHS(ast.lhs, ast.rhs, o)
        frame = o.frame
        rhsCode, _ = self.visit(ast.rhs, Access(frame, o.symbol, False))
        lhsCode, _ = self.visit(ast.lhs, Access(frame, o.symbol, True))
        
        """TODO
        TH1 : LHS = ArrayCell
        lhsCode
        rhsCode
        self.emit.emitASTORE(self.arrayCell, frame))
        
        TH2 : 
        lhsCode
        rhsCode        
        """
  
    
    def visitCallStmt(self, ast, o):
        #* phần io
        if ast.name.name in ["writeNumber", "writeBool", "writeString"]:
            if ast.name.name == "writeNumber": self.LHS_RHS(NumberType(), ast.args[0], o)
            elif ast.name.name == "writeBool": self.LHS_RHS(BoolType(), ast.args[0], o)
            elif ast.name.name == "writeString": self.LHS_RHS(StringType(), ast.args[0], o)
            
            argsCode, argsType = self.visit(ast.args[0], o)
            self.emit.printout(argsCode)
            self.emit.printout(self.emit.emitINVOKESTATIC(f"io/{ast.name.name}", FuncZcode(ast.name.name, VoidType(), [argsType]), o.frame))
            return

        """#TODO giống call expr"""
  
          
    def visitBlock(self, ast, o):
        symbolnew = [[]] + o.symbol #! tăng tầm vực
        o.frame.enterScope(False) #* tầm vực mới
        self.emit.printout(self.emit.emitLABEL(o.frame.getStartLabel(), o.frame)) #* đánh số tầm vực
        for item in ast.stmt: 
            self.visit(item,Access(o.frame, symbolnew, False))   
        self.emit.printout(self.emit.emitLABEL(o.frame.getEndLabel(), o.frame))
        o.frame.exitScope()  #* kết thức tầm vực
       
    def visitIf(self, ast, o):
        #* CHECK TYPE BTL3       
        self.LHS_RHS(BoolType(), ast.expr, o)        
        for item in ast.elifStmt:
            self.LHS_RHS(BoolType(), item[0], o)   
        
        frame = o.frame
        """_enterLoop_
            điều kiện if -> nhảy đến đặt label end if
                |
            visit body
                |
            goto exit
                |
            đặt label end if
                |
            nếu có eilf -> for
                tạo lable mới
                    |
                điều kiện -> nhảy lable mới
                    | 
                visit
                    |
                goto exit
                    |
                đặt đến lable mới
                    |
            -- end for
                |
            nếu có else
                |
              visit
                |
            lable exit
        """
        label_exit = frame.getNewLabel()


        self.emit.printout(self.emit.emitLABEL(label_exit, o.frame))  
        
        
        
        
    def visitFor(self, ast, o):
        
        #* CHECK TYPE BTL3
        """_typID_"""        
        self.LHS_RHS(NumberType(), ast.name, o)        
        
        """_typCondExpr_"""    
        self.LHS_RHS(BoolType(), ast.condExpr, o) 

        """_typUpdExpr_"""            
        self.LHS_RHS(NumberType(), ast.updExpr, o) 

        frame = o.frame
        self.visit(ast.name, o)
        
        """_enterLoop_
            gán for <- ast.name
                |
            tạo Loop
                |
            lable_new
                |
            kiểm tra exp để goto đến lable_Break
                |
            visit body
                |
            đặt lable continue
                |
            gọi phép gán Assign(ast.name, BinaryOp('+', ast.name, ast.updExpr))
                |
            goto đến lable_new
                |
            đặt lable_Break
                |
            end loop
                |
            gán for <- ast.name
            
        """
        self.visit(Assign(Id("for"), ast.name), o)
     
        self.visit(Assign(ast.name, Id("for")), o)

    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))

    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))
        
