def split_parity(lst):
    if not isinstance(lst, list):
        raise TypeError("Invalid Type")
    # Solution of sorted list
    i, j = 0, len(lst) - 1
    while i < j:  # At most n comparisons.
        left_val = lst[i]
        right_val = lst[j]
        is_left_even = left_val % 2 == 0
        is_right_even = right_val % 2 == 0
        if not is_right_even and is_left_even:
            # Swap
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
        elif is_right_even & is_left_even:
            # swap the next term
            j -= 1
        else:
            i += 1
    pass


# ### Behavior ###
# lst1 = [1,2,3,4,5,6,7,8,1,1,1,1,1,1,1,1,1,4,4,4,4,4,4,4]
# split_parity(lst1)
# print(lst1)

"""
final list => [3,1,2,4]
Odd even order DOES NOT MATTER
NO TEMP LIST
Run in O(n)
"""
