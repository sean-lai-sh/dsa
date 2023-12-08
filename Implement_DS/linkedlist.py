class LinkedList:
    # Nesting of the Node makes it a pseudo name of linked list node
    class Node:
        def __init__(self, e=None):
            self.data = e
            self.next = None

        def set_item(self, e):
            self.data = e

        def set_next(self, t):
            self.next = t

        def get_item(self):
            return self.data

        def next(self):
            return self.next

        def __repr__(self):
            return str(self.data)

    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0  # num items

    def __len__(self):
        return self.n

    def is_empty(self):
        return len(self) == 0

    def add_first(self, e):  # O(n) w.c if not at the start
        if self.is_empty():
            new_node = LinkedList.Node(e)
            self.head = new_node
            self.tail = self.tail
            self.n += 1
        else:
            new_node = LinkedList.Node(e)
            new_node.set_next(self.head)
            self.head = new_node
            self.n += 1

    def add_last(self, e):
        if self.is_empty():
            new_node = LinkedList.Node(e)
            self.tail = new_node
            self.head = self.tail
            self.n += 1
        else:
            new_node = LinkedList.Node(e)
            self.tail.set_next(new_node)
            self.tail = new_node
            self.n += 1

    def remove_first(self):
        if self.is_empty():
            raise Exception("Empty LL")
        new_head = self.head.next()
        to_re = self.head
        self.head = new_head
        return to_re

    def head(self):
        return self.head


ll = LinkedList()
ll.add_first(1)
ll.add_first(2)
ll.add_first(3)

print(ll.head)
print(ll.remove_first())
