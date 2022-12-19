#!/usr/bin/env python3

def mean(numbers: list[float]) -> float:
    return float(sum(numbers) / len(numbers))

def ema(data: list[float], period: int, smoothing: int = 2) -> float:
    ret = [sum(data[:period]) / period]
    for x in data[period:]:
        ret.append(
            (x * (smoothing / (1 + period)))
            + ret[-1] * (1 - (smoothing / (1 + period)))
        )
    return ret

if __name__ == "__main__":
    import numpy as np

    x = np.arange(-150, 150)
    ema_ = ema(x, 10)
    print(round(mean(ema_), 2))
