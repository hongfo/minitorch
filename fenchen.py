import math
from typing import Optional
import minitorch
import matplotlib.pyplot as plt
import cv2 as cv

from minitorch.scalar import ScalarHistory


def work(f, *vals, arg: int = 0, epsilon: float = 1e-6):
    po = [i for i in vals]
    po[arg] += epsilon
    m = f(*po)
    print(m)
    po[arg] -= 2 * epsilon
    n = f(*po)
    print(n)
    return (m - n) / (2 * epsilon)


def is_close(x: float, y: float) -> float:
    "$f(x) = |x - y| < 1e-2$"
    # TODO: Implement for Task 0.1.
    return float(abs(x - y) < 1e-2)


def f(*x):
    sum = 0
    for a, b in enumerate(x):
        sum += b ** (a + 1)
    return sum


def f(*x):
    sum = 0
    for i in x:
        for j in x:
            sum += i * j
    return sum


def wrap_tuple(x):  # type: ignore
    "Turn a possible value into a tuple"
    if isinstance(x, tuple):
        return x
    return (x,)










































"""
我就是这么一天天老下去了，从这个样子你决看不出我每天每夜每小时每一分钟都在想入非非，怀念着十七岁时见到的紫色天空，岸边长满绿色芦苇的河流，还有我的马兄弟。我本来不是这样的，我是装成这样的。
"""