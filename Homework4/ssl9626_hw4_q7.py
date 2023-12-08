def split_by_sign(lst, low, high):
    if (
        not isinstance(low, int)
        or not isinstance(high, int)
        or not isinstance(lst, list)
    ):
        raise TypeError("Invalid Inputs ")
    if low < 0 or high > len(lst):
        raise IndexError("Invalid range")
    if low <= high:
        low_val = lst[low]
        high_val = lst[high]
        if low_val >= 0 and high_val < 0:
            lst[low], lst[high] = lst[high], lst[low]
            return split_by_sign(lst, low + 1, high - 1)
        elif lst[low] >= 0 and high_val >= 0:
            return split_by_sign(lst, low, high - 1)
        elif lst[low] < 0 and high_val < 0:
            return split_by_sign(lst, low + 1, high)
        else:
            return split_by_sign(lst, low + 1, high - 1)
    else:
        return lst
