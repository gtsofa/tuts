import unittest

from calculator import Calculator

class TddInPythonExample(unittest.TestCase):
    def test_add_method_returns_correct_results(self):
        calc = Calculator()
        result = calc.add(2,2)
        self.assertEqual(4, result)

if __name__ == '__main__':
    unittest.main()
