from DoublyLinkedList import *

t_ll = DoublyLinkedList()
t_ll.add_last(3)
t_ll.add_last(7)
t_ll.add_last(4)
print(t_ll[0])
print(t_ll[2])
# t_ll.add_last(4)


def reverse_dll_by_data(dll: DoublyLinkedList):
    if dll.is_empty():
        return dll
    left = dll.header.next
    lInd = 0
    right = dll.trailer.prev
    rInd = len(dll) - 1
    while lInd < rInd:
        left.data, right.data = right.data, left.data
        left, right = left.next, right.prev
        lInd += 1
        rInd -= 1
    return dll

def fake_delete(dll, node):
    data = node.data
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    next_node.prev = prev_node
    dll.n -= 1
    return data

def reverse_dll_by_node(dll: DoublyLinkedList):
    if dll.is_empty() or len(dll) == 1:
        return dll
    left = dll.header.next
    lInd = 0
    right = dll.trailer.prev
    rInd = len(dll) - 1
    while lInd < rInd:
        next_values = (left.next, right.prev)
        if lInd != rInd - 1:
            fake_delete(dll, left)
            fake_delete(dll, right)
            dll.add_before(next_values[0], right)
            dll.add_after(next_values[1], left)
        else:
            fake_delete(dll, left)
            dll.add_after(right, left)
        left = next_values[0]
        right = next_values[1]
        lInd += 1
        rInd -= 1
    return dll


print(t_ll)
print(reverse_dll_by_data(t_ll))
print(reverse_dll_by_node(t_ll))

