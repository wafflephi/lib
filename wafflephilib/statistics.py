#!/usr/bin/env python3

from typing import List, Union

def mean(data: List[Union[int, float]]) -> Union[int, float]:
  return sum(data)/len(data)

def stdev(sample: List[Union[int, float]]) -> float:
  """Calculate standard deviation from sample data.
  """
  mean_ = mean(sample)
  acc = 0
  for x in sample:
    acc += (x-mean_)**2
  return (acc/len(sample))**0.5


  