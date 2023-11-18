# Expected failures

import unittest


class MyTest(unittest.TestCase):

    @unittest.expectedFailure
    def test_division_by_zero(self):
        result = 10 / 0
        self.assertEqual(result, 5)

    @unittest.expectedFailure
    def test_index_out_of_range(self):
        my_list = [1, 2, 3]
        element = my_list[5]
        self.assertEqual(element, 4)


class FeatureTests(unittest.TestCase):

    @unittest.expectedFailure
    def test_broken_feature(self):
        raise Exception("This test is going to fail")


if __name__ == '__main__':
    unittest.main()
