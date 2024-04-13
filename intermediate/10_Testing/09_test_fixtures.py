# test fixtures
import unittest


def power_cycle_device():
    print('Power cycling bluetooth device...')


class BluetoothDeviceTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        power_cycle_device()

    def test_feature_a(self):
        print('Testing_unittest Feature A')

    def test_feature_b(self):
        print('Testing_unittest Feature B')

    @classmethod
    def tearDownClass(cls):
        power_cycle_device()


if __name__=='__main__':
    unittest.main()
