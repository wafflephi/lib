#!/usr/bin/env python3

from typing import List, Union, Tuple

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

class LinearRegression:
  def __init__(self, slope, y_intercept):
    self.slope = slope
    self.y_intercept = y_intercept

  def __repr__(self):
    return f'LinearRegression(slope={self.slope}, y_intercept={self.y_intercept})'

def linreg(X:List[float], Y:List[float]) -> Tuple[list, float, float]:
  """Least squares method.
    Reference https://en.wikipedia.org/wiki/Least_squares
  """

  assert len(X) == len(Y)
  XY_sigma = 0
  X_squared_sigma = 0
  for x,y in zip(X,Y):
    XY_sigma += x*y
    X_squared_sigma += x**2
  slope = ((len(X) * XY_sigma) - (sum(X) * sum(Y))) / ((len(X) * X_squared_sigma) - (sum(X))**2)
  y_intercept = (sum(Y) - slope * sum(X)) / len(X)

  return LinearRegression(slope, y_intercept)

def fit(linreg: "LinearRegression", data):
  ret = []
  slope_intercept = lambda x: (linreg.slope * x) + linreg.y_intercept
  n = len(data)

  for x in range(n): 
    est_y = slope_intercept(x)
    ret.append(est_y)
  return ret

if __name__ == "__main__":
  print(stdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))
