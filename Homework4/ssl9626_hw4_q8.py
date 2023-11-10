def flat_list(nested_lst, low, high):
    if not isinstance(nested_lst, list):
        raise TypeError("Invalid type")
    if low < 0 or high >= len(nested_lst):
        raise IndexError("Invalid Range")
    if low > high:
        return []
    prev_lst = flat_list(nested_lst, low + 1, high)
    if isinstance(nested_lst[low], list):
        prev_lst = flat_list(nested_lst[low], 0, len(nested_lst[low]) - 1) + prev_lst
    else:
        prev_lst.insert(0, nested_lst[low])
    return prev_lst


nest_lst = [[1, 2], 3, [4, [5, 6, [7], 8]], [[[[9]]]]]
print(flat_list(nest_lst,0,len(nest_lst)-1))