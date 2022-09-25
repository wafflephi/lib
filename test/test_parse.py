#!/usr/bin/env python3

import os
import sys
import csv
import shutil
import tempfile
import unittest
from io import StringIO


dir_ = os.getcwd().split('/')
if dir_[-1] == 'test':
  sys.path.insert(0, '../')

from wafflephi import parse

lines = \
"""Header1,Header2
value1,value2
value3,value4"""

def mock_csv() -> str:
  fp = os.path.join('/tmp', 'wafflephi-test')
  with open(fp, 'w') as file:
    file.write(lines)

  return fp


fp = mock_csv()

class TestParse(unittest.TestCase):
  def test_basic(self):
    cmp1 = ['value1', 'value3']
    cmp2 = ['value2', 'value4']

    self.assertEqual(parse.extract_col(fp, 'Header1'), cmp1)
    self.assertEqual(parse.extract_col(fp, 'Header2'), cmp2)

  def test_non_existant_header(self):
    with self.assertRaises(ValueError):
      parse.extract_col(fp, 'Header3')



if __name__ == "__main__":
  unittest.main()