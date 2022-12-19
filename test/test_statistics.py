#!/usr/bin/env python3

import unittest

import os
import sys
import numpy as np
import scipy.stats

dir_ = os.getcwd().split("/")
if dir_[-1] == "test":
    sys.path.insert(0, "../")

from wafflephi import statistics

# accurate up to 12th decimal point
ROUND = 12


class TestMean(unittest.TestCase):
    def test_basic(self):
        for _ in range(100):
            arr = list(np.random.uniform(-1, 0, 1000))
            self.assertEqual(statistics.mean(arr), sum(arr) / len(arr))


class TestStandardDeviation(unittest.TestCase):
    def test_small(self):
        for x in range(100):
            self.assertEqual(statistics.stdev([x]), 0.0)
            self.assertEqual(statistics.stdev([x, x + 1]), 0.5)
            self.assertEqual(statistics.stdev([x, x + 1, x + 2]), 0.816496580927726)
            self.assertEqual(
                statistics.stdev([x, x + 1, x + 2, x + 3]), 1.118033988749895
            )

    def test_mixed_arrays(self):
        arr = [6, 2, 3, 1]
        self.assertEqual(statistics.stdev(arr), statistics.stdev(sorted(arr)))
        arr = np.random.uniform(-1, 0, 1000)
        self.assertEqual(
            round(statistics.stdev(arr), ROUND),
            round(statistics.stdev(sorted(arr)), ROUND),
        )

    def test_cmp_numpy(self):
        for _ in range(100):
            sample_data = np.random.uniform(-1, 0, 1000)
            numpy_res = np.std(sample_data)
            my_res = statistics.stdev(sample_data)
            self.assertEqual(round(numpy_res, ROUND), round(my_res, ROUND))


class TestLinearRegression(unittest.TestCase):
    def test_example(self):
        X = range(1, 8)
        Y = [1.5, 3.8, 6.7, 9, 11.2, 13.6, 16]
        l = statistics.linreg(X, Y)
        slope = l.slope
        y_int = l.y_intercept
        self.assertEqual(round(slope, 9), 2.414285714)
        self.assertEqual(round(y_int, 9), -0.828571429)

    def test_cmp_scipy(self):
        X = range(1, 8)
        Y = [1.5, 3.8, 6.7, 9, 11.2, 13.6, 16]

        l = statistics.linreg(X, Y)
        slope = l.slope
        y_int = l.y_intercept

        res_scipy = scipy.stats.linregress(X, Y)
        res_slope = res_scipy.slope
        res_yint = res_scipy.intercept

        self.assertEqual(round(slope, ROUND), round(res_slope, ROUND))
        self.assertEqual(round(y_int, ROUND), round(res_yint, ROUND))

    def test_cmp_scipy_no_y(self):
        Y = [1.5, 3.8, 6.7, 9, 11.2, 13.6, 16]

        with self.assertRaises(TypeError):
            l = statistics.linreg(Y)

    def test_random(self):
        for i in range(10, 1000):
            X = range(i)
            Y = np.random.uniform(-100, 100, i)

            l = statistics.linreg(X, Y)
            slope = l.slope
            y_int = l.y_intercept

            res_scipy = scipy.stats.linregress(X, Y)
            res_slope = res_scipy.slope
            res_yint = res_scipy.intercept

            self.assertEqual(round(slope, ROUND - 5), round(res_slope, ROUND - 5))
            self.assertEqual(round(y_int, ROUND - 5), round(res_yint, ROUND - 5))
