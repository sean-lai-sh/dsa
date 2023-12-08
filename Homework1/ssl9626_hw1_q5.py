def fibs(n):
    itr = 1
    if n == 0:
        yield 1
    f_n, s_n = 0, 1
    # first sum
    while itr <= n:
        yield s_n
        f_n, s_n = s_n, (f_n + s_n)
        itr += 1
