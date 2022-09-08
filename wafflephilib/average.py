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
  from parse import csv_column
  prices = csv_column('/tmp/e069dfb94b340f8df912e075c4ede2e7', 'Close', nums=True)
  print(prices)
  prices_ema = ema(prices, 10)
  print(prices_ema)