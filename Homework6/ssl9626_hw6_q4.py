from DoublyLinkedList import *


def deep_copy_linked_list(lnk_lst):
    if lnk_lst.is_empty():
        return DoublyLinkedList()
    to_re = DoublyLinkedList()
    ptr = lnk_lst.header.next
    while ptr != lnk_lst.trailer:
        data = ptr.data
        if isinstance(data, DoublyLinkedList):
            data = deep_copy_linked_list(data)
        to_re.add_last(data)
        ptr = ptr.next
    return to_re


def copy_linked_list(lnk_lst):
    if lnk_lst.is_empty():
        return DoublyLinkedList()
    to_re = DoublyLinkedList()
    ptr = lnk_lst.header.next
    while ptr != lnk_lst.trailer:
        data = ptr.data
        to_re.add_last(data)
        ptr = ptr.next
    return to_re


ll_test = DoublyLinkedList()
e1 = DoublyLinkedList()
e1.add_last(1)
e1.add_last(2)
ll_test.add_last(e1)
ll_test.add_last(3)
print("Before Copy", ll_test)
copyT = copy_linked_list(ll_test)
print("After Copy", copyT)

e1.header.next.data = 10

print("After value change", e1)
print(ll_test)
print(copyT)
