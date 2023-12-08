from ArrayQueue import *


def flatten_list_by_depth(lst):
    q = ArrayQueue()
    n_lst = []
    for i in range(len(lst)):
        q.enqueue(lst[i])
    while not q.is_empty():
        if isinstance(q.first(), list):
            for elem in q.first():
                q.enqueue(elem)
            q.dequeue()
        else:
            n_lst.append(q.dequeue())
    return n_lst


def n_bonnaci(n, k):
    Store_val = StaticArrayQueue(n)
    num_itr = 0
    while num_itr < k:
        if num_itr < n:
            Store_val.enqueue(1)
            num_itr += 1
            yield 1
        else:
            new_val = 0
            new_val += Store_val.dequeue()
            for i in range(n - 1):
                t_val = Store_val.dequeue()
                new_val += t_val
                Store_val.enqueue(t_val)
            Store_val.enqueue(new_val)
            num_itr += 1
            yield new_val


lst = [[[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]
new_lst = flatten_list_by_depth(lst)
print(new_lst)


for i in n_bonnaci(4, 2):
    print(i, end=", ")
