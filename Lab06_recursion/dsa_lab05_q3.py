def fib(n):
    if not isinstance(n, int):
        raise TypeError("Use Integers")
    elif n < 0:
        raise ValueError("There is no negative sequence of fibonacci numbers")
    return fib_help(n, [])


def fib_help(n, calc_vals):
    if n <= 1:

        return n
    else:
        return fib(n-1) + fib(n-2)


for i in range(0, 17):
    print(fib(i), end=", ")
