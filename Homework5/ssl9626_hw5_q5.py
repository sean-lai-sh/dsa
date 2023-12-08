from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack


def permutations(lst):
    if len(lst) == 0:
        return []
    elif not isinstance(lst, list):
        raise TypeError("Invalid Input")
    re_lst = []  # Does not count for O(1) Space
    stack = ArrayStack()
    queue = ArrayQueue()
    perm_itr = 1
    for k in range(1, len(lst) + 1):
        perm_itr *= k
        stack.push(lst[k - 1])
    while not stack.is_empty():
        insert_val = stack.pop()
        s_len = len(queue)
        if queue.is_empty():
            queue.enqueue([insert_val])
            continue
        for n in range(s_len):  # Iterate stuff
            if queue.is_empty():
                queue.enqueue([insert_val])
            else:
                pop_val = queue.dequeue()
                for k in range(len(pop_val) + 1):
                    new_perm = pop_val[:]
                    new_perm.insert(k, insert_val)
                    queue.enqueue(new_perm)
        print(len(queue))
    while not queue.is_empty():
        re_lst.append(queue.dequeue())
    return re_lst


# print(permutations([1]))
# print(permutations([1,2]))
# print(permutations([1,2,3]))
# # print(permutations([1,2,3,4]))
