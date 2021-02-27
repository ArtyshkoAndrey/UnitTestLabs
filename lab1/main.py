import unittest
from unitTests import TestLab1

lab1_suite = unittest.TestSuite()
lab1_suite.addTest(unittest.makeSuite(TestLab1))

runner = unittest.TextTestRunner(verbosity=3)
runner.run(lab1_suite)
