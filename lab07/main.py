def SortLst(lst):
    """
    O(n) run time (Possible if only from 0 -> n-1)
    :param lst:
    :return:
    """
    for i in range(len(lst)):
        lst[i] = i


def intersectionoflst(lst1, lst2):
    """
    : lst1 type: list[int]
    : lst2 type: list[int]
    : return type: list[int]
    """
    re_lst = []
    p1 = 0
    p2 = 0
    while p2 < len(lst2) and p1 < len(lst1):
        if lst1[p1] == lst2[p2]:
            re_lst.append(lst1[p1])
            p1 += 1
            p2 += 1
        elif lst1[p1] > lst2[p2]:
            p2 += 1
        else:
            p1 += 1
    return re_lst


def is_pow_two(n):
    if n == 1:
        return True
    if n % 2 == 1:
        return False
    return is_pow_two(n / 2)


def split_parity(lst, low, high):
    if high >= len(lst) or low < 0:
        raise IndexError("invalid indices")
    if low >= high:
        return lst
    if lst[low] % 2 == 1 and lst[high] % 2 == 0:
        lst[low], lst[high] = lst[high], lst[low]
        return split_parity(lst, low + 1, high - 1)
    elif lst[low] % 2 == 0 and lst[high] % 2 == 1:
        return split_parity(lst, low + 1, high - 1)
    elif lst[low] % 2 == 0 and lst[high] % 2 == 0:
        return split_parity(lst, low, high - 1)
    else:
        return split_parity(lst, low + 1, high)


def nested_sum(lst):
    # Define helper
    return get_sum(lst, 0, len(lst) - 1)


def get_sum(lst, low, high):
    if low > high:
        return 0
    if isinstance(lst[low], list):
        return get_sum(lst[low], 0, len(lst[low]) - 1) + get_sum(lst, low + 1, high)
    else:
        return lst[low] + get_sum(lst, low + 1, high)


def nested_depth_level(lst):
    return get_depth(lst, 0, len(lst) - 1)


def get_depth(lst, low, high):
    if low > high:
        return 1
    if isinstance(lst[low], list):
        return get_depth(lst[low], 0, len(lst[low]) - 1) + get_depth(lst, low + 1, high)
    else:
        return get_depth(lst, low + 1, high)


def deep_reverse(lst, low, high):
    if low > high:
        return None
    # RECUR CASE:
    # Reverse a smaller sub array.
    if isinstance(lst[low], list):
        # reverse first
        deep_reverse(lst[low], 0, len(lst[low]) - 1)
    if isinstance(lst[high], list):
        deep_reverse(lst[high], 0, len(lst[high]) - 1)
    lst[low], lst[high] = lst[high], lst[low]
    return deep_reverse(lst, low + 1, high - 1)


def yield_flattened(lst):
    yield from flattened_helper(lst, 0, len(lst) - 1)


def flattened_helper(lst, low, high):
    if low <= high: # Don't yield if low > high
        if isinstance(lst[low], list):
            yield from flattened_helper(lst[low], 0, len(lst[low]) - 1)
        else:
            yield lst[low]
        yield from flattened_helper(lst, low + 1, high)


def print_flattened(lst): # provided by lab07
    print("[" + ", ".join(str(num) for num in yield_flattened(lst)) + "]")


lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 3, 4, 5]
to_sort = [1, 4, 5, 2, 3, 6, 8, 7]
nest_lst = [[1, 2], 3, [4, [5, 6, [7], 8]], [[[[9]]]]]
SortLst(to_sort)
print("SortLst= ", to_sort)
print("intersection of lst = ", intersectionoflst(lst1, lst2))
print("is pow two = ", is_pow_two(16))
print("is pow two = ", is_pow_two(15))
print("split parity=", split_parity([1, 2, 3, 4, 5, 6, 7, 8], 0, 7))
print("nested_sum= ", nested_sum([[1, 2], 3, [4, [5, 6, [7], 8]]]))
print("nested depth array = ", [[[[[1]]]]])
print("nested depth level =", nested_depth_level([[[[[1]]]]]))
print("nested array for testing methods below = " , nest_lst)
print("print flattened =", end=" ")
print_flattened(nest_lst)
print("prior to deep reverse= ", nest_lst)
deep_reverse(nest_lst, 0, len(nest_lst) - 1)
print("deep reverse=", nest_lst)
