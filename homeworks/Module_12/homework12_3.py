import unittest
import homework12_1
import homework12_2

runnerST = unittest.TestSuite()
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(homework12_1.RunnerTest))
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(homework12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnerST)
