import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Addition Tests ---
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_addition_mixed_numbers(self):
        self.assertEqual(self.calc.add(-2, 3), 1)

    def test_addition_with_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)

    # --- Subtraction Tests ---
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtraction_resulting_in_negative(self):
        self.assertEqual(self.calc.subtract(4, 10), -6)

    def test_subtraction_with_zero(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)

    # --- Multiplication Tests ---
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    def test_multiplication_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_multiplication_mixed_signs(self):
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    # --- Division Tests ---
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_resulting_in_float(self):
        self.assertEqual(self.calc.divide(7, 2), 3.5)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))

    def test_division_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)

    def test_division_mixed_signs(self):
        self.assertEqual(self.calc.divide(10, -2), -5)


if __name__ == "__main__":
    unittest.main()
