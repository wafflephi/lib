import unittest

import numpy as np
import taichi as ti

import os
import sys

dir_ = os.getcwd().split('/')
if dir_[-1] == 'test':
  sys.path.insert(0, '../')

from wafflephi import average

ti.init() # speeds up for loops

def _mean(arr: list) -> float:
  return sum(arr)/len(arr) 

class TestAverages(unittest.TestCase):
  def test_mean(self):
    self.assertEqual(average.mean([4,36,45,50,75]), 42)

  @ti.data_oriented
  def test_ema(self):
    for i in range(100, 10000, 100):
      x = np.arange(-i, i)
      ema10_ = average.ema(x, 10)
      ema100_ = average.ema(x, 100)
      self.assertEqual(round(_mean(ema10_), 2), round(_mean(ema100_), 2))

if __name__ == "__main__":
  unittest.main()

