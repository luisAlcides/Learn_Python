import unittest
import entertainment


class EntertainmentTest(unittest.TestCase):

    def test_movie_license(self):
        daily_movie = entertainment.get_daily_movie()
        licensed_movies = entertainment.get_licensed_movies()
        self.assertIn(daily_movie, licensed_movies)

    def test_wifi_status(self):
        wifi_enabled = entertainment.get_wifi_status()
        self.assertTrue(wifi_enabled)

    def test_device_temperature(self):
        device_temp = entertainment.get_device_temp()
        self.assertLess(device_temp, 35)

    def test_maximum_display_brightness(self):
        brightness = entertainment.get_maximum_display_brightness()
        self.assertAlmostEqual(brightness, 400)


unittest.main()
