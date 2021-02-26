import unittest
from lab1 import lab1

class TestLab1(unittest.TestCase):

  def test_day(self):
    lab = lab1()
    self.assertEqual(lab.lab(25, 12, 24, 12, 2000), 1)

  def test_nextBirthday(self):
    lab = lab1()
    self.assertEqual(lab.lab(24, 12, 25, 12, 2000), 364)

  def test_typeError(self):
    lab = lab1()
    self.assertEqual(lab.lab(242, 12, 25, 12, 2000), None)

if __name__ == '__main__':
    unittest.main()