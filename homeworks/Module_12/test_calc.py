import unittest
import calc
import random


class CalcTest(unittest.TestCase):
    def setUp(self):  # перед каждым тестом запускается
        print('hi new test')

    @classmethod
    def setUpClass(cls):  # запускается в самом начале перед всеми методами
        print('hi all tests')

    def tearDown(self):  # запускается после каждого теста
        print('bye test')

    @classmethod
    def tearDownClass(cls):  # после всех методов
        print('bye all tests')

    @unittest.skip('Причина пропуска')
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)

    @unittest.skipIf(random.randint(0, 5) > 2, 'Число больше двух, поэтому не будет теста')
    def test_mul(self):
        self.assertEqual(calc.mul(1, 2), 2)


if __name__ == '__main__':
    unittest.main()
