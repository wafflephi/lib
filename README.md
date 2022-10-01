# wafflephi library

## Install as a package

```
git clone https://github.com/wafflephi/lib
cd lib/
pip3 install -e .
```

## Examples

### Standard deviation

```python
>>> from wafflephi.statistics import stdev
>>> data = [1.5, 3.8, 6.7, 9, 11.2, 13.6, 16]
>>> stdev(data)
4.83106444517866
```

### Least squares linear regression

```python
>>> from wafflephi.statistics import linreg, fit
>>> data = [1.5, 3.8, 6.7, 9, 11.2, 13.6, 16]
>>> x = range(len(data))
>>> linreg(x, data)
LinearRegression(slope=2.4142857142857133, y_intercept=1.585714285714289)
>>> l = linreg(x, data)
>>> fit(l, data)
[1.585714285714289, 4.000000000000002, 6.4142857142857155, 8.82857142857143, 11.242857142857142, 13.657142857142855, 16.07142857142857]
```
