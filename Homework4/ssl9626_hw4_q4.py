def list_min(lst, low, high):
    if (
        not isinstance(lst, list)
        or not isinstance(low, int)
        or not isinstance(high, int)
    ):
        raise TypeError("Invalid input(s)")
    if low < 0 or high > len(lst):
        raise IndexError("Invalid Range")
    if low == high:
        return lst[low]
    prev_min = list_min(lst, low + 1, high)
    if prev_min > lst[low]:
        return lst[low]
    else:
        return prev_min
