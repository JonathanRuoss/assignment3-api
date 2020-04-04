import unittest
from RetirementCalculator import RetirementCalculator

class RetirementCalculatorTestCase(unittest.TestCase):
    def testRetirementCalc(self):
        calculator = RetirementCalculator(21, 70000, 20, 1000000)
        self.assertEqual(calculator.getFinalAge(), 74, "Should be 74")

if __name__ == '__main__':
    unittest.main()