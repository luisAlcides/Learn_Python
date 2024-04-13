import unittest
import demo
class TestDemo(unittest.TestCase):
    def test_add(self):
        self.assertEqual(demo.add(2, 3), 5)
        self.assertEqual(demo.add(10,4), 14)
        self.assertEqual(demo.add(23, 7), 30)

    def test_sub(self):
        self.assertEqual(demo.sub(2,1), 1)

    def test_mul(self):
        self.assertEqual(demo.mul(5, 1), 5)

    def test_div(self):
        self.assertEqual(demo.div(8, 2), 4)


if __name__ == '__main__':
    unittest.main()