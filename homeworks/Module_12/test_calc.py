import unittest
import calc


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

    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)

    def test_mul(self):
        self.assertEqual(calc.mul(1, 2), 2)


if __name__ == '__main__':
    unittest.main()
