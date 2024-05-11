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
        self.frame = frame
        self.symbol = symbol
        self.isLeft = isLeft
        self.checkTypeLHS_RHS = checkTypeLHS_RHS

class Global():
    def __init__(self, symbol: list[list] = [[]], main: FuncDecl = None, function: FuncZcode = None, frame: Frame = None):
        self.symbol = symbol
        self.main = main
        self.function = function,
        self.frame = frame

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
     
    # Update type
    def LHS_RHS(self, LHS, RHS, o: Access):

        lhsAccess = Access(o.frame, o.symbol, True, True)
        rhsAccess = Access(o.frame, o.symbol, False, True)
        _, rhsType = self.visit(RHS, rhsAccess)
        _, lhsType = self.visit(LHS, lhsAccess)

        if isinstance(lhsType, Zcode) or isinstance(rhsType, Zcode):

            typ = rhsType if isinstance(lhsType, Zcode) else lhsType
            ZcodeType = rhsType if isinstance(rhsType, Zcode) else lhsType
            # Set type for Zcode and buff
            ZcodeType.typ = typ
            self.emit.setType(ZcodeType)
    
    def initGlobal(self, ast:Program):

        # Init method, var in global
        Symbol = [[]]
        Main = None
        function = None

        for item in ast.decl:

            if type(item) is VarDecl:

                index = -1
                # Add var to current scope
                newVar = VarZcode(item.name.name, item.varType, index, True if item.varInit else False)
                Symbol[0].append(newVar)

                code = self.emit.emitATTRIBUTE(
                    item.name.name, 
                    item.varType if item.varType else Symbol[0][-1], 
                    False, 
                    self.className
                )
                self.emit.printout(code)

                # Record buffer's line of var
                Symbol[0][-1].line = self.emit.printIndexNew()

            elif type(item) is FuncDecl and item.body is not None:
                
                # Add new function
                newFunction = FuncZcode(item.name.name, None, [i.varType for i in item.param])
                self.Listfunction.append(newFunction)

                if item.name.name == "main":
                    function = self.Listfunction[-1]
                    Main = item

        return Global(Symbol, Main, function)

    def initConstructor(self):

        # Constructor in Zcode 
        frame = Frame("<init>", VoidType)
        # Init Method
        code = self.emit.emitMETHOD(
            lexeme="<init>", 
            in_=FuncZcode("init", VoidType(), []), 
            isStatic=False, 
            frame=frame
        )
        self.emit.printout(code)

        # Enter scope, emitLABEL
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Declare attributes, methods
        self.emit.printout(
            self.emit.emitVAR(
                frame.getNewIndex(), 
                "this", Zcode(), 
                frame.getStartLabel(), 
                frame.getEndLabel(), 
                frame)
        )

        # Read attributes, methods
        self.emit.printout(
            self.emit.emitREADVAR(
                "this", 
                self.className, 
                0, 
                frame
            )
        )
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        # End Constructor
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))   
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))

        # Exit scope
        frame.exitScope()
    
    def initAttribute(self, ast: Program, o: Global):

        # Init Attribute in ZcodeClass
        Symbol = o.symbol
        frame = Frame("<clinit>", VoidType)

        # Init Constructor
        code = self.emit.emitMETHOD(
            lexeme="<clinit>", 
            in_=FuncZcode("clinit", VoidType(), []), 
            isStatic=True, 
            frame=frame
        )
        self.emit.printout(code)

        # Enter scope, emitLABEL
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        for var in ast.decl:

            if type(var) is VarDecl and var.varInit is not None:

                LHS = var.name
                RHS = var.varInit
                self.visit(Assign(LHS, RHS), Access(frame, Symbol, False))

            elif type(var) is VarDecl and type(var.varType) is ArrayType:
                
                arrayType: ArrayType = var.varType
                for i in arrayType.size:

                    sizeCode, _ = self.visit(
                        NumberLiteral(i), 
                        Access(frame, Symbol, False)
                    )
                    self.emit.printout(sizeCode)
                    self.emit.printout(self.emit.emitF2I(frame))

                # 1-D array
                if len(arrayType.size) == 1:
                    self.emit.printout(self.emit.emitNEWARRAY(arrayType.eleType, frame))
                
                else:
                    self.emit.printout(self.emit.emitMULTIANEWARRAY(arrayType, frame))
                # N-D array
                self.emit.printout(
                    self.emit.emitPUTSTATIC(
                        self.className + "." + var.name.name, 
                        arrayType, 
                        frame
                    )
                )

        # End method
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame)) 
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        # Exit scope
        frame.exitScope()

    def initMethod(self, ast: Program, o: Global):

        i = 0
        Symbol = o.symbol
        for item in ast.decl:
            if type(item) is FuncDecl and item.body is not None:

                if item.name.name != "main":
                    self.function = self.Listfunction[i]
                    self.visit(item, Symbol)
                    
                i += 1
    
    def initMainMethod(self, o: Global):

        Main = o.main
        Symbol = o.symbol
        function = o.function
        frame = Frame("main", VoidType)

        code = self.emit.emitMETHOD(
            lexeme="main", 
            in_=FuncZcode("main", VoidType(), [ArrayType([1], StringType())]), 
            isStatic=True, 
            frame=frame
        )
        self.emit.printout(code)

        # Enter Scope and emitLABEL
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Init String[] args in java
        code = self.emit.emitVAR(
            frame.getNewIndex(), 
            "args", 
            ArrayType([], StringType()), 
            frame.getStartLabel(), 
            frame.getEndLabel(), 
            frame
        )
        self.emit.printout(code)

        # Temp param used for ForStmt
        index = frame.getNewIndex()
        typeParam = [VarZcode("for", NumberType(), index, True)]
        code = self.emit.emitVAR(
            index, 
            "for", 
            NumberType(), 
            frame.getStartLabel(), 
            frame.getEndLabel(), 
            frame
        )
        self.emit.printout(code)

        # Set function to check body
        self.function = function
        # Visit body
        self.visit(Main.body, Access(frame, [typeParam] + Symbol, False))

        # End main method
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))   
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        # Exit Scope
        frame.exitScope()    

    def visitProgram(self, ast: Program, o):

        # Init Program ZCodeClass
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))

        # Init method, var in global
        varGlobal = self.initGlobal(ast)
        # Init constructor
        self.initConstructor()
        # Init Attribute of class Zcode
        self.initAttribute(ast, varGlobal)
        # Init method of class Zcode
        self.initMethod(ast, varGlobal)
        # Init Main
        self.initMainMethod(varGlobal)
        # Printout all the buff to .j file to run
        self.emit.emitEPILOG()
    
    def visitVarDecl(self, ast, o: Access):
        
        frame: Frame = o.frame

        # create new index
        index = frame.getNewIndex()
        newVarDecl = VarZcode(ast.name.name, ast.varType, index)
        # emitVAR
        code = self.emit.emitVAR(
            in_=index,
            varName=ast.name.name,
            inType=newVarDecl,
            fromLabel=frame.getStartLabel(),
            toLabel=frame.getEndLabel(),
            frame=frame
        )
        self.emit.printout(code)

        # add new var to symbol
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

            for size in arrayType.size:
                    
                # Visit NumberLiteral
                code, _ = self.visit(NumberLiteral(size), Access(frame, o.symbol, True))
                self.emit.printout(code)

                # Take 1 int from frame for the array dimension
                self.emit.printout(self.emit.emitF2I(frame))

            # Get new array 1D from frame
            if len(arrayType.size) == 1:
                self.emit.printout(self.emit.emitNEWARRAY(arrayType.eleType, frame))
            # Get new array N-D from frame
            else:
                self.emit.printout(self.emit.emitMULTIANEWARRAY(arrayType, frame))
            # Place this var in scope
            self.emit.printout(
                self.emit.emitWRITEVAR(
                    name=ast.name.name,
                    inType=arrayType,
                    index=index,
                    frame=frame
                )
            )

        # Set type for VarDecl in buff
        self.emit.setType(o.symbol[0][-1])
        
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
        self.emit.setType(self.function)

        # End function
        if not self.Return: self.emit.printout(self.emit.emitRETURN(self.function.typ, frame))
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
        # Update LHS, RHS
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

        # No checkLHS_RHS
        _, typeArray = self.visit(ast.value[0], o)
        codeReturn, returnType = "", typeArray

        codeReturn += self.emit.emitPUSHCONST(len(ast.value), NumberType(), frame)
        codeReturn += self.emit.emitF2I(frame)

        # If 1D-array
        if not type(returnType) is ArrayType:
            codeReturn += self.emit.emitNEWARRAY(returnType, frame)
        # If ND-array
        else:
            codeReturn += self.emit.emitANEWARRAY(returnType, frame)
        
        for idx in range(len(ast.value)):

            codeReturn += self.emit.emitDUP(frame)
            codeReturn += self.emit.emitPUSHCONST(idx, NumberType(), frame)
            codeReturn += self.emit.emitF2I(frame)

            # Store value of array element
            code, _ = self.visit(ast.value[idx], o)
            codeReturn += code
            # Store array
            codeReturn += self.emit.emitASTORE(returnType, frame)
        
        # Return
        if isinstance(returnType, (BoolType, StringType, NumberType)):
                return codeReturn, ArrayType([len(ast.value)], returnType)
        return codeReturn, ArrayType([float(len(ast.value))] + returnType.size, returnType.eleType)


       
    def visitArrayCell(self, ast, o: Access):

        # Update LHS, RHS
        if o.checkTypeLHS_RHS:
            _, arr = self.visit(ast.arr, Access(o.frame, o.symbol, False, False))
            for i in ast.idx:
                self.LHS_RHS(NumberType(), i, o)
            if len(arr.size) == len(ast.idx): return None, arr.eleType
            return None, ArrayType(arr.size[len(ast.idx):], arr.eleType)   

        # No check LHS-RHS
        frame = o.frame
        codeArray, typeArray = self.visit(ast.arr, Access(o.frame, o.symbol, False, False))
        codeReturn = codeArray
        returnType = typeArray.eleType if type(typeArray) is ArrayType else typeArray
            
        lenArrayCell = len(ast.idx)
        for idx in range(lenArrayCell - 1):
            
            code, _ = self.visit(ast.idx[idx], o)
            codeReturn += code # Get idx of array code
            codeReturn += self.emit.emitF2I(frame) # Convert Float to Int
            codeReturn += self.emit.emitALOAD(typeArray, frame) # Load array[idx] address
        
        # Last index
        code, _ = self.visit(ast.idx[-1], Access(o.frame, o.symbol, False, False))
        codeReturn += code
        codeReturn += self.emit.emitF2I(frame)

        if o.isLeft:
            self.arrayCell = returnType
        else:
            typ = None
            if type(typeArray) is ArrayType:
                typ = typeArray.eleType if len(ast.idx) == len(typeArray.size) else typeArray
            else:
                typ = typeArray
            codeReturn += self.emit.emitALOAD(typ, frame)

        return codeReturn, returnType


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
        
        rhsCode, rhsType = self.visit(RHS, o)
        if rhsCode: self.emit.printout(rhsCode)
        self.emit.printout(self.emit.emitRETURN(rhsType, frame))


    def visitAssign(self, ast, o: Access):
        self.LHS_RHS(ast.lhs, ast.rhs, o)
        frame = o.frame
        rhsCode, _ = self.visit(ast.rhs, Access(frame, o.symbol, False))
        lhsCode, _ = self.visit(ast.lhs, Access(frame, o.symbol, True))

        if type(ast.lhs) is ArrayCell:
            code = self.emit.emitASTORE(self.arrayCell, frame)
            self.emit.printout(lhsCode)
            self.emit.printout(rhsCode)
            self.emit.printout(code)
        else:
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

        # Check if condition 
        LHS = BoolType()
        RHS = ast.expr 
        self.LHS_RHS(LHS, RHS, o)  
        # Check elif condition      
        for elifStmt in ast.elifStmt:
            RHS = elifStmt[0]
            self.LHS_RHS(LHS, RHS, o)   
        
        frame = o.frame
        
        # Step 1: Create Loop
        # Step 2: create exitLabel, endIfLabel
        exitLabel = frame.getNewLabel()
        endIfLabel = frame.getNewLabel()
        # Step 3: Check if condition to jump to endIfLabel
        condExpCode, _ = self.visit(ast.expr, o)
        self.emit.printout(condExpCode)
        self.emit.printout(self.emit.emitIFFALSE(endIfLabel, frame))
        # Step 4: visit body of thenStmt
        self.visit(ast.thenStmt, o)
        # Step 5: goto exit
        self.emit.printout(self.emit.emitGOTO(exitLabel, frame))
        # Step 6: Place endIfLabel here
        self.emit.printout(self.emit.emitLABEL(endIfLabel, frame))
        # Step 7: Check elifStmt
        for elifStmt in ast.elifStmt:

            # Step 7.1: Create elifLabel
            endElifLabel = frame.getNewLabel()
            # Step 7.2: Check elifCond to jump to endElifLabel
            condExpCode, _ = self.visit(elifStmt[0], o)
            self.emit.printout(condExpCode)
            self.emit.printout(self.emit.emitIFFALSE(endElifLabel, frame))
            # Step 7.3: visit elifStmt
            self.visit(elifStmt[1], o)
            # Step 7.4: goto exit
            self.emit.printout(self.emit.emitGOTO(exitLabel, frame))
            # Step 7.5: Place endElifLabel here
            self.emit.printout(self.emit.emitLABEL(endElifLabel, frame))
        
        # Step 8: Check elseStmt
        if ast.elseStmt: self.visit(ast.elseStmt, o)
        # Step 9: Place exitLabel here
        self.emit.printout(self.emit.emitLABEL(exitLabel, frame))  
        
        
        
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
        
