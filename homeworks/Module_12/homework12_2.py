import tournament
import unittest
import pprint


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.runner1 = tournament.Runner('Усейн', 10)
        self.runner2 = tournament.Runner('Андрей', 9)
        self.runner3 = tournament.Runner('Ник', 3)


    @classmethod
    def tearDownClass(cls):
        pprint.pprint(cls.all_result)

    def test_start1(self):
        tour = tournament.Tournament(90, self.runner1, self.runner3)
        TournamentTest.all_result[1] = tour.start()
        self.assertTrue(TournamentTest.all_result[1][2] == 'Ник')

    def test_start2(self):
        tour = tournament.Tournament(90, self.runner2, self.runner3)
        TournamentTest.all_result[2] = tour.start()
        self.assertTrue(TournamentTest.all_result[2][2] == 'Ник')

    def test_start3(self):
        tour = tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        TournamentTest.all_result[3] = tour.start()
        self.assertTrue(TournamentTest.all_result[3][3] == 'Ник')


if __name__ == '__main__':
    unittest.main()
