import unittest
import entertainment2


class EntertainmentSystemTests(unittest.TestCase):

    @unittest.skipIf(entertainment2.regional_jet(), 'Not available on regional jets')
    def test_movie_license(self):
        daily_movie = entertainment2.get_daily_movie()
        licensed_movies = entertainment2.get_licensed_movies()
        self.assertIn(daily_movie, licensed_movies)

    @unittest.skipUnless(not entertainment2.regional_jet(), 'Not available on regional jets')
    def test_wifi_status(self):
        wifi_enabled = entertainment2.get_wifi_status()
        self.assertTrue(wifi_enabled)

    def test_device_temperature(self):
        if entertainment2.regional_jet():
            self.skipTest('Not available on regional jets')
        device_temp = entertainment2.get_device_temp()
        self.assertLess(device_temp, 35)

    def test_maximum_display_brightness(self):
        if entertainment2.regional_jet():
            self.skipTest('Not available on regional jets')
        brightness = entertainment2.get_maximum_display_brightness()
        self.assertAlmostEqual(brightness, 400)


if __name__ == '__main__':
    unittest.main()
