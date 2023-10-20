import math
def find_missing(lst):
    for i in range(len(lst) + 1):
        if i != lst[i]:
            return i
    return None


print(find_missing([0, 1, 2, 3, 4, 5, 7]))


def find_missing_unsort(lst):
    t_sum = len(lst) ** 2 + len(lst)
    return t_sum//2 - sum(lst)
    # lst_nums = [i for i in range(len(lst) + 2)]
    # for i in range(len(lst)):
    #     for k in range(len(lst_nums)):
    #         if lst[i] == lst_nums[k]:
    #             lst_nums[k] = None
    # return int(sum([i for i in range(len(lst_nums)) if isinstance(lst_nums[i], int)]))


print(find_missing_unsort([2, 3, 4, 1,0, 6]))
