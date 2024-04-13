import unittest
import demo2


@unittest.skip('SKipping this test for some reason')
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calculate = demo2.Calculate()

    def tearDown(self):
        print('This is a teardown method, executes after each test')

    def test_add(self):
        self.assertEqual(self.calculate.add(1, 2), 3)

    def test_div(self):
        self.assertEqual(self.calculate.div(40, 5), 8)
        with self.assertRaises(ValueError):
            self.calculate.div(10, 0)

class TestCalculate2(unittest.TestCase):
    def setUp(self):
        self.calculate = demo2.Calculate()

    def tearDown(self):
        print('This is a teardown method, executes after each test')

    def test_add(self):
        self.assertEqual(self.calculate.add(1, 2), 3)

    @unittest.skipIf(True, 'Skipping because the conditions is true')
    def test_div(self):
        self.assertEqual(self.calculate.div(40, 5), 8)
        with self.assertRaises(ZeroDivisionError):
            self.calculate.div(10, 0)


if __name__ == '__main__':
    unittest.main()
