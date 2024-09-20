import unittest
import test_calc
import test_new_calc

calcST = unittest.TestSuite()
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_calc.CalcTest))  # можно добавлять разные тестовые файлы
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_new_calc.CalcNewTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcST)
