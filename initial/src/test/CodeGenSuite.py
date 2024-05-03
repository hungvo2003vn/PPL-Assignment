import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    
    # test cơ bản về hàm main và các hàm write
    def test_1(self):
        input = """
        func main ()
        begin
            writeNumber(1)
            writeBool(true)
            writeString("vohung")
        end
        """
        expect = "1.0\ntrue\nvohung\n"
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
    
    #* test var
    def test_2(self):
        input = """
        number a <- 1
        func main ()
        begin
            writeNumber(a)
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 702))   
        
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
            var b <- "vohung"
            begin
                a <- b
            end
            writeString(a)
        end
        """
        expect = "vohung\n"
        self.assertTrue(TestCodeGen.test(input, expect, 707))      
        
        input = """
        dynamic a <-1
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
        
    #* hàm experCall
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
        self.assertTrue(TestCodeGen.test(input, expect, 710)) 
        
        
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
        self.assertTrue(TestCodeGen.test(input, expect, 711)) 
        
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
        self.assertTrue(TestCodeGen.test(input, expect, 712))  
        
        input = """
        func main ()
        begin
            var a <- readString()
            writeString(a)
        end
        """
        expect = "-1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 713))  
        
        input = """
        func main ()
        begin
            var a <- readNumber()
            writeNumber(a)
        end
        """
        expect = "-1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 714))  
        
        input = """
        func main ()
        begin
            var a <- readBool() #* true
            writeBool(a)
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 715))  
        
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
        self.assertTrue(TestCodeGen.test(input, expect, 716))  
        
        input = """
        func foo()
            return "vohung"
        func main ()
        begin
            var a <- foo() ## true
            writeString(a)
        end
        """
        expect = "vohung\n"
        self.assertTrue(TestCodeGen.test(input, expect, 717)) 
        
    #* test binary
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
        self.assertTrue(TestCodeGen.test(input, expect, 718))
        
        input = """
        func main ()
        begin
            writeNumber(1 + 1 + 1)
            writeNumber(1 + 1 * 3 - 1 * 2 / 2)
            writeNumber(2 * 3 % 2)
        end
        """
        expect = "3.0\n3.0\n0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 719))
        
        input = """
        func main ()
        begin
            writeBool(1 > 2) ## push -1
            writeBool(2 > 1) ## push 1
            writeBool(1 > 1) ## push 0
        end
        """
        expect = "false\ntrue\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 720))
        
        input = """
        func main ()
        begin
            writeBool(1 >= 2)
            writeBool(2 >= 1) 
            writeBool(1 >= 1) 
        end
        """
        expect = "false\ntrue\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 721))
        
        input = """
        func main ()
        begin
            writeBool(1 < 2) 
            writeBool(2 < 1) 
            writeBool(1 < 1) 
        end
        """
        expect = "true\nfalse\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 722))
        
        input = """
        func main ()
        begin
            writeBool(1 <= 2) 
            writeBool(2 <= 1) 
            writeBool(1 <= 1) 
        end
        """
        expect = "true\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 723))
        
        input = """
        func main ()
        begin
            writeBool(1 != 2) 
            writeBool(2 != 1) 
            writeBool(1 != 1) 
        end
        """
        expect = "true\ntrue\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 724))
        
        input = """
        func main ()
        begin
            writeBool(1 = 2) 
            writeBool(2 = 1) 
            writeBool(1 = 1) 
        end
        """
        expect = "false\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 725))
        
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
        self.assertTrue(TestCodeGen.test(input, expect, 726))
        
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
        self.assertTrue(TestCodeGen.test(input, expect, 727))
        
        input = """
        func main ()
        begin
            writeBool(true or true and false or true) 
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 728))
        
        input = """
        func main ()
        begin
            writeString("vo" ... "hung") 
        end
        """
        expect = "vohung\n"
        self.assertTrue(TestCodeGen.test(input, expect, 729)) 
        
        input = """
        func main ()
        begin
            writeBool("vo" == "hung") 
            writeBool("hung" == "hung")
        end
        """
        expect = "false\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 730))
        
        input = """
        func main ()
        begin
            writeBool(not not true) 
            writeBool(not true)
            writeBool(not false)
        end
        """
        expect = "true\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 731))
        
        input = """
        func main ()
        begin
            writeNumber(--1) 
            writeNumber(-1)
        end
        """
        expect = "1.0\n-1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 732))
                 
    # * vong for  
    def test_5(self): 
        input = """
        func main ()
        begin
            var i <- 0
            for i until i >= 2 by 1
                writeNumber(i)
        end
        """
        expect = "0.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 733))
        
        input = """
        func main ()
        begin
            var i <- 0
            for i until i > 2 by 1
                writeNumber(i)
        end
        """
        expect = "0.0\n1.0\n2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 734))
        
        input = """
        func main ()
        begin
            var i <- 0
            for i until i > 2 by 2
                writeNumber(i)
        end
        """
        expect = "0.0\n2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 735))
        
        input = """
        func main ()
        begin
            var i <- 3
            for i until i > 2 by 2
                writeNumber(i)
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 736))
        
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
        self.assertTrue(TestCodeGen.test(input, expect, 737))
        
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
        self.assertTrue(TestCodeGen.test(input, expect, 738))
        
        input = """
        func main ()
        begin
            var i <- 0
            for i until i >= 2 by 1
                break
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 739))
         
         
    def test_6(self): 
        input = """
        number a[2]
        func main ()
        begin
            writeNumber(a[1])
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 740))      
        
        input = """
        number a[2]
        func main ()
        begin
            writeNumber(a[1] + 1)
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 741))  
        
        input = """
        number a[2]
        func main ()
        begin
            var x <- a[0]
            writeNumber(x)
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 742))     
        
        input = """
        func main ()
        begin
            number a[2]
            var x <- a[0] + 2.5
            writeNumber(x)
        end
        """
        expect = "2.5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 743))     
        
        input = """
        number a[2, 3]
        func main ()
        begin
           writeNumber(a[0,0])
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 744))  
        
        input = """
        func main ()
        begin
            number a[2, 3]
           writeNumber(a[0,0])
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 745))  
        
        input = """
        func main ()
        begin
            number a[2,2,2,2]
           writeNumber(a[0,0,0,0])
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 746))  
        
        input = """
        func main ()
        begin
            number a[2,2,2,2]
            var c <- a[0,0,0]
           writeNumber(c[0])
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 747))  
        
        input = """
        number a[2]
        func main ()
        begin
           a[1] <- 1
           writeNumber(a[1])
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 748))  
        
        input = """
        number a[2]
        func main ()
        begin
           a[1] <- a[0] + 1
           writeNumber(a[1])
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 749))  
        
        input = """
        number a[2,2]
        func main ()
        begin
           a[1,1] <- a[0,0] + 1
           writeNumber(a[1,1])
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 750))  
        
        input = """
        func main ()
        begin
            number a[2,2]
           a[1,1] <- a[0,0] + 1
           writeNumber(a[1,1])
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 751)) 
        
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
        self.assertTrue(TestCodeGen.test(input, expect, 752)) 
        
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
        self.assertTrue(TestCodeGen.test(input, expect, 753)) 
        
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
        self.assertTrue(TestCodeGen.test(input, expect, 754)) 
        

    #* array literals
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
        self.assertTrue(TestCodeGen.test(input, expect, 755))   
        
        input = """
        func main ()
        begin
            number a[2] <- [1,2]
            writeNumber(a[1])
            writeNumber(a[0])
        end
        """
        expect = "2.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 756))          
        
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
        self.assertTrue(TestCodeGen.test(input, expect, 757))    
        
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
        self.assertTrue(TestCodeGen.test(input, expect, 758))   
        
        input = """
        var a <- [1,2]
        func main ()
        begin
            writeNumber(a[1])
            writeNumber(a[0])
        end
        """
        expect = "2.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 759))    
        
        input = """
        func main ()
        begin
            var a <- [3,2]
            writeNumber(a[1])
            writeNumber(a[0])
        end
        """
        expect = "2.0\n3.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 760))  
        
        input = """
        func main ()
        begin
            var a <- [[1],[2]]
            writeNumber(a[1,0])
            writeNumber(a[0,0])
        end
        """
        expect = "2.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 761))  
        
        input = """
        var a <- [[1],[2]]
        func main ()
        begin
            writeNumber(a[1,0])
            writeNumber(a[0,0])
        end
        """
        expect = "2.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 762))  
        
        input = """
        number a[2,1] <- [[1],[2]]
        func main ()
        begin
            writeNumber(a[1,0])
            writeNumber(a[0,0])
        end
        """
        expect = "2.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 763))  
        
        input = """
        func main ()
        begin
            number a[2,1] <- [[1],[2]]
            writeNumber(a[1,0])
            writeNumber(a[0,0])
        end
        """
        expect = "2.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 764))  
         
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
        self.assertTrue(TestCodeGen.test(input, expect, 765))  
        
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
        self.assertTrue(TestCodeGen.test(input, expect, 766))  
        
        input = """
        string a[2,1] <- [["v"],["o"]]
        func main ()
        begin
            var b <- ["hung"]
            writeString(a[1,0])
            writeString(a[0,0])
            writeString(b[0])
        end
        """
        expect = "o\nv\nhung\n"
        self.assertTrue(TestCodeGen.test(input, expect, 767))     
        
        input = """
        string b[1] <- ["hung"]
        func main ()
        begin
            var a <- [["v"],["o"]]
            writeString(a[1,0])
            writeString(a[0,0])
            writeString(b[0])
        end
        """
        expect = "o\nv\nhung\n"
        self.assertTrue(TestCodeGen.test(input, expect, 768))   
        
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
        self.assertTrue(TestCodeGen.test(input, expect, 769))  
        
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
        self.assertTrue(TestCodeGen.test(input, expect, 770))  
        
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
        self.assertTrue(TestCodeGen.test(input, expect, 771)) 
         
         
         
    #* test khởi tạo hàm và visitCallStmt và return
    def test_3(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 772))   
        
        input = """
        func foo(string a)
        begin
            writeString(a)
        end        
        func main ()
        begin
            foo("Vohung")
        end
        """
        expect = "Vohung\n"
        self.assertTrue(TestCodeGen.test(input, expect, 773)) 
        
        input = """
        func foo(string a)   
        func main ()
        begin
            foo("Vohung")
        end
        func foo(string a)
        begin
            writeString(a)
        end     
        """
        expect = "Vohung\n"
        self.assertTrue(TestCodeGen.test(input, expect, 774)) 
        
        input = """
        func foo(string a, bool b)   
        func main ()
        begin
            foo("Vohung", true)
        end
        func foo(string a, bool b)
        begin
            writeString(a)
            writeBool(true)
        end     
        """
        expect = "Vohung\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 775)) 
        

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
        self.assertTrue(TestCodeGen.test(input, expect, 776)) 
    
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
        self.assertTrue(TestCodeGen.test(input, expect, 777)) 
        

        
        
    def test_1(self):
        input = """
        func main ()
        begin
            writeNumber(1)
            writeBool(true)
            writeString("vohung")
        end
        """
        expect = "1.0\ntrue\nvohung\n"
        self.assertTrue(TestCodeGen.test(input, expect, 778))
    
    def test_2(self):
        input = """
        number a
    
        func main ()
        begin
            writeNumber(1)
            writeBool(true)
            writeString("vohung")
        end
        """
        expect = "1.0\ntrue\nvohung\n"
        self.assertTrue(TestCodeGen.test(input, expect, 779))  
    
    
    
    
    
    
    
    def test_2(self): 
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
        self.assertTrue(TestCodeGen.test(input, expect, 780))
        
        input = """
        func main ()
        begin
            writeNumber(1 + 1 + 1)
            writeNumber(1 + 1 * 3 - 1 * 2 / 2)
            writeNumber(2 * 3 % 2)
        end
        """
        expect = "3.0\n3.0\n0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 781))
        
    def test_4(self): 
        input = """
        number a <- 1
        func main ()
        begin
            writeNumber(a)
            number a <- 2
            writeNumber(a)
        end
        """
        expect = "1.0\n2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 782))
        
    def test_5(self): 
        input = """
        func main ()
        begin
            writeBool(1 > 2)
        end
        """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input, expect, 783))      
        
        
        
        
        
        
        
        
        

    def test_5(self): 
        input = """
        
        func foo()
        begin
          ##  writeString("foo")
        end

        func main ()
        begin
        end
        """
        expect = "1.0\n2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 784))

     
    def test_5(self): 
        input = """
        number a
        
        func main ()
        begin
            writeNumber(a)
            number b
            writeNumber(b)
        end
        """
        expect = "0.0\n0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 785))

