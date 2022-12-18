import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

class WindowGenerator:
  """
  Reference: 
  https://www.tensorflow.org/tutorials/structured_data/time_series
  """
  def __init__(self,
              input_width: int,
              label_width: int,
              shift: int,
              train_df: pd.DataFrame,
              val_df: pd.DataFrame,
              test_df: pd.DataFrame,
              label_columns: list[str] | None = None,
              ) -> None:

    self.train_df = train_df
    self.test_df = test_df
    self.val_df = val_df

    self.label_columns = label_columns
    if label_columns is not None:
      self.label_columns_indicies = {name: i for i, name in
                                      enumerate(label_columns)}
    self.column_indicies = {name: i for i, name in enumerate(train_df.columns)}

    self.input_width = input_width
    self.label_width = label_width
    self.shift = shift

    self.total_window_size = input_width + shift

    self.input_slice = slice(0, input_width)
    self.input_indices = np.arange(self.total_window_size)[self.input_slice]

    self.label_start = self.total_window_size - self.label_width
    self.labels_slice = slice(self.label_start, None)
    self.label_indices = np.arange(self.total_window_size)[self.labels_slice]

  def __repr__(self) -> str:
    return '\n'.join([
      f'Total window size: {self.total_window_size}',
      f'Input indices: {self.input_indices}',
      f'Label indices: {self.label_indices}',
      f'Label column name(s): {self.label_columns}'
    ])

  def split_window(self, features: tf.stack) -> tuple(tf.stack, tf.stack):
    inputs = features[:, self.input_slice, :]
    labels = features[:, self.labels_slice, :]

    if self.label_columns is not None: 
      labels = tf.stack(
        [labels[:,:,self.column_indicies[name]] for name in self.label_columns],
        axis = -1
      )

    inputs.set_shape([None, self.input_width, None])
    labels.set_shape([None, self.label_width, None])

    return inputs, labels

  def plot(self,
          model: tf.keras.Model | None = None,
          plot_col: str = 'Close',
          max_subplots: int = 3,
          xlabel: str = '15 min [quarters]', # this should be changed depening on the dataset
          ) -> None:
    inputs, labels = self.example
    plt.figure(figsize=(12,8))
    plot_col_index = self.column_indicies[plot_col]
    max_n = min(max_subplots, len(inputs))
    for n in range(max_n):
      plt.subplot(max_n, 1, n+1)
      plt.ylabel(f'{plot_col} [normed]')
      plt.plot(self.input_indices, inputs[n,:,plot_col_index], label='Inputs', marker='.', zorder=-10)

      if self.label_columns:
        label_col_index = self.label_columns_indicies.get(plot_col, None)
      else:
        label_col_index = plot_col_index

      if label_col_index is None:
        continue

      plt.scatter(self.label_indices, labels[n, :, label_col_index],
        edgecolors='k', label='Labels', c='#2ca02c', s=64
      )

      if model is not None:
        predictions = model(inputs)
        plt.scatter(self.label_indices, predictions[n, :, label_col_index],
          marker='X', edgecolors='k', label='Predictions',
          c='#ff7f0e', s=64
        )

      if n == 0:
        plt.legend()

    plt.xlabel(xlabel)

  def make_dataset(self, data: pd.DataFrame) -> tf.data.Dataset:
    data = np.array(data, dtype=np.float32)
    ds = tf.keras.utils.timeseries_dataset_from_array(
      data=data,
      targets=None,
      sequence_length=self.total_window_size,
      sequence_stride=1,
      shuffle=True,
      batch_size=32,
    )
    ds = ds.map(self.split_window)
    return ds

  @property
  def train(self) -> tf.data.Dataset:
    return self.make_dataset(self.train_df)

  @property
  def val(self) -> tf.data.Dataset:
    return self.make_dataset(self.val_df)

  @property
  def test(self) -> tf.data.Dataset:
    return self.make_dataset(self.test_df)

  @property
  def example(self) -> tf.data.Dataset:
    """
    Get and cache an example batch of `inputs, labels` for plotting.
    """

    result = getattr(self, '_example', None)
    if result is None:
      result = next(iter(self.train))
      self._example = result
    return result






if __name__ == '__main__':
  w = WindowGenerator()