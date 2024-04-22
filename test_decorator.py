import time

import decorator


@decorator.block_stdout
def test_bso():
    print("this is a decorator test")


@decorator.cal_time_cost
def test_timecost():
    test_bso()
    time.sleep(5)


if __name__ == "__main__":
    test_timecost()
