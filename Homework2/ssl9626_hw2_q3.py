import math


def factors(num):
    if not isinstance(num, int):
        raise TypeError("Invalid Input")
    # Process from 0 -> Sqrt(num) since all factor pairs need to be there
    # from there
    fact_pairs = [0] * int(math.sqrt(num))
    curr_p = 0
    for i in range(1, int(math.sqrt(num) + 1)):  # Sqrt(num)
        if num % i == 0:
            fact_pairs[curr_p] = i
            curr_p += 1
            yield i
    for i in range(len(fact_pairs) - 1, -1, -1):  # Runs max Sqrt(n)
        if fact_pairs[i] != 0 and fact_pairs[i] != math.sqrt(num):
            yield int(num / fact_pairs[i])


#
# for k in factors(100):
#     print(k, end=", ")
