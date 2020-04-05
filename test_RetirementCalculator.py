import unittest
from RetirementCalculator import RetirementCalculator


class RetirementCalculatorTestCase(unittest.TestCase):
    def testRetirementCalc1(self):
        calculator = RetirementCalculator(21, 70000, 20, 1000000)
        self.assertEqual(
            calculator.getFinalAge(), 74, "Should be 74"
            )

    def testRetirementCalc2(self):
        calculator = RetirementCalculator(21, 70000, 20, 1000000000)
        self.assertEqual(
            calculator.getFinalAge(), 52932, "Should be 52932"
            )

    def testRetirementCalc3(self):
        calculator = RetirementCalculator(21, 70000, 20, 1000000)
        self.assertEqual(
            calculator.getGoalMet(), True, "Should be True"
            )

    def testRetirementCalc4(self):
        calculator = RetirementCalculator(21, 70000, 20, 1000000000)
        self.assertEqual(
            calculator.getGoalMet(), False, "Should be False"
            )
