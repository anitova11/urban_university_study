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
        tour = tournament.Tournament(90, self.runner3, self.runner2, self.runner1)
        TournamentTest.all_result[3] = tour.start()
        self.assertTrue(TournamentTest.all_result[3][3] == 'Ник')  # Ник здесь будет 3м, но на 1м месте Андрей

    def test_start4(self):
        tour = tournament.Tournament(90, *sorted([self.runner3, self.runner2, self.runner1],
                                                 key=lambda x: x.speed, reverse=True))
        TournamentTest.all_result[3.1] = tour.start()
        self.assertTrue(TournamentTest.all_result[3.1][1] == 'Усейн')  # если добавить сортировку при создании tour


if __name__ == '__main__':
    unittest.main()
