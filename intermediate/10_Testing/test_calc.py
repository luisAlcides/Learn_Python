import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15, 'The result should be 15!')

    def test_divide_by_nonzero(self):
        result = calc.divide(10, 2)
        self.assertEqual(result, 5, 'The result should be 5!')

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
