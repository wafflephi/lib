#!/usr/bin/env python3

import pandas as pd


def extract_col(fp: str, col: str, nums: bool = False) -> list:
    """Extract a column from csv file as a python list.

    :param fp: path to a csv file.
    :type fp: string
    :param col: column header
    :type col: string
    :param nums: if True format column contents as a floats
    :type nums: float
    :return: extracted column
    :rtype: list
    """

    lines = [line.split(",") for line in open(fp, "r").read().strip().split("\n")]
    headers = lines[0]
    try:
        column_index = headers.index(col)
    except ValueError:
        raise ValueError(f"There's no column '{col}' in {fp}")

    ret = []
    for line in lines[1::]:
        try:
            ret.append(float(line[column_index]) if nums else line[column_index])
        except IndexError:
            ret.append(None)
    return ret


def split_and_normalize(
    df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.Series, pd.Series,]:

    # column_indicies = {name: i for i, name in enumerate(df.columns)}

    n = len(df)

    train_df = df[0 : int(n * 0.7)]
    val_df = df[int(n * 0.7) : int(n * 0.9)]
    test_df = df[int(n * 0.9) :]

    # num_features = df.shape[1]

    train_mean = train_df.mean()
    train_std = train_df.std()

    train_df = (train_df - train_mean) / train_std
    val_df = (val_df - train_mean) / train_std
    test_df = (test_df - train_mean) / train_std

    return train_df, val_df, test_df, train_mean, train_std


def split_and_normalize_static(
    df: pd.DataFrame, starting_point: int = 0
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.Series, pd.Series,]:

    columns = {name: i for i, name in enumerate(df.columns)}
    train = pd.DataFrame(columns=columns)
    val = pd.DataFrame(columns=columns)
    test = pd.DataFrame(columns=columns)

    val = pd.concat(
        [val, df.iloc[starting_point::10], df.iloc[starting_point + 1 :: 10]]
    )
    val.reset_index(drop=True, inplace=True)

    test = df.iloc[starting_point + 2 :: 10]
    test.reset_index(drop=True, inplace=True)

    train_list = []

    # * Grab the rest of the data
    for i in range(starting_point + 3, 10):
        train_list.append(df.iloc[i::10])

    train = pd.concat(train_list)
    train.reset_index(drop=True, inplace=True)

    num_features = df.shape[1]
    train_mean = train.mean()
    train_std = train.std()

    train_df = (train - train_mean) / train_std
    val_df = (val - train_mean) / train_std
    test_df = (test - train_mean) / train_std
    return train_df, val_df, test_df, train_mean, train_std, num_features


def normalize(df: pd.DataFrame):
    train_mean = df.mean()
    train_std = df.std()
    train_df = (df - train_mean) / train_std
    return train_df
