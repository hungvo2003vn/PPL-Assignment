import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_declared(self):
        """declared  declared  declared  declared"""
        input = """
            number VoTien
        """
        expect = str(Program([
                VarDecl(Id("VoTien"), NumberType())
            ]))
        self.assertTrue(TestAST.test(input, expect, 301))
        
        input = """
            string VoTien <- 1
        """
        expect = str(Program([
                VarDecl(Id("VoTien"), StringType(), NumberLit(1))
            ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 302))
        
        input = """
            string Votien
            bool Votien
            string Votien <- 1
            bool Votien <- 1
        """
        expect = str(Program([
                VarDecl(Id("Votien"), StringType()),
                VarDecl(Id("Votien"), BooleanType()),
                VarDecl(Id("Votien"), StringType(), NumberLit(1)),
                VarDecl(Id("Votien"), BooleanType(), NumberLit(1))
            ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 303))
        
        input = """
            string VoTien[5] <- 1
            string VoTien[5]
        """
        expect = str(Program([
                VarDecl(Id("VoTien"), ArrayType([5], StringType()), NumberLit(1)),
                VarDecl(Id("VoTien"), ArrayType([5], StringType()))
            ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 304))
        
        input = """
            number VoTien[5,3,4] <- 1
            bool VoTien[2,3,4]
        """
        expect = str(Program([
                VarDecl(Id("VoTien"), ArrayType([5, 3, 4], NumberType()), NumberLit(1)),
                VarDecl(Id("VoTien"), ArrayType([2, 3, 4], BooleanType()))
            ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 305))
        
        input = """
            dynamic Votien <- 1
            dynamic Votien
        """
        expect = str(Program([
                    ImplicitDynamicDecl(Id("Votien"), NumberLit(1)),
                    ImplicitDynamicDecl(Id("Votien"))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 306))
        
        input = """
            var Votien <- 1
        """
        expect = str(Program([
                    ImplicitVarDecl(Id("Votien"), NumberLit(1))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 307))
        
        input = """
            func main()
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], None)
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 308))
        
        input = """
            func main()
                begin
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], BlockStmt([]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 309))

        input = """
            func main()
                begin
                break
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], BlockStmt([
                    BreakStmt()]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 310))
                
        input = """
            func main(number a)
            func main(number a, string a, bool a[2])
            func main(number Votien[1,2])
                return
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [ParamDecl("a", NumberType())], None),
                    FuncDecl(Id("main"), [ParamDecl("a", NumberType()), ParamDecl("a", StringType()), ParamDecl("a", ArrayType([2], BooleanType()))], None),
                    FuncDecl(Id("main"), [ParamDecl("Votien", ArrayType([1, 2], NumberType()))], ReturnStmt())
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 311))
        
    def test_Expression(self):
        """Expression Expression Expression"""
        input = """
            var x <- 1
            var x <- "123"
            var x <- true
            var x <- false
        """
        expect = str(Program([
                    ImplicitVarDecl(Id("x"), NumberLit(1)),
                    ImplicitVarDecl(Id("x"), StringLit("123")),
                    ImplicitVarDecl(Id("x"), BooleanLit(True)),
                    ImplicitVarDecl(Id("x"), BooleanLit(False))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 312))
        
        input = """
            var x <- [1, "a", true, false]
        """
        expect = str(Program([
                    ImplicitVarDecl(Id("x"), ArrayLit([NumberLit(1), StringLit("a"), BooleanLit(True), BooleanLit(False)]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 313))   
        
        input = """
            var x <- [[1], [1]]
            var x <- [[1]]
        """
        expect = str(Program([
                    ImplicitVarDecl(Id("x"), ArrayLit([ArrayLit([NumberLit(1)]), ArrayLit([NumberLit(1)])])),
                    ImplicitVarDecl(Id("x"), ArrayLit([ArrayLit([NumberLit(1)])]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 314))  
        
        input = """
            var x <- 1 ... "2"
            var x <- 1 <= "2"
            var x <- 1 and 2 or 3
            var x <- 1 + 2 - 3
            var x <- 1 * 2 / 3 % 4
            var x <- ---1
            var x <- not not 1
            var x <- x 
            var x <- a[1,2,3]
        """
        expect = str(Program([
                    ImplicitVarDecl(Id("x"), BinExpr("...", NumberLit(1), StringLit("2"))),
                    ImplicitVarDecl(Id("x"), BinExpr("<=", NumberLit(1), StringLit("2"))),
                    ImplicitVarDecl(Id("x"), BinExpr("or", BinExpr("and", NumberLit(1), NumberLit(2)), NumberLit(3))),
                    ImplicitVarDecl(Id("x"), BinExpr("-", BinExpr("+", NumberLit(1), NumberLit(2)), NumberLit(3))),
                    ImplicitVarDecl(Id("x"), BinExpr("%", BinExpr("/", BinExpr("*", NumberLit(1), NumberLit(2)), NumberLit(3)), NumberLit(4))),
                    ImplicitVarDecl(Id("x"), UnExpr("-", UnExpr("-", UnExpr("-", NumberLit(1))))),
                    ImplicitVarDecl(Id("x"), UnExpr("not", UnExpr("not", NumberLit(1)))),
                    ImplicitVarDecl(Id("x"), Id("x")),
                    ImplicitVarDecl(Id("x"), ArrayCell(Id("a"), [NumberLit(1), NumberLit(2), NumberLit(3)]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 315))  
        
        input = """
            var x <- 2 or 3 and 1 <= 2 ... 4 <= 5 + a * 3 + c - -1 + not - 2
        """
        expect = str(Program([
                ImplicitVarDecl(Id("x"), BinExpr("...", BinExpr("<=", BinExpr("and", BinExpr("or", NumberLit(2), NumberLit(3)), NumberLit(1)), NumberLit(2)), BinExpr("<=", NumberLit(4), BinExpr("+", BinExpr("-", BinExpr("+", BinExpr("+", NumberLit(5), BinExpr("*", Id("a"), NumberLit(3))), Id("c")), UnExpr("-", NumberLit(1))), UnExpr("not", UnExpr("-", NumberLit(2)))))))
            ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 316))  
        
        input = """
            var x <- -a[1+2] ... 2
        """
        expect = str(Program([
                    ImplicitVarDecl(Id("x"), BinExpr("...", UnExpr("-", ArrayCell(Id("a"), [BinExpr("+", NumberLit(1), NumberLit(2))])), NumberLit(2)))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 317))  
        
        input = """
            var x <- fun()
        """
        expect = str(Program([
                    ImplicitVarDecl(Id("x"), FuncCall(Id("fun"), []))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 318)) 
        
        input = """
            var x <- fun(1+1, "a")
        """
        expect = str(Program([
                    ImplicitVarDecl(Id("x"), FuncCall(Id("fun"), [BinExpr("+", NumberLit(1), NumberLit(1)), StringLit("a")]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 319)) 
        
        input = """
            var x <- fun(fun())
        """
        expect = str(Program([
                    ImplicitVarDecl(Id("x"), FuncCall(Id("fun"), [FuncCall(Id("fun"), [])]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 320)) 
        
        input = """
            var x <- (2 ... 3) ... 4
        """
        expect = str(Program([
                    ImplicitVarDecl(Id("x"), BinExpr("...", BinExpr("...", NumberLit(2), NumberLit(3)), NumberLit(4)))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 321)) 
         
    def test_Statements(self):
        """Statements Statements Statements"""
        input = """
            func main()
                begin
                    continue
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], BlockStmt([
                    ContinueStmt()]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 322))

        input = """
            func main()
                begin
                    continue
                    continue
                    break
                    begin
                        continue
                        continue
                        break                    
                    end
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], BlockStmt([
                    ContinueStmt(),
                    ContinueStmt(),
                    BreakStmt(),
                        BlockStmt([
                        ContinueStmt(),
                        ContinueStmt(),
                        BreakStmt()])]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 323))
        
        input = """
            func main()
                begin
                    return  1 + 1
                end
            func main()
                return 1
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], BlockStmt([
                    ReturnStmt(BinExpr("+", NumberLit(1), NumberLit(1)))])),
                    FuncDecl(Id("main"), [], ReturnStmt(NumberLit(1)))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 324))

        input = """
            func main()
                begin
                    main(a)
                    main(1,1)
                end
            func main()
                begin
                main()
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], BlockStmt([
                    CallStmt(Id("main"), [Id("a")]),
                    CallStmt(Id("main"), [NumberLit(1), NumberLit(1)])])),
                    FuncDecl(Id("main"), [], BlockStmt([
                    CallStmt(Id("main"), [])]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 325))
        
        input = """
            func main()
                begin
                    a <- 1
                    a[1] <- 2
                    a[3,2] <- 4 + 2
                end
            func main()
                begin
                a[1+1, 3] <- 1
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], BlockStmt([
                    AssignStmt(Id("a"), NumberLit(1)),
                    AssignStmt(ArrayCell(Id("a"), [NumberLit(1)]), NumberLit(2)),
                    AssignStmt(ArrayCell(Id("a"), [NumberLit(3), NumberLit(2)]), BinExpr("+", NumberLit(4), NumberLit(2)))])),
                    FuncDecl(Id("main"), [], BlockStmt([
                    AssignStmt(ArrayCell(Id("a"), [BinExpr("+", NumberLit(1), NumberLit(1)), NumberLit(3)]), NumberLit(1))]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 326))
        
        input = """
            func main()
                begin
                    for i until i > 2 by 1 + 1
                        print(1)
                end
            func main()
                begin
                    for i until i by [1]
                    begin
                        print(1)
                    end
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], BlockStmt([
                    ForStmt(Id("i"), BinExpr(">", Id("i"), NumberLit(2)), BinExpr("+", NumberLit(1), NumberLit(1)), CallStmt(Id("print"), [NumberLit(1)]))])),
                    FuncDecl(Id("main"), [], BlockStmt([
                    ForStmt(Id("i"), Id("i"), ArrayLit([NumberLit(1)]), BlockStmt([
                    CallStmt(Id("print"), [NumberLit(1)])]))]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 327))
        
        input = """
            func main()
                begin
                    if true return 1
                end
            func main()
                begin
                    if true return 2
                    else return 3
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], BlockStmt([
                    IfStmt(BooleanLit(True), ReturnStmt(NumberLit(1)), [] ,)])),
                    FuncDecl(Id("main"), [], BlockStmt([
                    IfStmt(BooleanLit(True), ReturnStmt(NumberLit(2)), [] ,ReturnStmt(NumberLit(3)))]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 328))
        

        input = """
            func main()
                begin
                    if true return 1
                    elif true return 1
                    elif true return 1
                    else return 1
                end

        """
        expect =str(Program([
                    FuncDecl(Id("main"), [], BlockStmt([
                    IfStmt(BooleanLit(True), ReturnStmt(NumberLit(1)), [[BooleanLit(True),ReturnStmt(NumberLit(1))],[BooleanLit(True),ReturnStmt(NumberLit(1))]] ,ReturnStmt(NumberLit(1)))]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 329))     
        
        input = """
            var c <- a[1,2]
            var c <- fun()[1,2]
            var c <- fun(1,2)[1,3]
        """
        expect = str(Program([
            ImplicitVarDecl(Id("c"), ArrayCell(Id("a"), [NumberLit(1), NumberLit(2)])),
            ImplicitVarDecl(Id("c"), ArrayCell(FuncCall(Id("fun"), []), [NumberLit(1), NumberLit(2)])),
            ImplicitVarDecl(Id("c"), ArrayCell(FuncCall(Id("fun"), [NumberLit(1), NumberLit(2)]), [NumberLit(1), NumberLit(3)]))
        ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 330))    
        
        
        