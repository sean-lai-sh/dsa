def remove_all(lst, value):
    end = False
    checked_index = len(lst) - 1
    while checked_index > -1 and end is False:
        try:
            if l
            checked_index -= 1
        except ValueError:
            end = True


def my_remove(lst, value, starting_index):
    for i in range(starting_index, -1, -1):
        if lst[i] == value:
            lst.pop(i)
            return True

    raise ValueError("Not found")

# lst1 = [1,2,3,4,5,1,1,1,1,1,1,1,1]
# print(lst1)
# remove_all(lst1, 1)
# print(lst1)