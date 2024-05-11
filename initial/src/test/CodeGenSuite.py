import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    
    # #* test cơ bản về hàm main và các hàm write
    def test_1(self):
        input = """
        func main ()
        begin
            writeNumber(1)
            writeBool(true)
            writeString("votien")
        end
        """
        expect = "1.0\ntrue\nvotien\n"
        self.assertTrue(TestCodeGen.test(input, expect, 700))
        
        input = """
        func main ()
        begin
            writeNumber(1.0)
            writeBool(false)
            writeString("")
        end
        """
        expect = "1.0\nfalse\n\n"
        self.assertTrue(TestCodeGen.test(input, expect, 701))
    
    #* test visitVarDecl và visitId và visitAssign và visitReturn và visitCallStmt(cơ bản)
    def test_2(self):
        #* test visitVarDecl biến toàn cục emit.put và emit.get
        input = """
        number a <- 1
        func main ()
        begin
            writeNumber(a)
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 702))   
        
        #* test visitVarDecl biến cục bộ emit.read và emit.write
        input = """
        number a <- 1
        func main ()
        begin
            number a <- 2
            writeNumber(a)
        end
        """
        expect = "2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 703))  
        
        input = """
        number a <- 1
        func main ()
        begin
            begin
                number a <- 2
            end
            writeNumber(a)
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 704))  
        
        input = """
        number a <- 1
        func main ()
        begin
            begin
                number a <- 2
                writeNumber(a)
            end
            writeNumber(a)
        end
        """
        expect = "2.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 705))  
        
        input = """
        dynamic a
        func main ()
        begin
            bool b <- true
            begin
                a <- b
            end
            writeBool(a)
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 706))  
        
        input = """
        dynamic a
        func main ()
        begin
            var b <- "votien"
            begin
                a <- b
            end
            writeString(a)
        end
        """
        expect = "votien\n"
        self.assertTrue(TestCodeGen.test(input, expect, 707))      
        
        input = """
        dynamic a <- 1
        func foo(number a)
        begin
            writeNumber(a)
        end
        func main ()
        begin
            foo(2)
        end
        """
        expect = "2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 708)) 
        
        input = """
        dynamic a <-1
        func foo(number a)
        begin
            var a <- 3
            writeNumber(a)
        end
        func main ()
        begin
            foo(2)
        end
        """
        expect = "3.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 709)) 
        
        
        input = """
        dynamic a <-1
        func foo(number a)
        begin
            writeNumber(a)
            var a <- 3
            writeNumber(a)
        end
        func main ()
        begin
            foo(2)
            writeNumber(a)
        end
        """
        expect = "2.0\n3.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 710)) 
        
        input = """
        dynamic a <-1
        func foo()
        begin
            a <- 3
        end
        func main ()
        begin
            foo()
            writeNumber(a)
        end
        """
        expect = "3.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 711)) 
        
        input = """
        dynamic a <- 1
        func foo()
        begin
            begin
                number a <- 2
            end
            writeNumber(a)
            a <- 3
        end
        func main ()
        begin
            foo()
            writeNumber(a)
        end
        """
        expect = "1.0\n3.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 712))  
        

        input = """
        dynamic a <- 1
        func foo()
        begin
            a <- 3
            writeNumber(a)
        end
        func main ()
        begin
            number a <- 2
            foo()
            writeNumber(a)
        end
        """
        expect = "3.0\n2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 713))   
        
        input = """
        dynamic a
        func foo()
        func main ()
        begin
            foo()
            writeNumber(a)
        end
        func foo()
        begin
            a <- 3
            writeNumber(a)
        end
        """
        expect = "3.0\n3.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 714))             
           
    #* test visitCallExpr và visitReturn
    def test_3(self):
        input = """
        func foo(number a)
        begin
            return a
        end
        func main ()
        begin
            writeNumber(foo(2))
        end
        """
        expect = "2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 715)) 
        
        
        input = """
        func foo(number a)
        begin
            return true
        end
        func main ()
        begin
            writeBool(foo(2))
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 716)) 
        
        input = """
        func foo(string a)
        begin
            return a
        end
        func main ()
        begin
            writeString(foo("vo"))
        end
        """
        expect = "vo\n"
        self.assertTrue(TestCodeGen.test(input, expect, 717))  
        
        input = """
        func main ()
        begin
            var a <- readString()
            writeString(a)
        end
        """
        expect = "-1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 718))  
        
        input = """
        func main ()
        begin
            var a <- readNumber()
            writeNumber(a)
        end
        """
        expect = "-1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 719))  
        
        # Test này nhập tay nên bỏ qua
        # input = """
        # func main ()
        # begin
        #     var a <- readBool() #* true
        #     writeBool(a)
        # end
        # """
        # expect = "true\n"
        # self.assertTrue(TestCodeGen.test(input, expect, 720))  
        
        input = """
        func foo()
            return true
        func main ()
        begin
            var a <- foo() ## true
            writeBool(a)
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 721))  
        
        input = """
        func foo()
            return "votien"
        func main ()
        begin
            var a <- foo() ## true
            writeString(a)
        end
        """
        expect = "votien\n"
        self.assertTrue(TestCodeGen.test(input, expect, 722)) 
        
        input = """
        func foo(number a, number c)
            return a
        func main ()
        begin
            var a <- foo(1, 2) ## true
            writeNumber(a)
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 723))
        
        input = """
        number c <- 5
        func foo(number a, number c)
        begin
            return c
        end
        func main ()
        begin
            var a <- foo(1, 2)
            writeNumber(a)
        end
        """
        expect = "2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 724))  

        input = """
        number c <- 5
        func foo(number a)
        begin
            return c
        end
        func main ()
        begin
            var a <- foo(1) 
            writeNumber(a)
        end
        """
        expect = "5.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 725))  
        
    #* test visitBinaryOp và visitUnaryOp
    def test_4(self): 
        input = """
        func main ()
        begin
            writeNumber(1 + 1)
            writeNumber(1 - 1)
            writeNumber(1 * 2)
            writeNumber(1 / 2)
            writeNumber(7.5%3.5)
            writeNumber(7.8%3.38)
        end
        """
        expect = "2.0\n0.0\n2.0\n0.5\n0.5\n1.04\n"
        self.assertTrue(TestCodeGen.test(input, expect, 726))
        
        input = """
        func main ()
        begin
            writeNumber(1 + 1 + 1)
            writeNumber(1 + 1 * 3 - 1 * 2 / 2)
            writeNumber(2 * 3 % 2)
        end
        """
        expect = "3.0\n3.0\n0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 727))
        
        input = """
        func main ()
        begin
            writeBool(1 > 2) ## push -1
            writeBool(2 > 1) ## push 1
            writeBool(1 > 1) ## push 0
        end
        """
        expect = "false\ntrue\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 728))
        
        input = """
        func main ()
        begin
            writeBool(1 >= 2)
            writeBool(2 >= 1) 
            writeBool(1 >= 1) 
        end
        """
        expect = "false\ntrue\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 729))
        
        input = """
        func main ()
        begin
            writeBool(1 < 2) 
            writeBool(2 < 1) 
            writeBool(1 < 1) 
        end
        """
        expect = "true\nfalse\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 730))
        
        input = """
        func main ()
        begin
            writeBool(1 <= 2) 
            writeBool(2 <= 1) 
            writeBool(1 <= 1) 
        end
        """
        expect = "true\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 731))
        
        input = """
        func main ()
        begin
            writeBool(1 != 2) 
            writeBool(2 != 1) 
            writeBool(1 != 1) 
        end
        """
        expect = "true\ntrue\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 732))
        
        input = """
        func main ()
        begin
            writeBool(1 = 2) 
            writeBool(2 = 1) 
            writeBool(1 = 1) 
        end
        """
        expect = "false\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 733))
        
        input = """
        func main ()
        begin
            writeBool(true and true) 
            writeBool(true and false)
            writeBool(false and true) 
            writeBool(false and false)  
        end
        """
        expect = "true\nfalse\nfalse\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 734))
        
        input = """
        func main ()
        begin
            writeBool(true or true) 
            writeBool(true or false)
            writeBool(false or true) 
            writeBool(false or false)  
        end
        """
        expect = "true\ntrue\ntrue\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 735))
        
        input = """
        func main ()
        begin
            writeBool(true or true and false or true) 
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 736))
        
        input = """
        func main ()
        begin
            writeString("vo" ... "tien") 
        end
        """
        expect = "votien\n"
        self.assertTrue(TestCodeGen.test(input, expect, 737)) 
        
        input = """
        func main ()
        begin
            writeBool("vo" == "tien") 
            writeBool("tien" == "tien")
        end
        """
        expect = "false\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 738))
        
        input = """
        func main ()
        begin
            writeBool(not not true) 
            writeBool(not true)
            writeBool(not false)
        end
        """
        expect = "true\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 739))
        
        input = """
        func main ()
        begin
            writeNumber(--1) 
            writeNumber(-1)
        end
        """
        expect = "1.0\n-1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 740))
                    
    #* test visitFor 
    def test_5(self): 
        input = """
        func main ()
        begin
            var i <- 0
            for i until i >= 2 by 1
                writeNumber(i)
                
            writeNumber(i)
        end
        """
        expect = "0.0\n1.0\n0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 741))
        
        input = """
        func main ()
        begin
            var i <- 0
            for i until i >= 2 by 1
            begin
                i <- 1000
                break
            end
            writeNumber(i)
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 742))

        #* ảo ma canada
        input = """
        func main ()
        begin
            var i <- 0
            for i until i >= 1 by 1
                var k <- 2
            writeNumber(i)
            ## writeNumber(k)
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 743))
        
        
        input = """
        func main ()
        begin
            var i <- 0
            for i until i > 2 by 1
                writeNumber(i)
        end
        """
        expect = "0.0\n1.0\n2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 744))
        
        
        input = """
        func main ()
        begin
            var i <- 0
            for i until i > 2 by 2
                writeNumber(i)
        end
        """
        expect = "0.0\n2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 745))
        
        input = """
        func main ()
        begin
            var i <- 3
            for i until i > 2 by 2
                writeNumber(i)
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 746))
        
        input = """
        func main ()
        begin
            var i <- 0
            for i until i >= 2 by 1
            begin
                writeNumber(i)
                continue
                writeNumber(i)
            end
        end
        """
        expect = "0.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 747))
        
        input = """
        func main ()
        begin
            var i <- 0
            for i until i >= 2 by 1
            begin
                writeNumber(i)
                break
                writeNumber(i)
            end
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 748))
        
        input = """
        func main ()
        begin
            var i <- 0
            for i until i >= 2 by 1
                break
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 749))
             
    #* test visitIf và visitFor
    def test_9(self):
        input = """
            func main()
            begin
                if (true) writeNumber(1)
                else writeNumber(0)
            end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 750)) 

        input = """
            func main()
            begin
                if (2 > 3) writeNumber(1)
                else writeNumber(0)
            end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 751)) 

        input = """
            func main()
            begin
                if (2 = 2) writeNumber(1)
            end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 752)) 
                                              
        input = """
            func main()
            begin
                var a <- 1
                if (a = 0) writeNumber(1)
                elif (a = 1) writeNumber(2)
                elif (a = 2) writeNumber(3)
            end
        """
        expect = "2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 753)) 

        input = """
            func main()
            begin
                var a <- 2
                if (a = 0) writeNumber(1)
                elif (a = 1) writeNumber(2)
                elif (a = 2) writeNumber(3)
            end
        """
        expect = "3.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 754)) 
        
        input = """
            func main()
            begin
                var a <- 0
                if (a = 0) writeNumber(1)
                elif (a = 1) writeNumber(2)
                elif (a = 2) writeNumber(3)
            end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 755))  
        
        input = """
            func main()
            begin
                var a <- -1
                if (a = 0) writeNumber(1)
                elif (a = 1) writeNumber(2)
                elif (a = 2) writeNumber(3)
                else writeNumber(4)
            end
        """
        expect = "4.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 756)) 
        
        input = """
            func main()
            begin
                var a <- 0
                if (a = 0) var b <- 2
                elif (a = 1)  var b <- 3
                elif (a = 2)  var b <- 4
                else  var b <- 5
                writeNumber(b)
            end
        """
        expect = "2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 757))                
        
        input = """
            func main()
            begin
                var i <- 0
                for i until i >= 10 by 1
                begin
                    if (i = 3) break
                    writeNumber(i)
                end 
            end
        """
        expect = "0.0\n1.0\n2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 758))                
        
        input = """
            func main()
            begin
                var i <- 0
                for i until i >= 10 by 2
                begin
                    if (i = 3) break
                    writeNumber(i)
                end 
            end
        """
        expect = "0.0\n2.0\n4.0\n6.0\n8.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 759))                
        
                
    #* visitArrayCell và visitAssign  và khởi tạo array            
    def test_6(self): 
        input = """
        number a[2]
        func main ()
        begin
            writeNumber(a[1])
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 760))      
        
        input = """
        number a[2]
        func main ()
        begin
            writeNumber(a[1] + 1)
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 761))  
        
        input = """
        number a[2]
        func main ()
        begin
            var x <- a[0]
            writeNumber(x)
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 762))     
        
        input = """
        func main ()
        begin
            number a[2]
            var x <- a[0] + 2.5
            writeNumber(x)
        end
        """
        expect = "2.5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 763))     
        
        input = """
        number a[2, 3]
        func main ()
        begin
           writeNumber(a[0,0])
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 764))  
        
        input = """
        func main ()
        begin
            number a[2, 3]
           writeNumber(a[0,0])
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 765))  
        
        input = """
        func main ()
        begin
            number a[2,2,2,2]
           writeNumber(a[0,0,0,0])
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 766))  
        
        input = """
        func main ()
        begin
            number a[2,2,2,2]
            var c <- a[0,0,0]
           writeNumber(c[0])
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 767))  
        
        input = """
        number a[2]
        func main ()
        begin
           a[1] <- 1
           writeNumber(a[1])
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 768))  
        
        input = """
        number a[2]
        func main ()
        begin
           a[1] <- a[0] + 1
           writeNumber(a[1])
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 769))  
        
        input = """
        number a[2,2]
        func main ()
        begin
           a[1,1] <- a[0,0] + 1
           writeNumber(a[1,1])
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 770))  
        
        input = """
        func main ()
        begin
            number a[2,2]
           a[1,1] <- a[0,0] + 1
           writeNumber(a[1,1])
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 771)) 
        
        input = """
        func main ()
        begin
            number a[2,2]
           var b <- a[0]
           b[0] <- 1
           writeNumber(a[0,0])
           writeNumber(b[0])
        end
        """
        expect = "1.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 772)) 
        
        input = """
        bool a[2]
        bool b[2,2]
        func main ()
        begin
            writeBool(a[1])
            writeBool(b[0,0])
            a[0] <- true
            writeBool(a[0])
            b[0,0] <- true
            writeBool(b[0,0])
            var c <- b[0]
            c[1] <- true
            writeBool(b[0,1])
        end
        """
        expect = "false\nfalse\ntrue\ntrue\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 773)) 
        
        input = """
        func main ()
        begin
            bool a[2]
            bool b[2,2]
            writeBool(a[1])
            writeBool(b[0,0])
            a[0] <- true
            writeBool(a[0])
            b[0,0] <- true
            writeBool(b[0,0])
            var c <- b[0]
            c[1] <- true
            writeBool(b[0,1])
        end
        """
        expect = "false\nfalse\ntrue\ntrue\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 774)) 
        


    #* test visitArrayLiteral
    def test_7(self): 
        input = """
        number a[2] <- [1,2]
        func main ()
        begin
            writeNumber(a[1])
            writeNumber(a[0])
        end
        """
        expect = "2.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 775))   
        
        input = """
        func main ()
        begin
            number a[2] <- [1,2]
            writeNumber(a[1])
            writeNumber(a[0])
        end
        """
        expect = "2.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 776))          
        
        input = """
        func main ()
        begin
            dynamic a 
            a <- [1,2]
            writeNumber(a[1])
            writeNumber(a[0])
        end
        """
        expect = "2.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 777))    
        
        input = """
        dynamic a 
        func main ()
        begin
            a <- [1,2]
            writeNumber(a[1])
            writeNumber(a[0])
        end
        """
        expect = "2.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 778))   
        
        input = """
        var a <- [1,2]
        func main ()
        begin
            writeNumber(a[1])
            writeNumber(a[0])
        end
        """
        expect = "2.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 779))    
        
        input = """
        func main ()
        begin
            var a <- [3,2]
            writeNumber(a[1])
            writeNumber(a[0])
        end
        """
        expect = "2.0\n3.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 780))  
        
        input = """
        func main ()
        begin
            var a <- [[1],[2]]
            writeNumber(a[1,0])
            writeNumber(a[0,0])
        end
        """
        expect = "2.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 781))  
        
        input = """
        var a <- [[1],[2]]
        func main ()
        begin
            writeNumber(a[1,0])
            writeNumber(a[0,0])
        end
        """
        expect = "2.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 782))  
        
        input = """
        number a[2,1] <- [[1],[2]]
        func main ()
        begin
            writeNumber(a[1,0])
            writeNumber(a[0,0])
        end
        """
        expect = "2.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 783))  
        
        input = """
        func main ()
        begin
            number a[2,1] <- [[1],[2]]
            writeNumber(a[1,0])
            writeNumber(a[0,0])
        end
        """
        expect = "2.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 784))  
         
        input = """
        var b <- [true]
        func main ()
        begin
            bool a[2,1] <- [[true],[false]]
            writeBool(a[1,0])
            writeBool(a[0,0])
            writeBool(b[0])
        end
        """
        expect = "false\ntrue\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 785))  
        
        input = """
        bool a[2,1] <- [[true],[false]]
        func main ()
        begin
            var b <- [true]
            writeBool(a[1,0])
            writeBool(a[0,0])
            writeBool(b[0])
        end
        """
        expect = "false\ntrue\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 786))  
        
        input = """
        string a[2,1] <- [["v"],["o"]]
        func main ()
        begin
            var b <- ["tien"]
            writeString(a[1,0])
            writeString(a[0,0])
            writeString(b[0])
        end
        """
        expect = "o\nv\ntien\n"
        self.assertTrue(TestCodeGen.test(input, expect, 787))     
        
        input = """
        string b[1] <- ["tien"]
        func main ()
        begin
            var a <- [["v"],["o"]]
            writeString(a[1,0])
            writeString(a[0,0])
            writeString(b[0])
        end
        """
        expect = "o\nv\ntien\n"
        self.assertTrue(TestCodeGen.test(input, expect, 788))   
        
        input = """
        var a <- [[[[1]]]]
        func main ()
        begin
            var b <- a[0]
            var c <- b[0]
            var d <- c[0]
            d[0] <- 2
            writeNumber(a[0,0,0,0])
        end
        """
        expect = "2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 789))  
        
        input = """
        var a <- [[[[1]]]]
        func main ()
        begin
            var b <- a[0]
            var c <- b[0]
            var d <- c[0]
            a[0,0,0,0] <- 4
            writeNumber(d[0])
        end
        """
        expect = "4.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 790))  
        
        input = """
        func foo(number a[2])
        begin
            a[1] <- 2
        end
        func main ()
        begin
            number a[2]
            writeNumber(a[0])
            foo(a)
            writeNumber(a[1])
        end
        """
        expect = "0.0\n2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 791)) 
        
        input = """
        func foo(number a[2])
        begin
            a[0] <- 2
            a[1] <- 3
        end
        func main ()
        begin
            number a[2,2]
            writeNumber(a[0,0])
            foo(a[0])
            writeNumber(a[0,1])
        end
        """
        expect = "0.0\n3.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 792)) 
             
    #* test khởi tạo hàm và visitCallStmt và return
    def test_10(self):
        input = """
        func foo()
        begin
            writeNumber(1.0)
            return
            writeNumber(1.0)
        end        
        func main ()
        begin
            foo()
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 793))   
        
        input = """
        func foo(string a)
        begin
            writeString(a)
        end        
        func main ()
        begin
            foo("Votien")
        end
        """
        expect = "Votien\n"
        self.assertTrue(TestCodeGen.test(input, expect, 794)) 
        
        input = """
        func foo(string a)   
        func main ()
        begin
            foo("Votien")
        end
        func foo(string a)
        begin
            writeString(a)
        end     
        """
        expect = "Votien\n"
        self.assertTrue(TestCodeGen.test(input, expect, 795)) 
        
        input = """
        func foo(string a, bool b)   
        func main ()
        begin
            foo("Votien", true)
        end
        func foo(string a, bool b)
        begin
            writeString(a)
            writeBool(true)
        end     
        """
        expect = "Votien\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 796)) 
        

        input = """
        func foo()
        begin
            writeString("1")
        end  
        func foo1()
        begin
            writeString("2")
        end  
        func main ()
        begin
            foo()
            foo1()
        end
   
        """
        expect = "1\n2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 797)) 
    
        input = """
        func foo(number a)
        begin
            writeNumber(a)
        end  
        func main ()
        begin
            dynamic a
            a <- 1
            foo(a)
        end
   
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 798)) 
 
    #* Suy diễn kiểu 
    def test_8(self): 
        input = """
            func main()
            begin
                dynamic a
                
                begin 
                    a <- 1
                end
                    writeNumber(a)
            end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 799)) 
        
        input = """
            func main()
            begin
                number a
                writeNumber(a)
            end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 800)) 
        
        input = """
            func main()
            begin
                dynamic a
                writeNumber(a + 1)
            end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 801)) 
                   
        input = """
            func foo(number a)
                return a
            func main()
            begin
                dynamic a
                writeNumber(foo(a))
            end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 802)) 
                 
        input = """
            func main()
            begin
                dynamic a
                number b[3] <- [1,a,a]
                writeNumber(b[2])
                a <- 3
                writeNumber(a)
            end
        """
        expect = "0.0\n3.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 803)) 
                 
        input = """
            dynamic a
            func main()
            begin
                number b[2,2] <- [[1,1], [1,a]]
                a <- 3
                writeNumber(b[1,1])
            end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 804)) 
                 
        input = """
            func main()
            begin
                dynamic a <- [2,3]
                number b[2,2] <- [[1,1], a]
                writeNumber(b[1,1])
            end
        """
        expect = "3.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 805)) 
                 
                 
        # input = """
        #     func main()
        #     begin
        #         dynamic a
        #         number b[2,2] <- [[1,1], a]
        #         writeNumber(b[1,1])
        #     end
        # """
        # expect = "0.0\n"
        # self.assertTrue(TestCodeGen.test(input, expect, 806)) 
             
             
    #* test ALL    
    def test_99(self):  
        input = """
func areDivisors(number num1, number num2)
return ((num1 % num2 = 0) or (num2 % num1 = 0))
func main()
begin
var num1 <- 3
var num2 <- 4
if (areDivisors(num1, num2)) writeString("Yes")
else writeString("No")
end

        """
        expect = "No\n"
        self.assertTrue(TestCodeGen.test(input, expect, 807))  
    
        input = """
func areDivisors(number num1, number num2)
return ((num1 % num2 = 0) or (num2 % num1 = 0))
func main()
begin
var num1 <- 2
var num2 <- 4
if (areDivisors(num1, num2)) writeString("Yes")
else writeString("No")
end

        """
        expect = "Yes\n"
        self.assertTrue(TestCodeGen.test(input, expect, 808))  
        
        input = """
func isPrime(number x)
func main()
begin
number x <- 7
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
        expect = "Yes\n"
        self.assertTrue(TestCodeGen.test(input, expect, 809))

        input = """
    func isPrime(number x)
    func main()
    begin
    number x <- 59
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
        expect = "Yes\n"
        self.assertTrue(TestCodeGen.test(input, expect, 810))
            
        input = """
func isPrime(number x)
func main()
begin
number x <- -9
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
        expect = "No\n"
        self.assertTrue(TestCodeGen.test(input, expect, 811))
        
                
        input = """
func isPrime(number x)
func main()
begin
number x <- 24
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
        expect = "No\n"
        self.assertTrue(TestCodeGen.test(input, expect, 812))   
        
        input = """
func printArray(number x[10])
func main()
begin
    var a <- [1,2,3,4,5,6,7,8,9,10]
    printArray(a)
end

func printArray(number x[10])
begin
    var i <- 0
    for i until i >= 10 by 1
        writeNumber(x[i])
end

        """
        expect = "1.0\n2.0\n3.0\n4.0\n5.0\n6.0\n7.0\n8.0\n9.0\n10.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 813))  
        
        input = """
func printArray(number x[10])
func main()
begin
    var a <- [1,2,3,4,5,6,7,8,9,10]
    printArray(a)
end

func printArray(number x[10])
begin
    var i <- 0
    var c <- 0
    for i until i >= 10 by 1
    begin
        c <- c + x[i]
    end
    writeNumber(c)
end

        """
        expect = "55.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 814)) 
        
        input = """
func printArray(number x[10])
func main()
begin
    var a <- [1,2,3,4,5,6,7,8,9,10]
    printArray(a)
    var i <- 0
    for i until i >= 10 by 1
    begin
        writeNumber(a[i])
    end
end

func printArray(number x[10])
begin
    var i <- 0
    for i until i >= 10 by 1
    begin
        x[i] <-  x[i] + 1
    end
end
        """
        expect = "2.0\n3.0\n4.0\n5.0\n6.0\n7.0\n8.0\n9.0\n10.0\n11.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 815))                              
                                 

        input = """
func printMinArray(number x[10])
func main()
begin
    var a <- [1,2,3,4,5,0,7,8,9,10]
    var c <- printMinArray(a)
    writeNumber(c)
end

func printMinArray(number x[10])
begin
    var i <- 1
    var min <- x[0]
    for i until i >= 10 by 1
    begin
        if (min > x[i]) min <- x[i]
    end
    return min
end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 816))    
        
        input = """
func printMinArray(number x[10])
func main()
begin
    var a <- [1,2,3,4,5,0,7,8,-1,10]
    var c <- printMinArray(a)
    writeNumber(c)
end

func printMinArray(number x[10])
begin
    var i <- 1
    var min <- x[0]
    for i until i >= 10 by 1
    begin
        if (min > x[i]) min <- x[i]
    end
    return min
end
        """
        expect = "-1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 817))                             
                                 
    
        
        
        
        
        
    