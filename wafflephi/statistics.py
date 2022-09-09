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

class LinearRegression:
  def lstsq(self, X:List[float], Y:List[float]) -> Tuple[list, float, float]:
    """Least squares method.
      Reference https://en.wikipedia.org/wiki/Least_squares
    """

    assert len(X) == len(Y)

    N = len(X)

    X_mean = mean(X)
    Y_mean = mean(Y)

    X_sigma = sum(X)
    Y_sigma = sum(Y)

    XY_sigma = 0
    X_squared_sigma = 0

    for x, y in zip(X,Y):
      XY_sigma += x*y
      X_squared_sigma += x**2

    slope = ((N * XY_sigma) - (X_sigma  * Y_sigma)) / ((N * X_squared_sigma) - (X_sigma)**2)
    y_intercept = (Y_sigma - slope * X_sigma) / N

    slope_intercept = lambda X: (slope * x) + y_intercept

    est = []
    for x, _ in zip(X,Y):
      y = slope_intercept(x)
      est.append(y)

    return est, slope, y_intercept
