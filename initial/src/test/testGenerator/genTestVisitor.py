from abc import ABC
import random

class Visitor(ABC):
    def accept(self, mode: str = 'parser'):
        method_name = f'visit{self.__class__.__name__}'
        visit = getattr(self, method_name)
        return visit(mode)
    
    def visit(self, mode: str = 'parser'):
        return self.accept(mode)

    def visitProgram(self, mode): pass
    
    def visitVarDecl(self, mode): pass
    def visitFuncDecl(self, mode): pass
    def visitParamDecl(self, mode): pass

    def visitIfStmt(self, mode): pass
    def visitForStmt(self, mode): pass
    def visitBlockStmt(self, mode): pass
    def visitBreakStmt(self, mode): pass
    def visitContinueStmt(self, mode): pass
    def visitReturnStmt(self, mode): pass
    def visitFuncCallStmt(self, mode): pass
    def visitAssignStmt(self, mode): pass

    def visitExpression(self, mode): pass
    def visitArrayCell(self, mode): pass
    def visitArrayLit(self, mode): pass
    def visitNumberLit(self, mode): pass
    def visitStringLit(self, mode): pass
    def visitBooleanLit(self, mode): pass
    def visitID(self, mode): pass

    def visitComment(self, mode): pass


class Program(Visitor):
    def __init__(self, mode: str = 'parser'):
        mode = mode.lower()
        if mode in ['ast', 'parser']:
            self.mode = mode
            self.depth = 0
            self.scope = 0
        
        else:
            raise ValueError(f'{mode=} must be parser mode or ast mode (case - insensitive)')

    def gen(self):
        return self.visit(self.mode)

    def getExprList(self, mode, min, max):
        if min > max:
            raise ValueError(f"{min =} must be smaller than or equal to {max =}")
        tmp_str = ", "
        return f"{tmp_str.join([self.visitExpression(mode) for i in range(random.randint(min, max))])}"
    
    def getStmt(self, mode):
        stmtList = ["visitVarDecl(mode)", "visitAssignStmt(mode)", "visitIfStmt(mode)", "visitForStmt(mode)", 
                    "visitBreakStmt(mode)", "visitContinueStmt(mode)", "visitReturnStmt(mode)", 
                    "visitBlockStmt(mode)", "visitFuncCallStmt(mode)"]
        return eval(f"self.{random.choice(stmtList)}")
    
    def getOperand(self, mode):
        literal = ["visitID(mode)", "visitNumberLit(mode)", "visitStringLit(mode)", "visitBooleanLit(mode)"]
        return eval(f"self.{random.choice(literal)}")
    
    def visitProgram(self, mode):
        numDecls = random.randint(1, 5)
        prog = ''
        decls = ['visitVarDecl(mode)', 'visitFuncDecl(mode)', 'visitComment(mode)']
        for i in range(numDecls):
            tmp_str = 'parser'
            prog += eval(f'self.{random.choice(decls) if mode == tmp_str else random.choice(decls[:-1])}') + '\n'
        
        return prog
    
    def visitVarDecl(self, mode):
        iden = self.visitID(mode)
        keywords = ["dynamic", "var", "string", "bool", "number"]
        if mode == 'parser':
            kw = random.choice(keywords)
            expr = (' <- ' + self.visitExpression(mode) if random.randint(0, 1) == 1 else "") + ("" if random.randint(0, 1) == 0 else f" {self.visitComment(mode)}")
            if random.randint(0, 1) == 0:
                len = random.randint(1, 3)
                arr = f"[{','.join([self.visitNumberLit(mode) for i in range(len)])}]"
                return f"{kw} {iden}{arr}{expr}"
            
            else:
                return f"{kw} {iden}{expr}"
        
        else:
            is_array_type = random.randint(0, 1) == 0
            kw = random.choice(keywords) if is_array_type == False else random.choice(keywords[2:])
            expr = ' <- ' + self.visitExpression(mode) if random.randint(0, 1) == 1 else ""
            if is_array_type:
                len = random.randint(1, 3)
                arr = f"[{','.join([self.visitNumberLit(mode) for i in range(len)])}]"

                return f"{kw} {iden}{arr}{expr}"
            
            else:
                return f"{kw} {iden}{expr}"

    def visitFuncDecl(self, mode):
        self.scope += 1
        tabarr = ['\t'] * self.scope
        has_newline = '\n' if random.randint(0, 1) == 1 else ''
        new_line_end = '\n' if random.randint(0, 1) == 1 else ''
        choices = random.randint(0, 2) == 0
        stmt = self.visitReturnStmt(mode) if choices == 0 else (self.visitBlockStmt(mode) if choices == 1 else '')
        funcDecl = f"func {self.visitID(mode)} ({', '.join([x for x in [self.visitParamDecl(mode) for i in range(random.randint(0, 3))]])}){has_newline}{''.join(tabarr)}{stmt}{new_line_end}"
        self.scope -= 1
        return funcDecl
    
    def visitParamDecl(self, mode):
        iden = self.visitID(mode)
        keywords = ["dynamic", "var", "string", "bool", "number"]
        if mode == 'parser':
            kw = random.choice(keywords)
            if random.randint(0, 1) == 0:
                len = random.randint(1, 3)
                arr = f"[{','.join([self.visitNumberLit(mode) for i in range(len)])}]"
                return f"{kw} {iden}{arr}"
            
            else:
                return f"{kw} {iden}"
        
        else:
            is_array_type = random.randint(0, 1) == 0
            kw = random.choice(keywords) if is_array_type == False else random.choice(keywords[2:])
            if is_array_type:
                len = random.randint(1, 3)
                arr = f"[{','.join([self.visitNumberLit(mode) for i in range(len)])}]"

                return f"{kw} {iden}{arr}"
            
            else:
                return f"{kw} {iden}"

    def visitIfStmt(self, mode):
        if_stmt = f"if {self.visitExpression(mode)} {self.getStmt(mode)}"
        numElif = random.randint(0, 5)
        tabarr = ['\t'] * self.scope
        for i in range(numElif):
            if_stmt += f"\n{''.join(tabarr)}elif {self.visitExpression(mode)} {self.getStmt(mode)}"
        
        if_stmt += f"\n{''.join(tabarr)}else {self.getStmt(mode)}" if random.randint(0, 1) == 1 else ""
        return if_stmt
    
    def visitForStmt(self, mode):
        self.scope += 1
        tabarr = ['\t'] * self.scope
        for_stmt = f"for {self.visitID(mode)} until {self.visitExpression(mode)} by {self.visitExpression(mode)}\n{''.join(tabarr)}{self.getStmt(mode)}"
        self.scope -= 1
        return for_stmt
    
    def visitBlockStmt(self, mode):
        self.scope += 1
        block_stmt = ''
        null_char = ''
        endline = '\n'
        tabarr = ['\t'] * self.scope
        if mode == 'ast':
            block_stmt = f"begin\n{''.join([stmt for stmt in [f'{null_char.join(tabarr)}{self.getStmt(mode)}{endline}' for i in range(random.randint(0, 3))]])}{''.join(tabarr[:-1])}end"

        else: 
            block_stmt = f"begin\n{''.join([stmt for stmt in [f'{null_char.join(tabarr)}{self.getStmt(mode) if random.randint(0, 1) == 0 else self.visitComment(mode)}{endline}' for i in range(random.randint(0, 3))]])}{''.join(tabarr[:-1])}end"

        self.scope -= 1
        return block_stmt
    
    def visitBreakStmt(self, mode):
        return "break"
    
    def visitContinueStmt(self, mode):
        return "continue"
    
    def visitReturnStmt(self, mode):
        return f'return{" " + self.visitExpression(mode) if random.randint(0, 1) == 1 else ""}'
    
    def visitFuncCallStmt(self, mode):
        return self.visitFuncCall(mode)
    
    def visitAssignStmt(self, mode):
        return f"{self.visitID(mode) if random.randint(0, 1) == 0 else self.visitArrayCell(mode)}{' <- ' + self.visitExpression(mode)}"

    def visitExpression(self, mode):
        if self.depth == 5:
            return self.getOperand(mode)
        
        opt = random.randint(0, 6)
        self.depth += 1
        if opt == 0:
            return random.choice(['+ ', '- ', 'not ']) + self.visitExpression(mode)
        
        elif opt == 1:
            return '(' + self.visitExpression(mode) + ')'

        elif opt == 2:
            return self.visitExpression(mode) + f" {random.choice(['+', '-', '*', '/', '%', '>', '<', '<=', '>=', '!=', '==', '=', 'and', 'or', '...'])} " + self.visitExpression(mode)
        
        elif opt == 3:
            return self.getOperand(mode)

        elif opt == 4:
            return self.visitArrayLit(mode)
        
        elif opt == 5:
            return self.visitFuncCall(mode)
        
        else:
            return self.visitArrayCell(mode)
    
    def visitFuncCall(self, mode):
        return "{}({})".format(self.visitID(mode), self.getExprList(mode, 0, 3))
    
    def visitArrayCell(self, mode):
        return "{}[{}]".format(random.choice([self.visitID(mode), self.visitFuncCall(mode)]), self.getExprList(mode, 1, 3))
    
    def visitArrayLit(self, mode):
        return "[{}]".format(self.getExprList(mode, 1, 3))
    
    def visitNumberLit(self, mode):
        digitSet = '0123456789'
        decPart = '.' + "".join([x for x in [digitSet[random.randint(0, len(digitSet) - 1)] for i in range(0, 3)]])
        sign = random.randint(0, 2)
        expPart = ('e' if random.randint(0, 1) == 0 else 'E') + ('+' if sign == 0 else ('-' if sign == 1 else '')) + "".join([x for x in [digitSet[random.randint(0, len(digitSet) - 1)] for i in range(1, 3)]])
        numLit = ""
        for i in range(random.randint(1, 3)):
            numLit = numLit + digitSet[random.randint(0, len(digitSet) - 1)]
            
        numLit += (decPart if random.randint(0, 1) == 1 else '') + (expPart if random.randint(0, 1) == 1 else '')
        while True:
            if numLit[0] == '0' and (len(numLit) > 1 and numLit[1] not in ['.', 'e', 'E']):
                numLit = numLit[1:]
            
            else:
                break
        
        return numLit
    
    def visitStringLit(self, mode):
        strLit = '\"'
        spec_quotes = '\'\"'
        for i in range(random.randint(1, 5)):
            opt = random.randint(0, 1)
            strLit = strLit + (chr(random.choice([x for x in range(32, 127) if x not in [39, 92]])) if opt == 1 else spec_quotes)
    
        strLit += '\"'
        return strLit
    
    def visitBooleanLit(self, mode):
        return "true" if random.randint(0, 1) == 1 else "false"

    def visitID(self, mode):
        charSet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
        iden = charSet[random.randint(0, len(charSet[:-11]) - 1)]
        for i in range(random.randint(1, 3)):
            iden = iden + charSet[random.randint(0, len(charSet) - 1)]
        
        return iden

    def visitComment(self, mode):
        cmt = '## '
        for i in range(random.randint(1, 20)):
            cmt = cmt + random.choice([chr(x) for x in range(32, 127) if x not in [39, 92]])
        
        return cmt