import unittest
import human


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        hum = human.Runner('ksu')
        for i in range(10):
            hum.walk()
        self.assertEqual(hum.distance, 50)

    def test_run(self):
        hum = human.Runner('ksu')
        for i in range(10):
            hum.run()
        self.assertEqual(hum.distance, 100)

    def test_challenge(self):
        hum1 = human.Runner('ksu')
        hum2 = human.Runner('nick')

        for i in range(10):
            hum1.run()

        for i in range(10):
            hum2.walk()

        self.assertNotEqual(hum1.distance, hum2.distance)


if __name__ == '__main__':
    unittest.main()