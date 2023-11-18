import unittest

# assert statements
x = 5
assert x == 5, 'x no es igual a 5'

# unit testing
class TestAssertions(unittest.TestCase):

    def test_assert_equality(self):
        self.assertEqual(2 + 2, 4, 'La suma debe ser igual a 4')

    def test_assert_membership(self):
        my_list = [1, 2, 3, 4, 5]
        self.assertIn(3, my_list, '3 deberia estar en la lista')

    def test_assert_quantitative_methods(self):
        self.assertGreater(5, 2, '5 deberia ser mayor que 2')

    def test_assert_exception_warning_methods(self):
        with self.assertRaises(ValueError):
            raise ValueError('Este es un ValueError')

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(1 + 1, 3, 'Esta afiramacion fallara, pero se espera')

    @unittest.skipIf(True, 'Ejemplo de skipping test')
    @unittest.expectedFailure
    @unittest.parameterized.parameterized.expand([
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (10, -5, 5),
        (2, 3, 6)
    ])
    def test_parameterizing_tests(self, a, b, expected_result):
        result = a + b
        self.assertEqual(result, expected_result)


def setup_fixture():
    print('Configuracion del fixture')


def teardown_fixture():
    print('Limpieza del fixture')


class TestFixtures(unittest.TestCase):

    def setUp(self):
        setup_fixture()

    def test_fixture_a(self):
        print('Prueba de Feature A')

    def test_fixture_b(self):
        print('Prueba de Feature B')

    def tearDown(self):
        teardown_fixture()


@unittest.skip('Ejemplo de omitir prueba')
def test_skipping():
    print('Esta prueba sera omitida')


if __name__ == '__main__':
    unittest.main()
