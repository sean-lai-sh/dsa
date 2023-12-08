import math


def max_sub_array(lst, k=1):
    if not isinstance(k, int):
        raise TypeError("Wrong Type")
    left_window = 0
    right_window = len(lst) // k
    # print(right_window)
    lst_len = len(lst)
    # t_sum = sum(lst[left_window:right_window])
    t_sum = sum([lst[i] for i in range(right_window)])
    max_sum = t_sum
    while right_window < lst_len:
        print("This is " + str(left_window) + " " + str(right_window))
        t_sum += lst[right_window] - lst[left_window]
        if t_sum > max_sum:
            max_sum = t_sum
        left_window += 1
        right_window += 1
    return max_sum


nums = [1, 12, -5, -6, 50, 3]
print(max_sub_array(nums, 2))
