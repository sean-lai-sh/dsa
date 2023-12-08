# This is a sample Python script.
import math


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def reverse_list(lst, low=None, high=None):
    i, j = 0, 0
    if high is None and low is None:
        i, j = 0, len(lst) - 1
    elif low <= -1 or high >= len(lst):
        raise AttributeError("Not valid inputs")
    else:
        i, j = low, high
    while i <= j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1

    # NO new list created
    # theta(n) runtime


def powers_of_two(n):
    itr = 0
    while itr < n:
        yield int(math.pow(2, itr))
        itr += 1


lst1 = [1, 2, 3, 4, 5, 6]
print(lst1)
reverse_list(lst1)
print(lst1)
lst2 = [1, 2, 3, 4, 5, 6]
print(lst2)
reverse_list(lst2, 1, 3)
print(lst2)

for n in powers_of_two(6):
    print(n, end=", ")
