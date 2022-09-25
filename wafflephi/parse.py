#!/usr/bin/env python3

def extract_col(fp: str, col: str, nums:bool=False) -> list:
  """Extract a column from csv file as a python list.

  :param fp: path to a csv file.
  :type fp: string
  :param col: column header
  :type col: string
  :param nums: if True format column contents as a floats
  :type nums: float
  :return: extracted column
  :rtype: list
  """

  lines = [line.split(',') for line in open(fp, 'r').read().strip().split('\n')]
  headers = lines[0]
  try:
    column_index = headers.index(col)
  except ValueError:
    raise ValueError(f"There's no column '{col}' in {fp}")

  ret = []
  for line in lines[1::]:
    if not nums:
      ret.append(line[column_index])
    else:
      ret.append(float(line[column_index]))
  return ret
