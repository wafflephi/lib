#!/usr/bin/env python3

import unittest

import os
import sys
import numpy as np

dir_ = os.getcwd().split('/')
if dir_[-1] == 'test':
  sys.path.insert(0, '../')

from wafflephi import statistics

# accurate up to 13th decimal point
ROUND = 13

class TestMean(unittest.TestCase):
  def test_basic(self):
    for _ in range(100):
      arr = list(np.random.uniform(-1, 0, 1000))
      self.assertEqual(statistics.mean(arr), sum(arr)/len(arr))

class TestStandardDeviation(unittest.TestCase):
  def test_small(self):
    for x in range(100):
      self.assertEqual(statistics.stdev([x]), .0)
      self.assertEqual(statistics.stdev([x, x+1]), .5)
      self.assertEqual(statistics.stdev([x, x+1, x+2]), 0.816496580927726)
      self.assertEqual(statistics.stdev([x, x+1, x+2, x+3]), 1.118033988749895)

  def test_mixed_arrays(self):
    arr = [6,2,3,1]
    self.assertEqual(statistics.stdev(arr), statistics.stdev(sorted(arr)))
    arr = np.random.uniform(-1, 0, 1000)
    self.assertEqual(round(statistics.stdev(arr), ROUND), round(statistics.stdev(sorted(arr)), ROUND))

  def test_cmp_numpy(self):
    for _ in range(100):
      sample_data = np.random.uniform(-1, 0, 1000)
      numpy_res = np.std(sample_data)
      my_res = statistics.stdev(sample_data)
      self.assertEqual(round(numpy_res, ROUND), round(my_res, ROUND)) 
