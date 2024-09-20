import unittest
import calc


class CalcNewTest(unittest.TestCase):

    def test_new_div(self):
        self.assertEqual(calc.div(4, 2), 2.0)


if __name__ == '__main__':
    unittest.main()
