import tensorflow as tf

import window

def compile_and_fit(model: tf.keras.Model, window: "window.WindowGenerator", patience: int = 5, epochs: int = 300) -> tf.keras.callbacks.History:
  early_stopping = tf.keras.callbacks.EarlyStopping(
                                                  monitor='val_loss',
                                                  patience=patience,
                                                  mode='min'
                                                  )
  model.compile(loss=tf.keras.losses.MeanSquaredError(),
                optimizer=tf.keras.optimizers.Adam(),
                metrics=[tf.keras.metrics.MeanAbsoluteError()])

  history = model.fit(window.train, epochs=epochs,
                      validation_data=window.val,
                      callbacks=[early_stopping])
  return history