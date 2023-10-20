def e_approx(n):
    if not isinstance(n, int):
        raise TypeError("Invalid Value")
    curr_fact = 1
    curr_approx = 1
    for i in range(1, n + 1):
        curr_fact *= i
        temp_factorial = 1 / curr_fact
        curr_approx += temp_factorial
    return curr_approx
