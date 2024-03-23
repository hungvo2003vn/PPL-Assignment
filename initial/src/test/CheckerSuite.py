import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    
    def test_a(self):
        input = """
            func a(number a, number c[3])
            func main() begin 
            end
            func a(number a, number c[3]) begin
                number c
            end
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 401)) 
                
    
    def test_no_entry_point(self):
        input = """
            number a
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 402))

        input = """
            number a
            func VoTien() begin 
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 403))
        
        input = """
            number a
            func main(number a) begin 
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 404))
        
        input = """
            number a
            func main(number a, number c[1]) begin 
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 405))
        
        input = """
            number main
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 406))


        input = """
            number a
            func main() begin 
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 407))
        
    def test_Break_Continue_in_loop(self):
        input = """
            func main() begin 
                number i
                for i until true by 1
                begin
                    break
                    continue
                    begin
                        break
                        continue
                    end
                    break
                    continue
                    for i until true by 1
                    begin
                        for i until true by 1
                        begin
                            break
                            continue
                        end
                        break
                        continue
                    end
                        break
                        continue
                    begin
                        break
                        continue
                    end
                end
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 408))

        input = """
            func main() begin 
                number i
                for i until true by 1
                begin
                    number i
                end
                break
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 409))    
        
        input = """
            func main() begin 
                number i
                for i until true by 1
                begin
                    begin
                        number i
                    end
                end
                continue
            end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 410))   
        
        
            
    
    def test_no_definition_for_a_funtion_And_Redeclared(self):
        input = """
            func a()
            func main() begin 
            end
        """
        expect = "No Function Definition: a"
        self.assertTrue(TestChecker.test(input, expect, 411))

        input = """
            func a()
            
            func a(number c) begin 
            end
            func main() begin 
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 412))    

        input = """
            func a(number c)
            
            func a(number d) begin 
            end
            func main() begin 
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 413))  
                
        input = """
            func a(number c)
            
            func a() begin 
            end
            func main() begin 
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 414))    
        
        input = """
            func a(number c)
            
            func a(string a) begin 
            end
            func main() begin 
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 415))    
        
        input = """
            func a() begin 
            end
            func a()
            func main() begin 
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 416))    

        input = """
            func a()
            func a(string c)
            func main() begin 
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 417)) 
                
        input = """
            func a() begin 
            end
            func a() begin 
            end
            func main() begin 
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 418))    
        
        input = """
            func a(number a) begin 
            end
            func a(string c) begin 
            end
            func main() begin 
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 419))    

        input = """
            func a() begin 
            end
            func a()
            func main() begin 
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 420))    
        
                
        input = """
            func a(number a) begin 
            end
            func a(string c)
            func main() begin 
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 421))  
        
        input = """
            number a
            func main() begin 
            end
            func a(string c)

        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 422))  
        
        input = """
            func a(string c)
            func main() begin 
            end
            number a

        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 423)) 
        
        input = """
            string a
            func main() begin 
            end
            number a
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 424)) 
        
        input = """
            func a(number a, number c, string a)
            func main() begin 
            end
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 425)) 
        
        input = """
            func a(number a, number c, string a)
            func main() begin 
            end
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 426)) 
        
        input = """
            func a(number a, number c[3])
            func main() begin 
            end
            func a(number a, number a[3]) begin
            end
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 427)) 
        
        input = """
            func a(number a, number c[3])
            func main() begin 
            end
            func a(number a, number c[3]) begin
                number a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 428)) 

        input = """
            func a(number a, number c[3])
            func main() begin 
            end
            func a(number a, number c[3]) begin
                number writeString
                number c
            end
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 429)) 
                

        input = """
            func a(number a, number c[3])
            func main() begin 
            end
            func a(number a, number c[3]) begin
                number e
                string e
            end
        """
        expect = "Redeclared Variable: e"
        self.assertTrue(TestChecker.test(input, expect, 430)) 
               

        input = """
            func a(number a, number c[3])
            func main() begin 
            end
            func a(number a, number c[3]) begin
                number e
                number k
                string e
            end
        """
        expect = "Redeclared Variable: e"
        self.assertTrue(TestChecker.test(input, expect, 431)) 
               
        input = """
            func a(number a, number c[3])
            func main() begin 
            end
            func a(number a, number c[3]) begin
                number e
                begin
                    number a
                    number e
                    number k
                    string k
                end
            end
        """
        expect = "Redeclared Variable: k"
        self.assertTrue(TestChecker.test(input, expect, 432)) 
               
        input = """
            func a(number a, number c[3])
            func main() begin 
            end
            func a(number a, number c[3]) begin
                number e
                begin
                    number e
                    number z
                    begin
                        number e
                    end
                    number z
                end
            end
        """
        expect = "Redeclared Variable: z"
        self.assertTrue(TestChecker.test(input, expect, 433)) 
        
        
        # check Type array
        input = """
            func a(number a[1,3,4])
            func main() begin 
            end
            func a(number a[1,3,2]) begin
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 434)) 

        input = """
            func a(number a[1,3])
            func main() begin 
            end
            func a(number a[1,3,2]) begin
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 435)) 
                             
        input = """
            func a(number a[1,3,2,4])
            func main() begin 
            end
            func a(number a[1,3,2]) begin
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 436)) 
                             
        input = """
            func a(number a[1,3,2])
            func main() begin 
            end
            func a(string a[1,3,2]) begin
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 437)) 

        input = """
            number readNumber
            func main() begin 
            end
        """
        expect = "Redeclared Variable: readNumber"
        self.assertTrue(TestChecker.test(input, expect, 438))              

        input = """
            func readNumber()
            func main() begin 
            end
        """
        expect = "Redeclared Function: readNumber"
        self.assertTrue(TestChecker.test(input, expect, 439))    

        input = """
            func readNumber() begin
            end
            func main() begin 
            end
        """
        expect = "Redeclared Function: readNumber"
        self.assertTrue(TestChecker.test(input, expect, 440))          

        input = """
            func writeString()
            func main() begin 
            end
        """
        expect = "Redeclared Function: writeString"
        self.assertTrue(TestChecker.test(input, expect, 441))    

        input = """
            func writeString() begin
            end
            func main() begin 
            end
        """
        expect = "Redeclared Function: writeString"
        self.assertTrue(TestChecker.test(input, expect, 442)) 
        
                
        input = """
            func a(number a[1,3,2])
            func main() begin 
            end
            func a(number a[1,3,2]) begin
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 443)) 

    
    def test_Undeclared(self):
     

        input = """
            number a
            number b
            var c <- c
            var d <- z
            func main() begin 
            end
        """
        expect = "Undeclared Identifier: z"
        self.assertTrue(TestChecker.test(input, expect, 444))   
        
        input = """
            number a
            number b
            var c <- d
            func main() begin 
            end
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 445))  
        
        input = """
            number a
            number b
            var c <- a
            func main() begin 
                var c <- c
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 446))    
    
        input = """
            number a
            number b
            var c <- a
            func main() begin 
                var c <- d
            end
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 447))   
        
        input = """
            number a
            number b
            var c <- a
            func main(number k, number j) begin 
                var x <- k
                var y <- c
                var c <- d
            end
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 448))  
        
        input = """
            number a
            number b
            var c <- a
            func main(number k, number j) begin 
                number z <- z
                begin
                    var c <- a
                    var b <- x
                end
            end
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 449))  
        
        input = """
            func a()
                return 1
            func main(number k, number j) begin 
                var c <- a()
                var d <- b()
            end
        """
        expect = "Undeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, 450))  
        
        input = """
            func a()
                return 1
            func main(number k, number j) begin 
                var c <- a
            end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 451)) 
        
        input = """
            func a()
                return 1
            func main(number k, number j) begin 
                var c <- k()
            end
        """
        expect = "Undeclared Function: k"
        self.assertTrue(TestChecker.test(input, expect, 452)) 

        input = """
            func a()
                return 1
            func main(number k, number j) begin 
                number a
                var c <- a()
            end
        """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 453)) 

        input = """
            func a()
                return 1
            func main(number k, number j) begin 
                number a <- a()
            end
        """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 454)) 
        
        
                
        input = """
            func a()
                return
            func main(number k, number j) begin 
                a()
                b()
            end
        """
        expect = "Undeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, 455)) 
        
        input = """
            func a() begin
                a()
                main()
            end
            func main() begin 

            end
        """
        expect = "Undeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 456)) 
        
        input = """
            func a()
            func main() begin 
                a()
                writeNumber(1.1)
                writeString("string")
                writeBool(true)
                var a <- readNumber()
                var b <- readString()
                var c <- readBool()
            end
            func a() return
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 457)) 
           