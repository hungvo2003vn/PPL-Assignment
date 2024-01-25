from abc import ABC, abstractmethod, ABCMeta
from typing import List, Tuple


class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def accept(self, v, param):
        method_name = 'visit{}'.format(self.__class__.__name__)
        visit = getattr(v, method_name)
        return visit(self, param)

class Stmt(AST): pass
class Expr(Stmt): pass
class Type(AST): pass
class Decl(AST): pass
class LHS(Expr): pass

# Types

class NumberType(Type):
    def __str__(self):
        return self.__class__.__name__ + "()"

class BooleanType(Type):
    def __str__(self):
        return self.__class__.__name__  + "()"

class StringType(Type):
    def __str__(self):
        return self.__class__.__name__  + "()"

#! dimensions là danh sách của mảng number lit
class ArrayType(Type):
    def __init__(self, dimensions: List[int], typ: Type):
        self.dimensions = dimensions
        self.typ = typ

    def __str__(self):
        return "ArrayType([{}], {})".format(", ".join([str(dimen) for dimen in self.dimensions]), str(self.typ))

# Expressions

class BinExpr(Expr):
    def __init__(self, op: str, left: Expr, right: Expr):
        self.op = op
        self.left = left
        self.right = right

    def __str__(self):
        return "BinExpr(\"{}\", {}, {})".format(self.op, str(self.left), str(self.right))

class UnExpr(Expr):
    def __init__(self, op: str, val: Expr):
        self.op = op
        self.val = val

    def __str__(self):
        return "UnExpr(\"{}\", {})".format(self.op, str(self.val))

class Id(LHS):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return "Id(\"{}\")".format(self.name)

#! toán tử index trong expr7
class ArrayCell(LHS):
    def __init__(self, name: Expr, cell: List[Expr]):
        self.name = name
        self.cell = cell

    def __str__(self):
        return "ArrayCell({}, [{}])".format(self.name, ", ".join([str(expr) for expr in self.cell]))

class NumberLit(Expr):
    def __init__(self, val: float):
        self.val = val

    def __str__(self):
        return "NumberLit({})".format(self.val)

class StringLit(Expr):
    def __init__(self, val: str):
        self.val = val

    def __str__(self):
        return "StringLit(\"{}\")".format(self.val)

class BooleanLit(Expr):
    def __init__(self, val: bool):
        self.val = val

    def __str__(self):
        return "BooleanLit({})".format("True" if self.val else "False")

#! array lit
class ArrayLit(Expr):
    def __init__(self, explist: List[Expr]):
        self.explist = explist

    def __str__(self):
        return "ArrayLit([{}])".format(", ".join([str(exp) for exp in self.explist]))

#! gọi hàm trong expr
class FuncCall(Expr):
    def __init__(self, name: str, args: List[Expr]):
        self.name = name
        self.args = args

    def __str__(self):
        return "FuncCall({}, [{}])".format(self.name, ", ".join([str(expr) for expr in self.args]))

# Statements

class AssignStmt(Stmt):
    def __init__(self, lhs: LHS, rhs: Expr):
        self.lhs = lhs
        self.rhs = rhs

    def __str__(self):
        return "AssignStmt({}, {})".format(str(self.lhs), self.rhs)

class BlockStmt(Stmt):
    def __init__(self, body: List[Stmt or Decl]):
        self.body = body

    def __str__(self):
        return "BlockStmt([\n\t{}])".format(",\n\t".join([str(body) for body in self.body]))

class IfStmt(Stmt):
    def __init__(self, cond: Expr, tstmt: Stmt, 
                        Elif: list[list[Expr or Stmt]], 
                        fstmt: Stmt or None = None):
        self.cond = cond
        self.tstmt = tstmt
        self.fstmt = fstmt
        self.Elif = Elif
    def __str__(self):
        return "IfStmt({}, {}, [{}] ,{})".format(str(self.cond), str(self.tstmt),
                                            ",".join(["[" + str(Elif[0]) + "," + str(Elif[1]) + "]" for Elif in self.Elif]), 
                                           str(self.fstmt) if self.fstmt else "")

class ForStmt(Stmt):
    def __init__(self, init: LHS, cond: Expr, upd: Expr, stmt: Stmt):
        self.init = init
        self.cond = cond
        self.upd = upd
        self.stmt = stmt

    def __str__(self):
        return "ForStmt({}, {}, {}, {})".format(str(self.init), str(self.cond), str(self.upd), str(self.stmt))

class BreakStmt(Stmt):
    def __str__(self):
        return "BreakStmt()"

class ContinueStmt(Stmt):
    def __str__(self):
        return "ContinueStmt()"

class ReturnStmt(Stmt):
    def __init__(self, expr: Expr = None):
        self.expr = expr

    def __str__(self):
        return "ReturnStmt({})".format(str(self.expr) if self.expr else "")

class CallStmt(Stmt):
    def __init__(self, name: str, args: List[Expr]):
        self.name = name
        self.args = args

    def __str__(self):
        return "CallStmt({}, [{}])".format(self.name, ", ".join([str(expr) for expr in self.args]))

# Declarations

class VarDecl(Decl):
    def __init__(self, name: str, typ: Type, init: Expr or None = None):
        self.name = name
        self.typ = typ
        self.init = init

    def __str__(self):
        return "VarDecl({}, {}{})".format(self.name, str(self.typ), ", " + str(self.init) if self.init else "")

class ImplicitDynamicDecl(Decl):
    def __init__(self, name: str, init: Expr or None = None):
        self.name = name
        self.init = init

    def __str__(self):
        return "ImplicitDynamicDecl({}, {})".format(self.name, ", " + str(self.init) if self.init else "")

class ImplicitVarDecl(Decl):
    def __init__(self, name: str, init: Expr or None = None):
        self.name = name
        self.init = init

    def __str__(self):
        return "ImplicitVarDecl({}, {})".format(self.name, ", " + str(self.init) if self.init else "")



class ParamDecl(Decl):
    # if ImplicitDynamic thì type = NONE
    def __init__(self, name: str, typ: Type = None):
        self.name = name
        self.typ = typ

    def __str__(self):
        return "ParamDecl(\"{}\", {})".format(self.name, str(self.typ))


class FuncDecl(Decl):
    def __init__(self, name: str, params: List[ParamDecl], body: Stmt = None):
        self.name = name
        self.params = params
        self.body = body

    def __str__(self):
        return "FuncDecl({}, [{}], {})".format(self.name, ", ".join([str(param) for param in self.params]), str(self.body))

# Program


class Program(AST):
    def __init__(self, decls: List[Decl]):
        self.decls = decls

    def __str__(self):
        return "str(Program([\n\t{}\n]))".format(",\n\t".join([str(decl) for decl in self.decls]))
