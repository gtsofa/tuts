import unittest

from calculator import Calculator

class TddInPythonExample(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    def test_add_method_returns_correct_results(self):
        result = self.calc.add(2,2)
        self.assertEqual(4, result)

    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')

    def test_calculator_returns_error_message_if_a_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 3)
    def test_calculator_returns_error_message_if_b_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 2, 'three')

if __name__ == '__main__':
    unittest.main()
