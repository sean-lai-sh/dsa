def sum_to_n(n):
    if n == 0:
        return 0
    return n + sum_to_n(n - 1)


def product_evens(n):
    if n == 2:
        return 2
    return n * product_evens(n - 2)


def find_max(lst):
    if not isinstance(lst, list):
        raise TypeError
    elif len(lst) == 1:
        return lst[0]
    return find_max_helper(lst, 0, len(lst) - 1)


def find_max_helper(lst, low, high):
    if low == high:
        return lst[low]
    # Get first Val
    cur = lst[low]
    other_max = find_max_helper(lst, low + 1, high)
    if cur > other_max:
        return cur
    return other_max


def is_palindrome(str):
    return is_palindrome_help(str, 0, len(str) - 1)


def is_palindrome_help(str, low, high):
    if low == high:
        return True
    elif str[low] != str[high]:
        return False
    return is_palindrome_help(str, low + 1, high - 1)


def binary_search(lst, low, high, val):
    if low > high:
        return None
    mid = (low + high) // 2
    if lst[mid] == val:
        return mid
    elif lst[mid] > val:
        return binary_search(lst, low, mid - 1, val)
    else:
        return binary_search(lst, mid + 1, high, val)


def vc_count(str, low, high):
    vowel = "aeiou"
    if low > high:
        return (0, 0)
    prev_tup = vc_count(str, low + 1, high)
    if str[low] in vowel:
        return (1 + prev_tup[0], prev_tup[1])
    else:
        return (prev_tup[0], 1 + prev_tup[1])


print(vc_count("care", 0, 3))


def sum_triangle(lst):
    if len(lst) == 1:
        return lst
    new_len = len(lst) - 1
    new_lst = []
    for i in range(new_len):
        new_lst.append(lst[i] + lst[i + 1])
    return sum_triangle(new_lst)


print(sum_triangle([1, 2, 3, 4, 5]))
