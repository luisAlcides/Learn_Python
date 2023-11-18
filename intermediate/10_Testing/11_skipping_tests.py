# skipping tests

import sys
import unittest


class LinuxTests(unittest.TestCase):

    @unittest.skipUnless(sys.platform.startswith('linux'), 'this test only runs on Linux')
    def test_linux_feature(self):
        print('This test should only run on linux')

    @unittest.skipIf(not sys.platform.startswith('linux'), 'this test only runs on linux')
    def test_other_linux_feature(self):
        print('This test should only run on linux')

    def test_linux_feature2(self):
        if not sys.platform.startswith('linux'):
            self.skipTest('Test only runs on linux 2 ')


if __name__ == '__main__':
    unittest.main()