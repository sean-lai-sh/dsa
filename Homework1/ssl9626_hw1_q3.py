import math


def get_squares(n):
    if n <= 0 or not isinstance(n, int):
        return 0
    elif n == 1:
        return 1
    temp = 1
    f_sum = 0
    while temp * temp < n:
        f_sum += temp * temp
        temp += 1
    return f_sum


def get_squares_odd(n):
    if n <= 0 or not isinstance(n, int):
        return 0
    elif n == 1:
        return 1
    temp = 1
    f_sum = 0
    while temp * temp < n:
        f_sum += temp * temp
        temp += 2
    return f_sum


sum([i * i for i in range(int(math.ceil(math.sqrt(16))))])
sum([i * i for i in range(1, int(math.ceil(math.sqrt(16))), 2)])

