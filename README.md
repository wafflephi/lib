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
from wafflephi.statistics import stdev

data = [1.5, 3.8, 6.7, 9, 11.2, 13.6, 16]
stdev(data) # 4.83106444517866
```

### Least squares linear regression

```python
from wafflephi.statistics import LinearRegression

data = [1.5, 3.8, 6.7, 9, 11.2, 13.6, 16]
est, slope, y_intercept = LinearRegression.lstsq(data)

print(est, slope, y_intercept, end='\n')

[-0.032370892429303244, 0.9193088613350588, 2.1192528986901245, 3.070932652454486, 3.981235025620397, 4.97429215998321, 5.967349294346023]
0.41377380598450525
-0.6530316014060611
```
