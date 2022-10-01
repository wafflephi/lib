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
  def lstsq(X:List[float], Y:List[float]) -> Tuple[list, float, float]:
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
    slope_intercept = lambda x: (slope * x) + y_intercept
    estimates = []
    for x,y in zip(X,Y):
      estimation_y = slope_intercept(x)
      estimates.append(estimation_y)
    return estimates, slope, y_intercept

if __name__ == "__main__":
  print(stdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))