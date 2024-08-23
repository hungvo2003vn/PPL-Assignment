from abc import ABC
import random

class Visitor(ABC):
    def accept(self, mode: str = 'parser'):
        method_name = f'visit{self.__class__.__name__}'
        visit = getattr(self, method_name)
        return visit(mode)
    
    def visit(self, mode: str = 'parser'):
        return self.accept(mode)

    def visitZCodeProgram(self, mode): pass
    
    def visitZCodeVarDecl(self, mode): pass
    def visitZCodeFuncDecl(self, mode): pass
    def visitZCodeParamDecl(self, mode): pass

    def visitZCodeIfStmt(self, mode): pass
    def visitZCodeForStmt(self, mode): pass
    def visitZCodeBlockStmt(self, mode): pass
    def visitZCodeBreakStmt(self, mode): pass
    def visitZCodeContinueStmt(self, mode): pass
    def visitZCodeReturnStmt(self, mode): pass
    def visitZCodeFuncCallStmt(self, mode): pass
    def visitZCodeAssignStmt(self, mode): pass

    def visitZCodeExpression(self, mode): pass
    def visitZCodeArrayCell(self, mode): pass
    def visitZCodeArrayLit(self, mode): pass
    def visitZCodeNumberLit(self, mode): pass
    def visitZCodeStringLit(self, mode): pass
    def visitZCodeBooleanLit(self, mode): pass
    def visitZCodeID(self, mode): pass

    def visitZCodeComment(self, mode): pass


class ZCodeProgram(Visitor):
    def __init__(self, mode: str = 'parser'):
        mode = mode.lower()
        if mode in ['ast', 'parser']:
            self.mode = mode
            self.depth = 0
            self.scope = 0
        
        else:
            raise ValueError("Must be in parser mode or ast mode (case - insensitive)")

    def gen(self):
        return self.visit(self.mode)

    def getExprList(self, mode, min, max):
        if min > max:
            raise ValueError("min must be smaller or equal to max")
        
        return "{}".format(
            ", ".join([self.visitZCodeExpression(mode) for i in range(random.randint(min, max))])
        )
    
    def getStmt(self, mode):
        stmtList = ["visitZCodeVarDecl(mode)", "visitZCodeAssignStmt(mode)", "visitZCodeIfStmt(mode)", "visitZCodeForStmt(mode)", 
                    "visitZCodeBreakStmt(mode)", "visitZCodeContinueStmt(mode)", "visitZCodeReturnStmt(mode)", 
                    "visitZCodeBlockStmt(mode)", "visitZCodeFuncCallStmt(mode)"]
        return eval("self.{}".format(random.choice(stmtList)))
    
    def getOperand(self, mode):
        literal = ["visitZCodeID(mode)", "visitZCodeNumberLit(mode)", "visitZCodeStringLit(mode)", "visitZCodeBooleanLit(mode)"]
        return eval("self.{}".format(random.choice(literal)))
    
    def visitZCodeProgram(self, mode):
        numDecls = random.randint(1, 5)
        prog = ''
        decls = ['visitZCodeVarDecl(mode)', 'visitZCodeFuncDecl(mode)', 'visitZCodeComment(mode)']
        for i in range(numDecls):
            prog += eval("self.{}".format(
                random.choice(decls) if mode == 'parser' else random.choice(decls[:-1])
            )) + '\n'
        
        return prog
    
    def visitZCodeVarDecl(self, mode):
        iden = self.visitZCodeID(mode)
        keywords = ["dynamic", "var", "string", "bool", "number"]
        if mode == 'parser':
            kw = random.choice(keywords)
            expr = (' <- ' + self.visitZCodeExpression(mode) if random.randint(0, 1) == 1 else "") + ("" if random.randint(0, 1) == 0 else f" {self.visitZCodeComment(mode)}")
            if random.randint(0, 1) == 0:
                len = random.randint(1, 3)
                arr = "[{}]".format(
                    ",".join([self.visitZCodeNumberLit(mode) for i in range(len)])
                )
                return "{} {}{}{}".format(kw, iden, arr, expr)
            
            else:
                return "{} {}{}".format(kw, iden, expr)
        
        else:
            is_array_type = random.randint(0, 1) == 0
            kw = random.choice(keywords) if is_array_type == False else random.choice(keywords[2:])
            expr = ' <- ' + self.visitZCodeExpression(mode) if random.randint(0, 1) == 1 or kw == "var" else ""
            if is_array_type:
                len = random.randint(1, 3)
                arr = "[{}]".format(
                    ",".join([self.visitZCodeNumberLit(mode) for i in range(len)])
                )
                return "{} {}{}{}".format(kw, iden, arr, expr)
            
            else:
                return "{} {}{}".format(kw, iden, expr)

    def visitZCodeFuncDecl(self, mode):
        self.scope += 1
        tabarr = ['\t'] * self.scope
        has_newline = '\n' if random.randint(0, 1) == 1 else ''
        new_line_end = '\n' if random.randint(0, 1) == 1 else ''
        choices = random.randint(0, 2) == 0
        stmt = self.visitZCodeReturnStmt(mode) if choices == 0 else (self.visitZCodeBlockStmt(mode) if choices == 1 else '')
        funcDecl = "func {} ({}){}{}{}{}".format(
            self.visitZCodeID(mode),
            ', '.join([x for x in [self.visitZCodeParamDecl(mode) for i in range(random.randint(0, 3))]]),
            has_newline,
            ''.join(tabarr),
            stmt,
            new_line_end
        )
        self.scope -= 1
        return funcDecl
    
    def visitZCodeParamDecl(self, mode):
        iden = self.visitZCodeID(mode)
        keywords = ["dynamic", "var", "string", "bool", "number"]
        if mode == 'parser':
            kw = random.choice(keywords)
            if random.randint(0, 1) == 0:
                len = random.randint(1, 3)
                arr = "[{}]".format(
                    ",".join([self.visitZCodeNumberLit(mode) for i in range(len)])
                )
                return "{} {}{}".format(kw, iden, arr)
            
            else:
                return "{} {}".format(kw, iden)
        
        else:
            is_array_type = random.randint(0, 1) == 0
            kw = random.choice(keywords[2:])
            if is_array_type:
                len = random.randint(1, 3)
                arr = "[{}]".format(
                    ",".join([self.visitZCodeNumberLit(mode) for i in range(len)])
                )
                return "{} {}{}".format(kw, iden, arr)
            
            else:
                return "{} {}".format(kw, iden)

    def visitZCodeIfStmt(self, mode):
        tabarr = ['\t'] * self.scope
        has_new_line = '\n' if random.randint(0, 1) == 0 else ''
        if_stmt = "if ({}){}{}".format(
            self.visitZCodeExpression(mode),
            has_new_line,
            (' ' if has_new_line == '' else ''.join(tabarr)) + self.getStmt(mode) 
        )
        numElif = random.randint(0, 5)
        for i in range(numElif):
            has_new_line = '\n' if random.randint(0, 1) == 0 else ''
            if_stmt += "\n{}elif ({}){}{}".format(
                ''.join(tabarr),
                self.visitZCodeExpression(mode),
                has_new_line,
                (' ' if has_new_line == '' else ''.join(tabarr)) + self.getStmt(mode)
            )
        
        if_stmt += "\n{}else {}".format(
            ''.join(tabarr),
            self.getStmt(mode)
        ) if random.randint(0, 1) == 1 else ""
        return if_stmt
    
    def visitZCodeForStmt(self, mode):
        self.scope += 1
        tabarr = ['\t'] * self.scope
        for_stmt = "for {} until {} by {}\n{}{}".format(
            self.visitZCodeID(mode),
            self.visitZCodeExpression(mode),
            self.visitZCodeExpression(mode),
            ''.join(tabarr),
            self.getStmt(mode)
        )
        self.scope -= 1
        return for_stmt
    
    def visitZCodeBlockStmt(self, mode):
        self.scope += 1
        block_stmt = ''
        tabarr = ['\t'] * self.scope
        if mode == 'ast':
            block_stmt = "begin\n{}{}end".format(
                ''.join([stmt for stmt in [''.join(tabarr) + self.getStmt(mode) + '\n' for i in range(random.randint(0, 3))]]),
                ''.join(tabarr[:-1])
            )

        else: 
            block_stmt = "begin\n{}{}end".format(
                ''.join([stmt for stmt in [''.join(tabarr) + (self.getStmt(mode) if random.randint(0, 1) == 0 else self.visitZCodeComment(mode)) + '\n' for i in range(random.randint(0, 3))]]),
                ''.join(tabarr[:-1])
            )

        self.scope -= 1
        return block_stmt
    
    def visitZCodeBreakStmt(self, mode):
        return "break"
    
    def visitZCodeContinueStmt(self, mode):
        return "continue"
    
    def visitZCodeReturnStmt(self, mode):
        return "return{}".format(" " + self.visitZCodeExpression(mode) if random.randint(0, 1) == 1 else "")
    
    def visitZCodeFuncCallStmt(self, mode):
        return self.visitZCodeFuncCall(mode)
    
    def visitZCodeAssignStmt(self, mode):
        if mode == 'parser':
            return "{}{}".format(
                self.visitZCodeID(mode) if random.randint(0, 1) == 0 else self.visitZCodeArrayCell(mode),
                ' <- ' + self.visitZCodeExpression(mode)
        )

        return "{}{}".format(
            self.visitZCodeID(mode) if random.randint(0, 1) == 0 else (self.visitZCodeID(mode) + '[{}]'.format(self.getExprList(mode, 1, 3))),
            ' <- ' + self.visitZCodeExpression(mode)
        )

    def visitZCodeExpression(self, mode):
        if self.depth == 5:
            return self.getOperand(mode)
        
        opt = random.randint(0, 6)
        self.depth += 1
        if opt == 0:
            return random.choice(['- ', 'not ']) + self.visitZCodeExpression(mode)
        
        elif opt == 1:
            return '(' + self.visitZCodeExpression(mode) + ')'

        elif opt == 2:
            return self.visitZCodeExpression(mode) + f" {random.choice(['+', '-', '*', '/', '%', '>', '<', '<=', '>=', '!=', '==', '=', 'and', 'or', '...'])} " + self.visitZCodeExpression(mode)
        
        elif opt == 3:
            return self.getOperand(mode)

        elif opt == 4:
            return self.visitZCodeArrayLit(mode)
        
        elif opt == 5:
            return self.visitZCodeFuncCall(mode)
        
        else:
            return self.visitZCodeArrayCell(mode)
    
    def visitZCodeFuncCall(self, mode):
        return "{}({})".format(self.visitZCodeID(mode), self.getExprList(mode, 0, 3))
    
    def visitZCodeArrayCell(self, mode):
        return "{}[{}]".format(random.choice([self.visitZCodeID(mode), self.visitZCodeFuncCall(mode)]), self.getExprList(mode, 1, 3))
    
    def visitZCodeArrayLit(self, mode):
        return "[{}]".format(self.getExprList(mode, 1, 3))
    
    def visitZCodeNumberLit(self, mode):
        numLit = ""
        if mode == 'parser':
            digitSet = '0123456789'
            decPart = '.' + "".join([x for x in [digitSet[random.randint(0, len(digitSet) - 1)] for i in range(0, 3)]])
            sign = random.randint(0, 2)
            expPart = ('e' if random.randint(0, 1) == 0 else 'E') + ('+' if sign == 0 else ('-' if sign == 1 else '')) + "".join([x for x in [digitSet[random.randint(0, len(digitSet) - 1)] for i in range(1, 3)]])
            for i in range(random.randint(1, 3)):
                numLit = numLit + digitSet[random.randint(0, len(digitSet) - 1)]
                
            numLit += (decPart if random.randint(0, 1) == 1 else '') + (expPart if random.randint(0, 1) == 1 else '')
            while True:
                if numLit[0] == '0' and (len(numLit) > 1 and numLit[1] not in ['.', 'e', 'E']):
                    numLit = numLit[1:]
                
                else:
                    break
        else:
            numLit = str(round(random.uniform(0, 100), 2))
        
        return numLit
    
    def visitZCodeStringLit(self, mode):
        strLit = '\"'
        if mode == 'parser':
            spec_quotes = '\'\"'
            for i in range(random.randint(1, 5)):
                opt = random.randint(0, 1)
                strLit = strLit + (chr(random.choice([x for x in range(32, 127) if x not in [34, 39, 92]])) if opt == 1 else spec_quotes)
        
        else:
            for i in range(random.randint(1, 5)):
                strLit += chr(random.choice(list(range(65, 91)) + list(range(97, 123))))
    
        strLit += '\"'
        return strLit
    
    def visitZCodeBooleanLit(self, mode):
        return "true" if random.randint(0, 1) == 1 else "false"

    def visitZCodeID(self, mode):
        charSet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
        iden = charSet[random.randint(0, len(charSet[:-11]) - 1)]
        for i in range(random.randint(1, 3)):
            iden = iden + charSet[random.randint(0, len(charSet) - 1)]
        
        kw = ['break', 'continue', 'if', 'else', 'elif', 'for', 'until', 'by', 'true', 'false', 'number', 'bool', 'string',
              'return', 'dynamic', 'var', 'not', 'and', 'or', 'begin', 'end', 'func']
        return iden if mode == 'parser' else (iden if iden not in kw else self.visitZCodeID(mode))

    def visitZCodeComment(self, mode):
        cmt = '## '
        for i in range(random.randint(1, 20)):
            cmt = cmt + random.choice([chr(x) for x in range(32, 127) if x not in [39, 92]])
        
        return cmt