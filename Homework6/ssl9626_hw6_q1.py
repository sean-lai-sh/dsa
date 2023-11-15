from DoublyLinkedList import *


class LinkedQueue:
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, item):
        self.data.add_last(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Empty Linked Queue")
        return self.data.delete_first()

    def first(self):
        if self.is_empty():
            raise Exception("Empty Queue")
        return self.data.header.next.data

#
# print("CHANGE IMPORT STATEMENTS")
#
# ll = LinkedQueue()
# ll.enqueue(2)
# print(ll.top())