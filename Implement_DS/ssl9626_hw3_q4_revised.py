def remove_all(lst, value): # Now in O(n) time
    left = 0
    right = len(lst) - 1
    num_pop = 0
    while left < right:
        lVal = lst[left]
        rVal = lst[right]
        if lVal == value and rVal != value:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
            num_pop += 1
        elif lVal != value and rVal != value:
            left += 1
        elif lVal != value and rVal == value:
            left += 1
            right -= 1
            num_pop += 1
        else:
            right -= 1
            num_pop += 1
    t_ends = None
    if lst[left] == value:
        t_ends = len(lst) - left
    else:
        t_ends = len(lst) - right
    print(t_ends)
    for n in range(t_ends):
        lst.pop()
    return lst

t_lst = [1,2,3,1,1,5, 4, 1,1,1]
print(remove_all(t_lst, 1))