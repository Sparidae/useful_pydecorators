import gc
import os
import sys
import time
import warnings
from functools import wraps


# 计算运算时间的装饰器
def cal_time_cost(function):
    @wraps(function)
    def func(*args, **kwargs):
        print("-" * 80)
        print(f"Running : {function.__name__:25}")
        t0 = time.perf_counter()
        result = function(*args, **kwargs)
        t1 = time.perf_counter()
        print(f"Ends    : {function.__name__:15} took {t1-t0:.4f}s")
        return result

    return func


# 屏蔽标准输出的装饰器
def block_stdout(func):
    def wrapper(*args, **kwargs):
        sys.stdout = open(os.devnull, "w")
        results = func(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return results

    return wrapper


# 屏蔽标准错误的装饰器
def block_stderr(func):
    def wrapper(*args, **kwargs):
        sys.stderr = open(os.devnull, "w")
        results = func(*args, **kwargs)
        sys.stderr = sys.__stderr__
        return results

    return wrapper
