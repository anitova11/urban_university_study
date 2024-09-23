import logging
import unittest
import runner_tour_exc


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_walk(self):
        try:
            hum = runner_tour_exc.Runner('ksu', -12)
            logging.info(f'test_walk выполнен успешно')
            for i in range(10):
                hum.walk()
            self.assertEqual(hum.distance, 120)
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            hum = runner_tour_exc.Runner(1, 12)
            logging.info(f'test_run выполнен успешно')
            for i in range(10):
                hum.run()
            self.assertEqual(hum.distance, 100)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        hum1 = runner_tour_exc.Runner('ksu')
        hum2 = runner_tour_exc.Runner('nick')

        for i in range(10):
            hum1.run()

        for i in range(10):
            hum2.walk()

        self.assertNotEqual(hum1.distance, hum2.distance)


if __name__ == '__main__':
    unittest.main()
logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        format='%(asctime)s | %(levelname)s | %(message)s', encoding='utf-8')

