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

def plot_data(df: pd.DataFrame, date_time: pd.dat) -> None:
  plot_cols = ['Close',"SMA_8","SMA_20", 'SMA_Ratio_MA','RSI_MA']
  features = df[plot_cols]

  features.index = date_time
  features.plot(subplots=True)

def plot_speard(df: pd.DataFrame) -> None:
  train_df, val_df, test_df, train_mean, train_std = split_and_normalize(df)
  std = (df - train_mean) / train_std
  std = std.melt(var_name='Column', value_name='Normalised')
  plt.figure(figsize=(12,6))
  ax = sns.violin(x='Column', y='Normalized', data=std)
  _ = ax.set_xticklabels(df.keys(), rotation=90)

def plot_wieght(df: pd.DataFrame, conv_model: tf.keras.Model) -> None:
  train_df, val_df, test_df, train_mean, train_std = split_and_normalize(df)
  plt.bar(x = range(len(train_df.columns)), height=conv_model.layers[0].kernel[:,0].numpy())
  ax = plt.gca()
  ax.set_xticks(range(len(train_df.columns)))
  _ = ax.set_xticklabels(train_df.columns, rotation=90)

if __name__ == "__main__":
  import sys
  ticker = sys.argv[-1]
  df = pd.read_csv(f'https://stooq.com/q/d/l/?s=^spx&d1=19500501&d2=20001115&i=d')
  print(df)
  fig = trend(df, ticker)
  plt.show()
