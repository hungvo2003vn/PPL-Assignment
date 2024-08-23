import sys
from abc import ABC
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener
import random
from genTestVisitor import ZCodeProgram

for path in ['./test/', './test/testcases/', './main/zcode/parser/', './main/zcode/utils/', './main/zcode/astgen/', 
             './main/zcode/checker/', './main/zcode/codegen/', '../target/']:
    sys.path.append(path)

import platform
if platform.system() != 'Windows':
    sys.path.append('../target/main/zcode/parser/')

from ZCodeLexer import ZCodeLexer
from ZCodeParser import ZCodeParser
from lexererr import *
from ASTGeneration import *
# from StaticChecker import *
# from StaticError import *
# from CodeGenerator import *

Lexer = ZCodeLexer
Parser = ZCodeParser

class TestSource:
    @staticmethod
    def makeSource(inputStr, num):
        filename = './test/testcases/' + str(num) + ".txt"
        file = open(filename, "w")
        file.write(inputStr)
        file.close()
        return FileStream(filename)

class TestCaseGenerator(ABC):
    pass

class LexerGenerator(TestCaseGenerator):
    def __init__(self, inputFile: str = './test/LexerSuite.py'):
        self.inputFile = inputFile
        self.importLib()
    
    def importLib(self):
        with open(self.inputFile, 'w') as f:
            importLine = """import unittest\nfrom TestUtils import TestLexer\n\nclass LexerSuite(unittest.TestCase):"""
            f.write(importLine)
            f.close()

    @staticmethod
    def printLexeme(lexer):
        dest = ""
        tok = lexer.nextToken()
        while tok.type != Token.EOF:
            try:
                dest += tok.text + ","
                tok = lexer.nextToken()
            
            except (ErrorToken, UncloseString, IllegalEscape) as err:
                dest += err.message
                return dest
        
        dest += "<EOF>"
        return dest

    def genID(self, num):
        charSet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_@#$^&'
        iden = ""
        with open(self.inputFile, 'a') as f:
            for i in range(random.randint(1, 10)):
                iden = iden + charSet[random.randint(0, len(charSet) - 1)]
            
            lexer = Lexer(TestSource.makeSource(iden, num))
            output = ''
            try:
                output += LexerGenerator.printLexeme(lexer)

            except (ErrorToken, UncloseString, IllegalEscape) as err:
                output += err.message
            
            finally:
                test = """\n\tdef test_{}(self):\n\t\tself.assertTrue(TestLexer.test(\"{}\", \"{}\", {}))\n""".format(str(num), iden, output, str(num))
                f.write(test)
                f.close()
    
    def genNumberLit(self, num):
        digitSet = '0123456789'
        decPart = '.' + "".join([x for x in [digitSet[random.randint(0, len(digitSet) - 1)] for i in range(0, 3)]])
        sign = random.randint(0, 2)
        expPart = ('e' if random.randint(0, 1) == 0 else 'E') + ('+' if sign == 0 else ('-' if sign == 1 else '')) + "".join([x for x in [digitSet[random.randint(0, len(digitSet) - 1)] for i in range(1, 3)]])
        numLit = ""
        with open(self.inputFile, 'a') as f:
            for i in range(random.randint(1, 3)):
                numLit = numLit + digitSet[random.randint(0, len(digitSet) - 1)]
            
            numLit += (decPart if random.randint(0, 1) == 1 else '') + (expPart if random.randint(0, 1) == 1 else '')
            while True:
                if numLit[0] == '0' and (len(numLit) > 1 and numLit[1] not in ['.', 'e', 'E']):
                    numLit = numLit[1:]
                
                else:
                    break
            
            lexer = Lexer(TestSource.makeSource(numLit, num))
            output = ''
            try:
                output += LexerGenerator.printLexeme(lexer)

            except (ErrorToken, UncloseString, IllegalEscape) as err:
                output += err.message
            
            finally:
                test = """\n\tdef test_{}(self):\n\t\tself.assertTrue(TestLexer.test(\"{}\", \"{}\", {}))\n""".format(str(num), numLit, output, str(num))
                f.write(test)
                f.close()

    def genStringLit(self, num):
        strLit = '"'
        spec_quotes = '\'"'
        with open(self.inputFile, 'a') as f:
            for i in range(random.randint(0, 5)):
                opt = random.randint(0, 1)
                ch = chr(random.choice([8, 9, 10, 12] + [x for x in range(32, 127) if x not in [34, 92]])) if opt == 1 else spec_quotes
                strLit = strLit + ch
            
            if len(strLit) >= 2:
                with_err = random.randint(0, 2)
                idx = random.randint(1, len(strLit) - 1)
                while strLit[idx] == '"':
                    idx = random.randint(1, len(strLit) - 1)

                if with_err == 1:
                    opt = random.randint(0, 1)
                    if opt == 0:
                        chList = list(strLit)
                        chList.insert(idx, '\n')
                        strLit = "".join([ch for ch in chList])
                        strLit += '"'
                    
                    else:
                        strLit += ' '
                
                elif with_err == 2:
                    invalid_char = 'acdeghijklmopqsuvwxyz'
                    chList = list(strLit)
                    chList.insert(idx, f'\\\\{invalid_char[random.randint(0, len(invalid_char) - 1)]}')
                    strLit = "".join([ch for ch in chList])    
                    strLit += '"'
                
                else:
                    strLit += '"'
            
            else:
                strLit += '"'

            inp = strLit.replace('\\\\', '\\')
            lexer = Lexer(TestSource.makeSource(inp, num))
            output = ''
            try:
                output += LexerGenerator.printLexeme(lexer)

            except (ErrorToken, UncloseString, IllegalEscape) as err:
                output += err.message
            
            finally:
                output = output.replace('\\', '\\\\')
                if output[0] == "'":
                    output = output[1:]
                    output = "\\'" + output

                test = """\n\tdef test_{}(self):\n\t\tself.assertTrue(TestLexer.test(\'\'\'{}\'\'\', \'\'\'{}\'\'\', {}))\n""".format(str(num), strLit, output, str(num))
                f.write(test)
                f.close()
    
    def genComment(self, num: int):
        cmt = '## '
        with open(self.inputFile, 'a') as f:
            for i in range(random.randint(1, 20)):
                ch = chr(random.choice([x for x in range(32, 127) if x not in [39, 92]]))
                cmt = cmt + ch

            lexer = Lexer(TestSource.makeSource(cmt, num))
            output = ''
            try:
                output += LexerGenerator.printLexeme(lexer)

            except (ErrorToken, UncloseString, IllegalEscape) as err:
                output += err.message
            
            finally:
                test = """\n\tdef test_{}(self):\n\t\tself.assertTrue(TestLexer.test(\'\'\'{}\'\'\', \'\'\'{}\'\'\', {}))\n""".format(str(num), cmt, output, str(num))
                f.write(test)
                f.close()
    
    def gen(self, test: int):
        genList = ['genID', 'genNumberLit', 'genStringLit', 'genComment']
        opt = random.randint(0, len(genList) - 1)
        exec(f'self.{genList[opt]}({test})')


class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line " + str(line) +
                              " col " + str(column) + ": " + offendingSymbol.text)


NewErrorListener.INSTANCE = NewErrorListener()


class SyntaxException(Exception):
    def __init__(self, msg):
        self.message = msg

class ParserGenerator(TestCaseGenerator):
    def __init__ (self, inputFile = './test/ParserSuite.py'):
        self.inputFile = inputFile
        self.importLib()
        self.prog = ZCodeProgram('parser')
    
    def importLib(self):
        with open(self.inputFile, 'w') as f:
            importLine = """import unittest\nfrom TestUtils import TestParser\n\nclass ParserSuite(unittest.TestCase):"""
            f.write(importLine)
            f.close()
    
    @staticmethod
    def createErrorListener():
        return NewErrorListener.INSTANCE

    @staticmethod
    def genResult(inputfile):
        lexer = Lexer(inputfile)
        listener = ParserGenerator.createErrorListener()
        tokens = CommonTokenStream(lexer)
        parser = Parser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        result = ''
        try:
            parser.program()
            result = "successful"
        except SyntaxException as f:
            result = f.message
        except Exception as e:
            result = str(e)
        finally:
            return result
    
    def gen(self, num: int):
        with open(self.inputFile, 'a') as f:
            program = '\n' + self.prog.gen()
            input = TestSource.makeSource(program, num)
            expect = ParserGenerator.genResult(input)
            test = """\n\tdef test_{}(self):\n\t\tinput = \'\'\'{}\'\'\'\n\t\texpect = \'\'\'{}\'\'\'\n\t\tself.assertTrue(TestParser.test(input, expect, {}))\n""".format(str(num), program, expect, str(num))
            f.write(test)
            f.close()

class ASTGenerator(TestCaseGenerator):
    def __init__(self, inputFile: str = './test/ASTGenSuite.py') -> None:
        self.inputFile = inputFile
        self.importLib()
        self.prog = ZCodeProgram('ast')
    
    def importLib(self):
        with open(self.inputFile, 'w') as f:
            importLine = """import unittest\nfrom TestUtils import TestAST\nfrom main.zcode.utils.AST import *\n\nclass ASTGenSuite(unittest.TestCase):"""
            f.write(importLine)
            f.close()
    
    @staticmethod
    def genResult(inputfile):
        lexer = Lexer(inputfile)
        tokens = CommonTokenStream(lexer)
        parser = Parser(tokens)
        tree = parser.program()
        asttree = ASTGeneration().visit(tree)
        return str(asttree)
    
    def gen(self, num: int):
        with open(self.inputFile, 'a') as f:
            program = '\n' + self.prog.gen()
            input = TestSource.makeSource(program, num)
            expect = ASTGenerator.genResult(input)
            test = """\n\tdef test_{}(self):\n\t\tinput = \'\'\'{}\'\'\'\n\t\texpect = \'\'\'{}\'\'\'\n\t\tself.assertTrue(TestAST.test(input, expect, {}))\n""".format(str(num), program, expect, str(num))
            f.write(test)
            f.close()
        

def main(argv):
    if argv[0] == 'LexerSuite':
        lexer = LexerGenerator()
        for test in range(101, 201):
            lexer.gen(test)
    
    elif argv[0] == 'ParserSuite':
        parser = ParserGenerator()
        for test in range(201, 301):
            parser.gen(test)
    
    elif argv[0] == 'ASTGenSuite':
        ast = ASTGenerator()
        for test in range(301, 401):
            ast.gen(test)

if __name__ == '__main__':
    main(sys.argv[1:])