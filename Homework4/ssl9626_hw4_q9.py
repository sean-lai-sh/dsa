import copy


def permutations(lst, low, high):
    if low < 0 or high > len(lst):
        raise Exception("Invalid Range")
    if lst == []:
        return [lst]
    if not isinstance(lst, list):
        raise TypeError("Invalid Type")
    if low == high:
        return [[lst[low]]]
    prev_perms = permutations(lst, low + 1, high)
    new_perms = permute(lst[low], prev_perms, high - low)
    return new_perms


def permute(val, start_lst, n):
    init_len = len(start_lst)
    res_lst = copy.deepcopy(start_lst)
    for i in range(n):
        res_lst += copy.deepcopy(start_lst)
    k = -1
    for i in range(len(res_lst)):
        if i % init_len == 0:
            k += 1
        res_lst[i].insert(k,val)
    return res_lst
