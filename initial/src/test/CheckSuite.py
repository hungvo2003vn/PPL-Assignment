import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_1_No_entry_point(self):
        input = """
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))
        
        input = """
            func main()
            func main() begin
                number main
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 402))
        
        input = """
            func main(number a) begin
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 403))
        
        input = """
            func main() return 1   
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 404))
        
        input = """
            number VoTien
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_2_NoDefinition(self):
        input = """
            func foo(number a)
            func foo(number a) return     
        
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))

        input = """
            func foo(number a) return   
        
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 407))
        
        input = """
            func foo(number a) 
        
            func main() return
        """
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 408))
        
    def test_3_Redeclared(self):
        input = """
            number a
            string a 
            
            func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 410))
        
        input = """
            func a()
            number a
            
            func main() return
        """
        expect = "No Function Definition: a"
        self.assertTrue(TestChecker.test(input, expect, 411))
        
        input = """
            func foo() return
            func foo()
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 412))
        
        input = """
            func foo()
            func foo()
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 413))
        
        input = """
            func foo() return
            func foo() return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 414))
        
        input = """
            number foo
            func foo() return
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 415))
        
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                number c
                string VoTien
                begin
                    number c
                    string VoTien
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 416))
        
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                string a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 417))
        
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                begin
                    number a
                end
                string a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 418))
        
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                begin
                    number a
                    string a
                end
                
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 419))
        
        input = """
            number a
            func VoTien(number a, number VoTien, number c)
            begin
                string c
            end
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 420))
        
        input = """
            number a
            func VoTien(number a, number VoTien, number c, string c)
            begin
            end
            
            func main() return
        """
        expect = "Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input, expect, 421))
        
        input = """
            number a
            func VoTien(number a, number VoTien, number c)
            begin
                begin
                    number a
                end
                number a
            end
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 422))
        
        input = """
            func foo(number a) 
            func foo(number b) return
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 423))
        
        input = """
            func foo(number a) 
            func foo(string a) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 423))
        
        input = """
            func foo(number a) 
            func foo(number a, string c) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 424))
        
        input = """
            func foo(number a, string c) 
            func foo(number a) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 425))
        
    def test_3_Undeclared(self):
        input = """
            number a <- a
            func main() begin
                number b <- a
                number c <- e
            end
        """
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input, expect, 426))
        
        input = """
            func a() return 1
            func main() begin
                number b <- a
            end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 427))
        
        input = """
            func a() return 1
            func main() begin
                number a
                begin 
                    number d
                end
                number b <- a
                number c <- d
            end
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 428))

        input = """
            func a() begin
                a()
            end
            func main() begin
                a()
                b()
            end
        """
        expect = "Undeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, 429))
        
        input = """
            func a() return
            func main() begin
                number a
                a()
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 430))
        
        input = """
            func a()
            func main() begin
                a()
            end
            func a() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 431))


    def test_4_MustInLoop(self):
        input = """
            func main() begin
                var i <- 2
                for i until true by 1
                begin
                    break
                    continue
                    begin
                        break
                        continue
                    end
                    
                    for i until true by 1
                    begin
                        break
                        continue
                    end
                    break
                    continue
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 432))
        
        input = """
            func main() begin
                break
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 433))
        
        input = """
            func main() begin
                continue
            end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 434))
        
    def test_5_TypeCannotBeInferred(self):
        input = """
            dynamic VoTien
            var a <- VoTien

            func main() return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, Id(VoTien))"
        self.assertTrue(TestChecker.test(input, expect, 435))
        
        input = """
            number VoTien
            var a <- VoTien
            number b <- a

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 436))
        
        input = """
            dynamic VoTien
            number a <- VoTien
            number b <- VoTien

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 437))
        
        input = """
            func foo() begin
                dynamic a
                return a
            end

            func main() return
        """
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 438))
        
        input = """
            func foo() begin
                return 1
                dynamic a
                return a
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 439))
        
        input = """
            func foo() begin
                number a
                return a
                return 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 440))
        
        input = """
            func foo() begin
                dynamic a
                dynamic b
                a <- b
            end

            func main() return
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 441))
        
        input = """
            func foo() begin
                number a
                dynamic b
                a <- b
                b <- 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 442))
        
        input = """
            func foo() begin
                number a
                dynamic b
                b <- a
                b <- 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 443))
        
    def test_6_TypeMismatchInStatement(self):
        input = """
            number a <- "1"

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 444))
        
       
        input = """
            number a[1,2] <- [[1,2]]

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 445))
        
        
        input = """
            number a[1,2,3] <- [[1,2]]

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0, 2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))"
        self.assertTrue(TestChecker.test(input, expect, 446))

        input = """
            number a[1] <- [[1,2]]

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))"
        self.assertTrue(TestChecker.test(input, expect, 447))       

        input = """
            func foo() return

            func main()begin
                foo()
                foo(1)
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 448))    
        
        input = """
            func foo(number a) return

            func main()begin
                foo()
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 449))     
        
        input = """
            func foo(number a) return

            func main()begin
                foo("1")
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 450))    
        
        input = """
            func foo(number a) return

            func main()begin
                dynamic a
                foo(a)
                number c <- a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 451))                

        input = """
            func main()begin
                dynamic a
                if (a) return
                a <- true
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 452))     
        
        input = """
            func main()begin
                dynamic a <- 1
                if (a) return
            end
        """
        expect = "Type Mismatch In Statement: If((Id(a), Return()), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 453))                 

        input = """
            func main()begin
                dynamic a
                if (a) return
                elif (a)  return
                else return
                
                if(true) return
                elif (1) return
            end
        """
        expect = "Type Mismatch In Statement: If((BooleanLit(True), Return()), [(NumLit(1.0), Return())], None)"
        self.assertTrue(TestChecker.test(input, expect, 454)) 
        
        input = """
            func foo() begin
                dynamic a
                dynamic b
                dynamic c
                for a until b by c return
                a <- 1
                b <- true
                c <- 1
            end
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 455))   
        
        input = """
            func foo() begin
                dynamic a <- true
                dynamic b
                dynamic c
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 456))    
        
        input = """
            func foo() begin
                dynamic a 
                dynamic b <- 2
                dynamic c
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 457))  

        input = """
            func foo() begin
                dynamic a 
                dynamic b
                dynamic c <- "1"
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 458))    
        
        input = """
            func foo() begin
                number a
                return 1
                return a
                return "!"
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: Return(StringLit(!))"
        self.assertTrue(TestChecker.test(input, expect, 459))  
        
        
        input = """
            func foo() begin
                number a
                a <- 1
                a <- true
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 460))  

    def test_6_TypeMismatchInExpression(self):
        input = """
            func foo() return 1

            func main() begin
                var a <- foo()
                var b <- foo(1)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 461))
        
        input = """
            func foo(number a) return 1

            func main() begin
                var a <- foo()
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 462))
        
        input = """
            func foo(number a) return 1

            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 463))
        
        input = """
            func foo(number a) return
            
            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 464))
        
        input = """
            func foo(number a) return
            
            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 465))
        
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- left + right
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 466))
        
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- left + 1
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 467))
        
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- 1 + right
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 468))
        

        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- - left
                left <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 469))
        
        input = """
            func main() begin
                number a[1,2]
                number b
                var c <- b[1]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 470))


        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- b[1]
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(c), None, var, ArrayCell(Id(b), [NumLit(1.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 471))
        
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[b, 1]
                b <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 472))
        
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a["1"]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 473))
        
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1,2,3]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0), NumLit(3.0)])"
        self.assertTrue(TestChecker.test(input, expect, 474))
        
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1,3]
                c <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 475))
        
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1]
                c <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 476))
        
        
        input = """
            func VoTien()
            func main() begin
                number VoTien_ <- VoTien()
            end
            func VoTien() begin
            end
        """
        # expect = "???"
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 477))
        
        input = """
            dynamic VoTien
            var x <- VoTien and (VoTien > VoTien)
        """
        expect = "Type Mismatch In Expression: BinaryOp(>, Id(VoTien), Id(VoTien))"
        self.assertTrue(TestChecker.test(input, expect, 478))

        input = """
            dynamic VoTien
            var x <- VoTien + VoTien * VoTien
            number y <- VoTien
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 479))
        
        input = """
            dynamic VoTien
            var x <- VoTien > VoTien ... VoTien < VoTien
        """
        expect = "Type Mismatch In Expression: BinaryOp(..., BinaryOp(>, Id(VoTien), Id(VoTien)), BinaryOp(<, Id(VoTien), Id(VoTien)))"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_7_full(self):
        input = """
            func areDivisors(number num1, number num2)
            return ((num1 % num2 = 0) or (num2 % num1 = 0))
            func main()
            begin
            var num1 <- readNumber()
            var num2 <- readNumber()
            if (areDivisors(num1, num2)) writeString("Yes")
            else writeString("No")
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))
        
        input = """
func isPrime(number x)
func main()
begin
number x <- readNumber()
if (isPrime(x)) writeString("Yes")
else writeString("No")
end
func isPrime(number x)
begin
if (x <= 1) return false
var i <- 2
for i until i > x / 2 by 1
begin
if (x % i = 0) return false
end
return true
end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 500))
        
        input = """
            var VoTien <- VoTien
            func main() return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(VoTien), None, var, Id(VoTien))"
        self.assertTrue(TestChecker.test(input, expect, 501))

        input = """
            func main() return main()
        """
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(main), []))"
        self.assertTrue(TestChecker.test(input, expect, 502))
        input = """
            func a()
            func main() begin 
                a()
            end
            func a() return 1
        """
        expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 503))  
        
        input = """
            func a()
            func main() begin 
                a()
            end
            func a() return 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 504))    \
            
        input = """
            func a()
            func a() return 1
            func main() begin 
                a()
            end
             
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(a), [])"
        self.assertTrue(TestChecker.test(input, expect, 505))
        
    def test_arraylit(self):
        
        input = """
            dynamic x
            number a <- [x]
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), NumberType, None, ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 506))        
        
        input = """
            dynamic x
            number a[3] <- [x]
            func f()
            begin
                x <- [1,2,3]
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 507))        
        
        input = """
            dynamic x
            number a[3] <- [x, 1, 2]
            func  main()
            begin
                x <- 1
            end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 508))     
        

        input = """
            dynamic x
            number a[3] <- [x, x, x]
            func  main()
            begin
                x <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 509))   
        
        input = """
            dynamic x
            number a[3] <- [x, x, "1"]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(Id(x), Id(x), StringLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 510))   
        
        input = """
            dynamic x
            number a[3] <- [x, 1, "1"]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), NumLit(1.0), StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 511))  
        
        input = """
            dynamic x
            number a[3] <- [x, [x,x], 1]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 512))  

        input = """
            dynamic x
            number a[3] <- [1, [x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(NumLit(1.0), ArrayLit(Id(x), Id(x))))"
        self.assertTrue(TestChecker.test(input, expect, 513))    
        
        input = """
            dynamic x
            number a[3] <- [[1,2,3], [x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 514))     
        
        input = """
            dynamic x
            number a[3,3] <- [[1,2,3], x, x]
            func  main()
            begin
                x <- [1,2,3]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 515))     
        
        input = """
            dynamic x
            number a[2,3] <- [[1,2,3], [x,x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 516))  
        
        input = """
            dynamic x
            number a[2,3] <- [[1,2,3], 1]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 517)) 
        
        input = """
            dynamic x
            number a[2,3] <- [[1,2,3], [x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 518)) 
        
        input = """
            dynamic x
            number a[1,1,1,1] <- [[[x]]]
            func  main()
            begin
                x <- [1]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 519)) 
        
        
        input = """
            dynamic x
            number a[1,1,2,2] <- [[[[1,2], x]]]
            func  main()
            begin
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 520)) 
        
        input = """
            dynamic x
            number a[1,1,2,2] <- [[[x, x]]]
            func  main()
            begin
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 521)) 
  
        input = """
            dynamic x
            var a <- [x]
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 522))  
        
        input = """
            func foo() begin
                dynamic x
                return [x]                
            end
            func main() return 
        """
        expect = "Type Cannot Be Inferred: Return(ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 523))  
        
        input = """
            func foo() begin
                dynamic x
                return [x, [1,2]]                
            end
            func main() return 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 524))  
        
        input = """
            func foo() begin
                dynamic x
                dynamic y
                return [[y], [y]]
                return x
                return [[1], [2]]
            end
            func main() return 
        """
        expect = "Type Cannot Be Inferred: Return(ArrayLit(ArrayLit(Id(y)), ArrayLit(Id(y))))"
        self.assertTrue(TestChecker.test(input, expect, 525))  
        
        input = """
            func foo() begin
                dynamic x
                dynamic y
                return [[1], [2]]
                return [x, y]
                x <- [1]
                y <- x
            end
            func main() return 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 526)) 
        
        
        input = """
            func foo() begin
                dynamic x
                dynamic y
                return [[1], [2]]
                return [x, [y]]
                x <- [1]
                y <- x
            end
            func main() return 
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(y), Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 527)) 
        
        
        input = """
            func foo(number a[2,2]) return
            func main() begin
                dynamic x
                foo(x)
                x <- [[2,2], [2,3]]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 528)) 
        
        input = """
            func foo(number a[2,2]) return
            func main() begin
                dynamic x
                foo([x])
                x <- [1]
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [ArrayLit(Id(x))])"
        self.assertTrue(TestChecker.test(input, expect, 529)) 

        input = """
            func foo(number a[2,2]) return
            func main() begin
                dynamic x
                foo([x, x])
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 530)) 
        
        input = """
            func foo(number a[2,2]) return 1
            func main() begin
                dynamic x
                var a <- foo([x, x])
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 531)) 
        
        input = """
            func foo(number a[2,2]) return 1
            func main() begin
                dynamic x
                var a <- foo(x)
                x <- [1,2]
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), ArrayLit(NumLit(1.0), NumLit(2.0)))"
        self.assertTrue(TestChecker.test(input, expect, 532)) 
        
        input = """
            func main() begin
                dynamic x
                number a <- 1 + x[1,3]
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), NumberType, None, BinaryOp(+, NumLit(1.0), ArrayCell(Id(x), [NumLit(1.0), NumLit(3.0)])))"
        self.assertTrue(TestChecker.test(input, expect, 533)) 
        
        input = """
            func main() begin
                dynamic x
                number a <- 1 + [x]
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), NumberType, None, BinaryOp(+, NumLit(1.0), ArrayLit(Id(x))))"
        self.assertTrue(TestChecker.test(input, expect, 534)) 

        input = """
            func main() begin
                dynamic x
                number a <- 1 + [x,1]
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), ArrayLit(Id(x), NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 535)) 
        
        
    def test_return(self):
        input = """
            func main() begin 
                return
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 536))   

        input = """
            func main() begin 
                return 1
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 537))   

        input = """
            func main() begin 
                return 1
                begin
                    return "string"
                end
            end
        """
        expect = "Type Mismatch In Statement: Return(StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 538))    
        
        input = """
            func main() begin 
                dynamic i
                return 1
                return i
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 539))  
        
        input = """
            func fun() begin
                return 
                return
                return 1
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 540))       
        
        input = """
            func fun() begin
                return 1
                return "string"
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 541))    
        
        input = """
            func fun() begin
                number a[3]
                return [1, 4, 3]
                return a
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 542))   
        
        input = """
            func fun() begin
                number a[2,2]
                return [[1,2], [3,4]]
                return a
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 543))    
        
        input = """
            func fun() begin
                number a[3,2]
                return [[1,2], [3,4]]
                return a
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 544))  
        
        input = """
            func fun() begin
                number a[2,2]
                return a
                return [["1","2"], ["3","4"]]
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
        self.assertTrue(TestChecker.test(input, expect, 545))   
        
        input = """
            func fun() begin
                string a[2,2, 3]
                return a
                return [["1","2"], ["3","4"]]
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
        self.assertTrue(TestChecker.test(input, expect, 546))  
        
        input = """
            func fun() begin
                string a[2]
                return a
                return [["1","2"], ["3","4"]]
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
        self.assertTrue(TestChecker.test(input, expect, 547))   
        
        input = """
            func fun() begin
                string a[1,1,1,1,1]
                return a
                return [[[[["1"]]]]]
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 548))     
        
        input = """
            func fun() begin
                return [1,2]
                return [3,4]
            end
            
            func fun1() begin
                return [[1,2], [3,4]]
                return [[1,5], [3,4]]
            end
            
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 549)) 
        
        
        input = """
            func fun1() return 1
            func fun2() return
            func fun3()
            
            func main() begin 
               return fun3()
            end
        """
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(fun3), []))"
        self.assertTrue(TestChecker.test(input, expect, 550)) 
        
        input = """
            func fun1() return 1
            func fun2() return
            func fun3()
            
            func main() begin 
               return fun1()
            end
            func fun3() return 1   
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 551)) 

        input = """
            func fun1() return 1
            func fun2() return
            func fun3()
            
            func main() begin 
               number a <- fun3()
            end
            func fun3() return "1"  
        """
        expect = "Type Mismatch In Statement: Return(StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 552)) 
        
                
        input = """
            func fun1() return [1,2]
            func fun2() return [3,4]
            func fun3()
            
            func main() begin 
               return fun1()
               return fun2()
               return fun3()
            end 
        """
        expect = "No Function Definition: fun3"
        self.assertTrue(TestChecker.test(input, expect, 553)) 
        

    def test_Assign(self):
        input = """
            func main() begin 
                number a
                dynamic b
                dynamic c
                b <- c
            end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(b), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 554)) 
        

        input = """
            func main() begin 
                number a
                dynamic b
                dynamic c
                a <- c
                b <- c
                return a
                return b
                return c
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 555))   
        
        input = """
            func main() begin 
                number a
                string b
                dynamic c
                a <- c
                c <- b

            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(c), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 556))   
        
        input = """
            func main() begin 
                number a
                string b
                dynamic c
                c <- a
                b <- c

            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 557))      
        
        input = """
            func main() begin 
                number a[1,3]
                dynamic c
                c <- [[1,2,3]]
                c <- a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 558))   
        
        input = """
            func foo()
            func main() begin 
                number a[1,3]
                dynamic c
                c <- foo()
            end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(c), CallExpr(Id(foo), []))"
        self.assertTrue(TestChecker.test(input, expect, 559)) 
        
        input = """
            func foo()
            func main() begin 
                number a[1,3]
                dynamic c
                a <- foo()
            end
            func foo()
                return [[1,2,3]]
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 560))
        
        input = """
            func foo()
            func main() begin 
                number a[1,3]
                dynamic c
                a <- foo()
            end
            func foo()
                return [1,2,3]
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 561))

    def test_Votien_1(self):
        input = """
            func foo(number a, string a)
            func foo(number a, string a) return 
            func main() return
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 601))

    def test_Votien_2(self):
        input = """
            func foo(number a, string a)
            func foo(number a) return
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 602))



    def test_Votien_3(self):
        input = """
            func foo(number a[1,2,3])
            func foo(number a[1,2]) return
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 603))


    def test_Votien_4(self):
        input = """
            number a
            func foo(number a)
            begin
                number a
                number b
                if (true) number b
            end
            func main() return
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 604))
        
    def test_Votien_5(self):
        input = """
            number a
            func foo(number a)
            begin
                number a
                if (true) number b
                else number b
            end
            func main() return
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 605))

    def test_Votien_6(self):
        input = """
            number a
            func foo(number a)
            begin
                number a
                if (true) number b
                
                for b until true by 1
                    number b
            end
            func main() return
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 606))
        
    def test_Votien_7(self):
        input = """
            number a
            func foo(number a)
            begin
                number a
                if (true)
                begin
                    number a
                end
                
                begin
                    number a
                end
                
                for a until true by 1
                begin
                    number a
                end
            end
            func main() 
            begin
                number a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 607))        


    def test_Votien_8(self):
        input = """
            func main() 
            begin
                dynamic x
                if ([x]) x <- 1
            end
        """
        expect = "Type Cannot Be Inferred: If((ArrayLit(Id(x)), AssignStmt(Id(x), NumLit(1.0))), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 608)) 
        
    def test_Votien_9(self):
        input = """
            func main() 
            begin
                dynamic x
                dynamic y
                for x until y[1] by 1
                    return
            end
        """
        expect = "Type Cannot Be Inferred: For(Id(x), ArrayCell(Id(y), [NumLit(1.0)]), NumLit(1.0), Return())"
        self.assertTrue(TestChecker.test(input, expect, 609)) 
        
    def test_Votien_10(self):
        input = """
            func main() 
            begin
                dynamic x
                dynamic y
                for x until true by x[1]
                    return
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(x), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 610)) 
               

    def test_Votien_11(self):
        input = """
            func main() 
            begin
                dynamic x
                dynamic y
                for x until true by x[1]
                    return
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(x), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 611)) 
               
    def test_Votien_12(self):
        input = """
            func main() 
            begin
                dynamic x
                return x[1]
            end
        """
        expect = "Type Cannot Be Inferred: Return(ArrayCell(Id(x), [NumLit(1.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 612))   
        
    def test_Votien_13(self):
        input = """
            func main() 
            begin
                dynamic x
                return [x, [x, x]]
            end
        """
        expect = "Type Cannot Be Inferred: Return(ArrayLit(Id(x), ArrayLit(Id(x), Id(x))))"
        self.assertTrue(TestChecker.test(input, expect, 613))                

    def test_Votien_13(self):
        input = """
            func foo(number a) return 1
            func main() 
            begin
                dynamic x
                number a <- 1 + foo([[x]])
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), NumberType, None, BinaryOp(+, NumLit(1.0), CallExpr(Id(foo), [ArrayLit(ArrayLit(Id(x)))])))"
        self.assertTrue(TestChecker.test(input, expect, 614)) 
                       
    def test_Votien_14(self):
        input = """
            func foo(number a) return 1
            func main() 
            begin
                dynamic x
                dynamic y
                var a <- [x, [[1,2]], [[y, 1]]]
                x <- [[0,0]]
                y <- x[0,0]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 615)) 


    def test_Votien_15(self):
        input = """
            func foo(number a) return
            func main() 
            begin
                return foo(1)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 616)) 
        
    def test_Votien_16(self):
        input = """
            func foo(number a) return 1
            func main() 
            begin
                dynamic x
                var a <- 1 * 2 + 3 * foo([x, x])
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, BinaryOp(+, BinaryOp(*, NumLit(1.0), NumLit(2.0)), BinaryOp(*, NumLit(3.0), CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))]))))"
        self.assertTrue(TestChecker.test(input, expect, 617)) 

    def test_Votien_17(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                var a <- foo([x, x]) ... foo([x, x])
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, BinaryOp(..., CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))]), CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))])))"
        self.assertTrue(TestChecker.test(input, expect, 618)) 

    def test_Votien_18(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                var a <- foo([x, x]) ... foo([x, x])
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, BinaryOp(..., CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))]), CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))])))"
        self.assertTrue(TestChecker.test(input, expect, 619))    
        
    def test_Votien_19(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                var a <- x ... foo([x, x])
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))])"
        self.assertTrue(TestChecker.test(input, expect, 620))     
        
    def test_Votien_20(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                var a <- x ... foo([x, x])
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))])"
        self.assertTrue(TestChecker.test(input, expect, 621))     
        
        
    def test_Votien_21(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                var a <- foo([x, x]) ... x
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, BinaryOp(..., CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))]), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 622))   
        
        
    def test_Votien_22(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                var a <- [[1,2,3], [x,x]]
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 623))   
        
    def test_Votien_23(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                var a <- [[1,2,3], [x,x]]
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 624))   
        
    def test_Votien_24(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                number a[1,1,1,1] <- [[[[x]]]]
                x <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 625))  
        
    def test_Votien_25(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                number a <- 1 + [[[[x]]]]
                x <- 1
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), NumberType, None, BinaryOp(+, NumLit(1.0), ArrayLit(ArrayLit(ArrayLit(ArrayLit(Id(x)))))))"
        self.assertTrue(TestChecker.test(input, expect, 626))  