import math


def two_sum(srt_lst, target):
    if not isinstance(target, int) or not isinstance(srt_lst, list):
        raise TypeError("Wrong Type!!")
    numsIndex = {}
    for i in range(len(srt_lst)):
        if target - srt_lst[i] in numsIndex:
            return (numsIndex[target - srt_lst[i]], i)
        numsIndex[srt_lst[i]] = i
    return None



# srt_lst1 = [-2, 7, 11, 15, 20, 21]
# print(two_sum(srt_lst1, 22))
# lst1 = [1, 2, 3, 4, 5]
# print(two_sum(lst1, 7))
# print(two_sum(lst1, 3))
# print(two_sum(lst1, 2))
