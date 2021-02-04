import unittest
import calculator

class TestCase(unittest.TestCase):
    #addition cases
    def test_add1(self):
        result = calculator.add(2, 2)
        self.assertEqual(result, 4)

    def test_add2(self):
        result = calculator.add(-2, 2)
        self.assertEqual(result, 0)

    def test_add3(self):
        result = calculator.add(-2, -2)
        self.assertEqual(result, -4)

    #subtraction cases
    def test_sub1(self):
        result = calculator.sub(2, 2)
        self.assertEqual(result, 0)

    def test_sub2(self):
        result = calculator.sub(-2, 2)
        self.assertEqual(result, -4)

    def test_sub3(self):
        result = calculator.sub(-2, -2)
        self.assertEqual(result, 0)

    #multiplication cases
    def test_mult1(self):
        result = calculator.mult(2, 2)
        self.assertEqual(result, 4)

    def test_mult2(self):
        result = calculator.mult(-2, 2)
        self.assertEqual(result, -4)

    def test_mult3(self):
        result = calculator.mult(-2, -2)
        self.assertEqual(result, 4)

    #division cases
    def test_div1(self):
        result = calculator.div(2, 2)
        self.assertEqual(result, 1)

    def test_div2(self):
        result = calculator.div(-2, 2)
        self.assertEqual(result, -1)

    def test_div3(self):
        result = calculator.div(-2, -2)
        self.assertEqual(result, 1)
    
    def test_div4(self):
        result = calculator.div(0, 2)
        self.assertEqual(result, 0)
    
    def test_div5(self):
        result = calculator.div(2, 0)
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()   