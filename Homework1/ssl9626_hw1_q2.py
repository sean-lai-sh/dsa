import copy


def shift(lst, k, direction='left'):  # O(N) run time
    if not isinstance(k, int) or k <= 0:  # edge case for not an int or is 0
        return lst
    if not isinstance(lst, list) or not bool(lst):  # edge case not a list or empty
        return []
    # now past edge case checking, now we can do swapping
    temp_lst = copy.copy(lst)  # shallow copy since we're working with integers
    len_lst = len(lst)
    if direction == 'left':
        # if statement is moved out to remove having it run
        # n times inside the loop since it doesn't change
        for i in range(len_lst):
            shift_val = i + k
            if shift_val >= len_lst:
                shift_val -= len_lst
            lst[i] = temp_lst[shift_val]
    elif direction == 'right':
        for i in range(len_lst):
            shift_val = i - k
            if shift_val < 0:
                shift_val += len_lst
            lst[i] = temp_lst[shift_val]
    return lst
