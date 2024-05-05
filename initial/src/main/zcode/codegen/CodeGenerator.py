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
    def __init__(self, frame: Frame, symbol: list[list], isLeft: bool, checkTypeLHS_RHS = False):
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
            if type(item) is FuncDecl and item.body is not None:

                if item.name.name != "main":
                    self.function = self.Listfunction[i]
                    self.visit(item, Symbol)
                    
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
    
    def visitVarDecl(self, ast, o: Access):
        
        frame: Frame = o.frame

        # create new index
        index = frame.getNewIndex()
        # emitVAR
        code = self.emit.emitVAR(
            in_=index,
            varName=ast.name.name,
            inType=ast.varType,
            fromLabel=frame.getStartLabel(),
            toLabel=frame.getEndLabel(),
            frame=frame
        )
        self.emit.printout(code)
        
        # add new var to symbol
        newVarDecl = VarZcode(ast.name.name, ast.varType, index)
        o.symbol[0].append(newVarDecl)
        o.symbol[0][-1].line = self.emit.printIndexNew()

        # Check varInit
        if ast.varInit:
            lhs = ast.name
            rhs = ast.varInit
            o.symbol[0][-1].init = True
            self.visit(Assign(lhs, rhs), o)

        elif type(ast.varType) is ArrayType:
            
            # LHS
            arrayType: ArrayType = ast.varType
            ## Array 1D
            if len(arrayType.size) == 1:
                
                # Visit NumberLiteral
                code = self.visit(NumberLiteral(arrayType.size[0]), Access(frame, o.symbol, True))
                self.emit.printout(code[0])

                # Take 1 int from frame for the array dimension
                self.emit.printout(self.emit.emitF2I(frame))
                # Get new array 1D from frame
                self.emit.printout(self.emit.emitNEWARRAY(arrayType.eleType, frame))
                # Place this var in static scope
                self.emit.printout(
                    self.emit.emitPUTSTATIC(
                        self.className + "." + ast.name.name,
                        arrayType,
                        frame
                    )
                )
            ## Array N-D
            else:
                for size in arrayType.size:
                    
                    # Visit NumberLiteral
                    code = self.visit(NumberLiteral(size), Access(frame, o.symbol, True))
                    self.emit.printout(code[0])

                    # Take 1 int from frame for the array dimension
                    self.emit.printout(self.emit.emitF2I(frame))

                # Get new array N-D from frame
                self.emit.printout(self.emit.emitMULTIANEWARRAY(arrayType, frame))
                # Place this var in static scope
                self.emit.printout(
                    self.emit.emitPUTSTATIC(
                        self.className + "." + ast.name.name,
                        arrayType,
                        frame
                    )
                )
        
        return

      
                              
    def visitFuncDecl(self, ast, Symbol: list[list]):

        self.Return = False

        frame = Frame(ast.name.name, None)
        code = self.emit.emitMETHOD(
            lexeme=ast.name.name,
            in_=self.function,
            isStatic=True,
            frame=frame
        )
        self.emit.printout(code)
        self.function.line = self.emit.printIndexNew()

        # Enter Scope
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        # Emit function
        typeParam = []
        forParam = VarDecl(Id("for"), NumberType())
        for funcParam in (ast.param + [forParam]):
            index = frame.getNewIndex()
            typeParam.append(
                VarZcode(funcParam.name.name, funcParam.varType, index, init=True) # Warning about init
            )
            typeParam[-1].line = self.emit.printIndexNew()

            code = self.emit.emitVAR(
                index, 
                funcParam.name.name, 
                funcParam.varType, 
                frame.getStartLabel(), 
                frame.getEndLabel(), 
                frame
            )
            self.emit.printout(code)
        
        # The body already not None, because this method only visit when body is not None
        self.visit(ast.body, Access(frame, [typeParam] + Symbol, False))

        if not self.Return:
            if self.function.typ is None:
                self.function.typ = VoidType()
        # Update frame
        frame.returnType = self.function.typ

        # Update function code
        code = self.emit.emitMETHOD(
            lexeme=ast.name.name,
            in_=self.function,
            isStatic=True,
            frame=frame
        )
        line = self.function.line
        self.emit.buff[line] = code

        # End function
        self.emit.printout(self.emit.emitRETURN(self.function.typ, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))

        # Exit Scope
        frame.exitScope()
        # self.emit.emitEPILOG()
        self.function = None
        

    def visitId(self, ast, o: Access):

        frame = o.frame
        Symbol = o.symbol

        # Update LHS, RHS
        if o.checkTypeLHS_RHS:
            for scope in Symbol:
                for sym in scope:
                    if sym.name == ast.name:
                        return None, sym.typ if sym.typ else sym
                                        
        # Find in all scope
        sym = None
        isGlobal = False
        for i, scope in enumerate(Symbol, 1):
            for item in scope:
                if item.name == ast.name:
                    sym = item
                    isGlobal = bool(i == len(Symbol)) # Global Scope
                    break

            if sym: break
        
        # Check scope
        code = None
        if not isGlobal:
            if o.isLeft: code = self.emit.emitWRITEVAR(sym.name, sym.typ, sym.index, frame)
            else: code = self.emit.emitREADVAR(sym.name, sym.typ, sym.index, frame)
        else:
            if o.isLeft: code = self.emit.emitPUTSTATIC(self.className + "/" + sym.name, sym.typ, frame)
            else: code = self.emit.emitGETSTATIC(self.className + "/" + sym.name, sym.typ, frame)
        
        return code, sym.typ if sym.typ else sym

    def visitCallExpr(self, ast, o: Access):

        # TH1: Check io -> call via class io.java in the lib
        ioFunctions = {
            "readNumber": NumberType(),
            "readBool": BoolType(),
            "readString": StringType()
        }
        returnType = ioFunctions.get(ast.name.name)
        if returnType:
            if o.checkTypeLHS_RHS: return None, returnType
            return self.emit.emitINVOKESTATIC(
                f"io/{ast.name.name}", 
                FuncZcode(ast.name.name, returnType, []), 
                o.frame
            ), NumberType

        # Check callFunction in self.Listfunction
        function = None
        for item in self.Listfunction:
            if item.name == ast.name.name:
                function = item
                
        # TH2: Update LHS, RHS
        if o.checkTypeLHS_RHS:

            listParam = function.param
            listArg = ast.args

            for i in range(len(listParam)):
                LHS = listParam[i]
                RHS = listArg[i]
                self.LHS_RHS(LHS, RHS, o)

            return None, function.typ if function.typ else function            
            
        # TH3: Not io, no checkTypeLHS_RHS
        codeReturn = ''
        for arg in ast.args:
            argCode, _ = self.visit(arg, o)
            codeReturn += argCode
        return codeReturn + self.emit.emitINVOKESTATIC(
            f"ZCodeClass/{ast.name.name}",
            function,
            o.frame
        ), function.typ
     

    def visitBinaryOp(self, ast, o: Access):
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
        codeReturn, returnType = codeLeft + codeRight, None

        if op in ['+', '-']:
            codeReturn += self.emit.emitADDOP(op, NumberType(), o.frame)
            returnType = NumberType()
            
        elif op in ['*', '/']:
            codeReturn += self.emit.emitMULOP(op, NumberType(), o.frame)
            returnType = NumberType()

        elif op in ['=', '!=', '<', '>', '>=', '<=']:
            codeReturn += self.emit.emitREOP(op, NumberType(), o.frame)
            returnType = BoolType()

        elif op in ['and']:
            codeReturn += self.emit.emitANDOP(o.frame)
            returnType = BoolType()

        elif op in ['or']:
            codeReturn += self.emit.emitOROP(o.frame)
            returnType = BoolType()
        
        elif op in ['==']:
            codeReturn += self.emit.emitINVOKEVIRTUAL(
                'java/lang/String/equals', 
                FuncZcode('java/lang/String/equals', BoolType(), [object()]), 
                o.frame
            )
            returnType = BoolType()
        
        elif op in ['...']:
            codeReturn += self.emit.emitINVOKEVIRTUAL(
                'java/lang/String/concat', 
                FuncZcode('java/lang/String/concat', StringType(), [StringType()]), 
                o.frame
            )
            returnType = StringType()
        
        elif op in ['%']:
            codeReturn += codeLeft # Need 1 frame
            codeReturn += codeRight # Need 1 frame

            o.frame.push() # Add new frame for codeLeft
            o.frame.push() # Add new frame for codeRight
            # Chia lấy nguyên
            codeReturn += self.emit.emitMULOP('/', NumberType(), o.frame)
            # Ép thành int
            codeReturn += self.emit.emitF2I(o.frame)
            # Ép lại thành F
            codeReturn += self.emit.emitI2F(o.frame)
            # Kết quả nhân với RHS
            codeReturn += self.emit.emitMULOP('*', NumberType(), o.frame)
            # LHS - (Kết quả nhân với RHS) = Phần dư
            codeReturn += self.emit.emitADDOP('-', NumberType(), o.frame)

            returnType = NumberType()
        
        return codeReturn, returnType



    def visitUnaryOp(self, ast, o: Access):
        op = ast.op
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            if op in ['-']:
                self.LHS_RHS(ast.operand, NumberType(), o)
                return None, NumberType()
            elif op in ['not']:
                self.LHS_RHS(ast.operand, BoolType(), o)
                return None, BoolType()
        
        codeOp, _ = self.visit(ast.operand, o)
        codeReturn, returnType = '', None

        if op in ['-']:
            codeReturn += codeOp
            codeReturn += self.emit.emitNEGOP(NumberType(), o.frame)
            returnType = NumberType()
        elif op in ['not']:
            codeReturn += codeOp
            codeReturn += self.emit.emitNOT(BoolType(), o.frame)
            returnType = BoolType()
        
        return codeReturn, returnType
    
    def visitArrayLiteral(self, ast, o: Access):
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
       
    def visitArrayCell(self, ast, o: Access):
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
        
       
        
    def visitNumberLiteral(self, ast, o: Access):
        return self.emit.emitPUSHCONST(ast.value, NumberType(), o.frame) if not o.checkTypeLHS_RHS else None, NumberType()
    def visitBooleanLiteral(self, ast, o: Access):
        return self.emit.emitPUSHCONST(ast.value, BoolType(), o.frame) if not o.checkTypeLHS_RHS else None, BoolType()
    def visitStringLiteral(self, ast, o: Access):
        return self.emit.emitPUSHCONST("\"" + ast.value + "\"", StringType(), o.frame) if not o.checkTypeLHS_RHS else None, StringType()
    def visitArrayType(self, ast, param): return None, ast
    def visitNumberType(self, ast, param): return None, NumberType()
    def visitVoidType(self, ast, param): return None, VoidType()
    def visitBoolType(self, ast, param): return None, BoolType()
    def visitStringType(self, ast, param): return None, StringType()
    def visitFuncZcode(self, ast, param): return None, ast.typ if ast.typ else ast
    def visitVarZcode(self, ast, param): return None, ast.typ if ast.typ else ast
    def visitReturn(self, ast, o: Access):
        
        # Check type
        LHS = self.function
        RHS = ast.expr if ast.expr else VoidType()
        self.LHS_RHS(LHS, RHS, o)
        
        self.Return = True
        frame = o.frame
        
        """#TODO emitRETURN
        #* TH1 : nếu  ast.expr is None
        #* TH2 : Ngc lại
        vd : return 1
        iconst_1
        freturn
        """
        rhsCode, _ = self.visit(RHS, o)
        self.emit.printout(rhsCode)
        self.emit.emitRETURN(RHS, frame)


    def visitAssign(self, ast, o: Access):
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
        self.emit.printout(rhsCode)
        self.emit.printout(lhsCode)
        
  
    
    def visitCallStmt(self, ast, o: Access):

        # TH1: Call write IO -> VoidType()
        ioFunctions = {
            "writeNumber": NumberType(),
            "writeBool": BoolType(),
            "writeString": StringType()
        }
        returnType = ioFunctions.get(ast.name.name)
        if returnType:
            
            self.LHS_RHS(returnType, ast.args[0], o)
            argsCode, argsType = self.visit(ast.args[0], o)
            self.emit.printout(argsCode)

            code = self.emit.emitINVOKESTATIC(
                f"io/{ast.name.name}", 
                FuncZcode(ast.name.name, VoidType(), [argsType]), 
                o.frame
            )
            self.emit.printout(code)
            return


        # Check callFunction in self.Listfunction
        function = None
        for item in self.Listfunction:
            if item.name == ast.name.name:
                function = item
        
        # TH2: Update LHS, RHS
        if o.checkTypeLHS_RHS:

            listParam = function.param
            listArg = ast.args

            for i in range(len(listParam)):
                LHS = listParam[i]
                RHS = listArg[i]
                self.LHS_RHS(LHS, RHS, o)

            return None, function.typ if function.typ else function
        
        # TH3: Not io, no checkTypeLHS_RHS
        for arg in ast.args:
            argCode, _ = self.visit(arg, o)
            self.emit.printout(argCode)
        code = self.emit.emitINVOKESTATIC(
            f"ZCodeClass/{ast.name.name}",
            function,
            o.frame
        )
        self.emit.printout(code)

        return
  
          
    def visitBlock(self, ast, o: Access):
        symbolnew = [[]] + o.symbol # increase Scope
        o.frame.enterScope(False) # new Scope

        code = self.emit.emitLABEL(o.frame.getStartLabel(), o.frame) 
        self.emit.printout(code)
        
        # Visit all statements
        for item in ast.stmt: 
            self.visit(item, Access(o.frame, symbolnew, False))
        
        code = self.emit.emitLABEL(o.frame.getEndLabel(), o.frame)
        self.emit.printout(code)

        o.frame.exitScope() # End Scope
       
    def visitIf(self, ast, o: Access):
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
        
        
        
        
    def visitFor(self, ast, o: Access):
        
        # Check LHS, RHS
        LHS = [NumberType(), BoolType(), NumberType()]
        RHS = [ast.name, ast.condExpr, ast.updExpr]
        for i in range(3):
            self.LHS_RHS(LHS[i], RHS[i], o)

        frame = o.frame
        self.visit(ast.name, o)
        
        # Step 1: Assign for = ast.name
        self.visit(Assign(Id("for"), ast.name), o)
        # Step 2: Create Loop
        frame.enterLoop()
        # Step 3: For Label, Break Label, Continue Label
        forLabel = frame.getNewLabel()
        breakLabel = frame.getBreakLabel()
        continueLabel = frame.getContinueLabel()
        # Step 3': Place forLabel here
        self.emit.printout(self.emit.emitLABEL(forLabel, frame))
        # Step 4: Check exp to jump to breakLabel
        expCode, _ = self.visit(ast.condExpr, Access(frame, o.symbol, False))
        self.emit.printout(expCode)
        self.emit.printout(self.emit.emitIFTRUE(breakLabel, frame)) # Yes it is =))
        # Step 5: visit body
        self.visit(ast.body, o)
        # Step 6: Place continueLabel here
        self.emit.printout(self.emit.emitLABEL(continueLabel, frame))
        # Step 7: Update Expr
        self.visit(Assign(ast.name, BinaryOp('+', ast.name, ast.updExpr)), o)
        # Step 8: Go back to forLabel
        self.emit.printout(self.emit.emitGOTO(forLabel, frame))
        # Step 9: Place breakLabel here
        self.emit.printout(self.emit.emitLABEL(breakLabel, frame))
        # Step 10: End Loop
        frame.exitLoop()
        # Step 11: Assign ast.name = for
        self.visit(Assign(ast.name, Id("for")), o)

    def visitContinue(self, ast, o: Access):

        code = self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame)
        self.emit.printout(code)

    def visitBreak(self, ast, o: Access):

        code = self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame)
        self.emit.printout(code)
        
