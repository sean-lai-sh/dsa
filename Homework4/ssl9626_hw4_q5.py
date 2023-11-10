
def count_lowercase(s, low, high):
    if low < 0 or high > len(s):
        raise IndexError("Invalid Range!!!!")
    if low <= high:
        if s[low].islower():
            return 1 + count_lowercase(s, low + 1, high)
        else:
            return 0 + count_lowercase(s, low + 1, high)
    return 0


def is_number_of_lowercase_even(s, low, high):
    if low == high:
        return not s[low].islower()
    prev = is_number_of_lowercase_even(s, low + 1, high)
    if prev is False and s[low].islower():
        return True
    elif prev is True and s[low].islower():
        return False
    else:
        return prev

# print(count_lowercase("abcde", 0,4))
# print(is_lowercase_even("abcDeF", 0 ,5))