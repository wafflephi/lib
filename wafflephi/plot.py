#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from typing import Optional, List, Union, Iterable

from wafflephi.statistics import linreg, fit

def trend(df: pd.DataFrame, label:Optional[str]=None, stdev:Optional[bool]=True) -> matplotlib.figure.Figure:
  Y = np.log10(df['Close'])
  X = range(df.shape[0])
  l = linreg(X, Y)
  est = fit(l, Y)

  fig, ax = plt.subplots(figsize=(20,10))

  DATES_INTERVAL = df.shape[0]//10
  plt.plot(X,Y)
  plt.plot(X, est, "--k", label="least squares method trend")

  if stdev:
    plt.plot(X, est + np.std(est)/2, "r", label="+ 2 STDEV")
    plt.plot(X, est + np.std(est)/4, "r", label="+ 1 STDEV")
    plt.plot(X, est - np.std(est)/4, "g", label="- 1 STDEV")
    plt.plot(X, est - np.std(est)/2, "g", label="- 2 STDEV")

  legend = plt.legend(loc='upper left', fontsize=18)
  ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda y, _: '{:g}'.format(10**y)))

  plt.xticks(range(0, df.shape[0], DATES_INTERVAL), df['Date'].loc[::DATES_INTERVAL], rotation=45, fontsize=20)
  plt.yticks(fontsize=18)
  plt.grid(True)
  plt.title(label if label else 'label not set', fontsize=30)
  plt.ylabel('Close Price in USD', fontsize=22)

  return fig

if __name__ == "__main__":
  import sys
  ticker = sys.argv[-1]
  df = pd.read_csv(f'https://stooq.com/q/d/l/?s={ticker}&i=m')
  print(df)
  fig = trend(df, ticker)
  plt.show()
