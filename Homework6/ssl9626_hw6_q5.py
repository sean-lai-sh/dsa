from DoublyLinkedList import *


def merge_linked_lists(srt_lnk_lst1: DoublyLinkedList, srt_lnk_lst2: DoublyLinkedList):
    def merge_sublists(ll1: DoublyLinkedList, ll1_cursor, ll2: DoublyLinkedList, ll2_cursor):
        if ll1.is_empty() and ll2.is_empty():
            return DoublyLinkedList()
        if ll1_cursor == ll1.trailer and ll2_cursor == ll2.trailer:
            return DoublyLinkedList()
        else:
            prev_dll = None
            if ll1_cursor == ll1.trailer:
                prev_dll = merge_sublists(ll1, ll1_cursor, ll2, ll2_cursor.next)
                prev_dll.add_first(ll2_cursor.data)
            elif ll2_cursor == ll2.trailer:
                prev_dll = merge_sublists(ll1, ll1_cursor.next, ll2, ll2_cursor)
                prev_dll.add_first(ll1_cursor.data)
            else:
                if ll1_cursor.data < ll2_cursor.data:
                    prev_dll = merge_sublists(ll1, ll1_cursor.next, ll2, ll2_cursor)
                    prev_dll.add_first(ll1_cursor.data)
                else:
                    prev_dll = merge_sublists(ll1, ll1_cursor, ll2, ll2_cursor.next)
                    prev_dll.add_first(ll2_cursor.data)
            return prev_dll

    return merge_sublists(srt_lnk_lst1, srt_lnk_lst1.header.next, srt_lnk_lst2, srt_lnk_lst2.header.next)

# li1 = DoublyLinkedList()
# for elem in [1 , 3 , 5 , 6 , 8]:
#     li1.add_last(elem)
#
# li2 = DoublyLinkedList()
# for elem in [2, 3, 5, 10,15,18]:
#     li2.add_last(elem)
#
# print(merge_linked_lists(li1,li2))