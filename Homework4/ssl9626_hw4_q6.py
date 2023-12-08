def appearances(s, low, high):
    if low < 0 or high >= len(s):
        raise IndexError("Invalid Range")
    if low == high:
        key = s[low]
        return {key: 1}
    prev_dict = appearances(s, low + 1, high)
    if s[low] in prev_dict:
        prev_dict.update({s[low]: prev_dict.get(s[low]) + 1})
    else:
        prev_dict.update({s[low]: 1})
    return prev_dict
