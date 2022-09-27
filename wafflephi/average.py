#!/usr/bin/env python3

from typing import List

def mean(numbers:List[float]) -> float:
  return float(sum(numbers)/len(numbers))

def ema(data:List[float], period:int, smoothing:int=2) -> float:
  """Calculate an Exponential Moving Average.

  :param data: Input data sample
  :type data: List[float]
  :param period: Period of days
  :type period: int
  :param smoothing: Smoothing factor
  :default smoothing: 2
  :type smoothing: int

  :return: Exponential moving average of the data sample.
  :rtype: float
  """

  ret = [sum(data[:period]) / period]
  for x in data[period:]:
    ret.append((x * (smoothing / (1 + period))) + ret[-1] * (1 - (smoothing / (1+period))))
  return ret

if __name__ == "__main__":
  import numpy as np
  x = np.arange(-150, 150)
  ema_  = ema(x, 10)
  print(round(mean(ema_), 2))

