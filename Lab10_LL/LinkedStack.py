from DS_packages import *

class LinkedStack:

    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        self.data.add_last(e)

    def pop(self):
        if self.is_empty():
            raise Exception("empty stack")
        return self.data.delete_last()
