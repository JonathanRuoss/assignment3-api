import unittest
from BmiCalculator import BmiCalculator


class BmiCalculatorTestCase(unittest.TestCase):
    def testUnderweightBmiVal(self):
        calculator = BmiCalculator(6, 0, 100)
        self.assertEqual(
            calculator.getBmiVal(), 13.9, "Should be 13.9"
            )

    def testNormalweightBmiVal(self):
        calculator = BmiCalculator(6, 0, 170)
        self.assertEqual(
            calculator.getBmiVal(), 23.6, "Should be 23.6"
            )

    def testOverweightBmiVal(self):
        calculator = BmiCalculator(6, 0, 200)
        self.assertEqual(
            calculator.getBmiVal(), 27.8, "Should be 27.8"
            )
    
    def testObeseBmiVal(self):
        calculator = BmiCalculator(6, 0, 250)
        self.assertEqual(
            calculator.getBmiVal(), 34.7, "Should be 34.7"
            )

    def testUnderweightBmiCat(self):
        calculator = BmiCalculator(6, 0, 100)
        self.assertEqual(
            calculator.getBmiCat(), "Underweight", "Should be Underweight"
            )

    def testNormalweightBmiCat(self):
        calculator = BmiCalculator(6, 0, 170)
        self.assertEqual(
            calculator.getBmiCat(), "Normal weight", "Should be Normal weight"
            )

    def testOverweightBmiCat(self):
        calculator = BmiCalculator(6, 0, 200)
        self.assertEqual(
            calculator.getBmiCat(), "Overweight", "Should be Overweight"
            )

    def testObeseBmiCat(self):
        calculator = BmiCalculator(6, 0, 250)
        self.assertEqual(
            calculator.getBmiCat(), "Obese", "Should be Obese"
            )
