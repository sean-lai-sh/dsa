import math


def findChange(lst01):
    # Idea, utilize binary search, to find a 1 where the index -1 is a 0,
    # taking that index and returning it
    if not isinstance(lst01, list):
        raise TypeError("Invalid Input")
    lst_len = len(lst01)  # Get length
    curr_index = int(math.ceil(lst_len / 2))  # Start
    while 0 <= curr_index < lst_len:
        curr_val = lst01[curr_index]
        prev_val = lst01[curr_index - 1]
        isChange = curr_val == 1 and prev_val == 0
        if isChange:
            return curr_index
        if curr_val == 1:
            curr_index -= curr_index // 2
        else:
            curr_index += (lst_len - curr_index) // 2
    return 0


# lst = [1]
# print(findChange(lst))
