import unittest
import entertainment


class EntertainmentSystemTests(unittest.TestCase):

    def test_movie_license(self):
        # Checkpoint 1
        daily_movies = entertainment.get_daily_movies()
        licensed_movies = entertainment.get_licensed_movies()

        # Checkpoint 2
        for movie in daily_movies:
            print(movie)
            # Checkpoint 3 & 4
            with self.subTest(movie):
                self.assertIn(movie, licensed_movies)


unittest.main()
