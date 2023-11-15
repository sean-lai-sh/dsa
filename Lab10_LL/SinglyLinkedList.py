class SinglyLinkedList:
    class Node:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

        def disconnect(self):
            self.data = None
            self.next = None

    def __init__(self):
        self.header = SinglyLinkedList.Node()
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return len(self) == 0

    def add_first(self, val):
        if self.is_empty():
            self.header.next = SinglyLinkedList.Node(val)
            self.n += 1
        else:
            ptr = self.header.next
            self.header.next = SinglyLinkedList.Node(val)
            self.header.next.next = ptr
            self.n += 1
        return True

    def add_after(self, node, val):
        if self.is_empty() and node != self.header:
            raise Exception("cannot refernce a node in empty list ")
        ptr = node.next
        node.next = SinglyLinkedList.Node(val)
        node.next.next = ptr
        self.n += 1
        return True

    def add_before(self, node, val):
        if self.is_empty():
            self.add_first(val)
            return
        cursor = self.header.next
        prev = self.header
        found_node = False
        while cursor.next is not None and not found_node:
            if cursor == node:
                found_node = True
                continue
            else:
                prev = cursor
                cursor = cursor.next
        if not found_node:
            raise Exception("Node does not exist")
        else:
            prev.next = SinglyLinkedList.Node(val)
            prev.next.next = cursor

    def add_last(self, val):
        if self.is_empty():
            self.header.next = SinglyLinkedList.Node(val)
            self.n += 1
        else:
            cursor = self.header.next
            while cursor.next is not None:
                cursor = cursor.next
            cursor.next = SinglyLinkedList.Node(val)
            self.n += 1
    def delete_first(self):
        if self.is_empty():
            raise Exception()
        if len(self) == 1:
            re_data = self.header.next.data
            self.header.next.disconnect()
            self.header.next = None
            self.n -= 1
            return re_data
        newhead = self.header.next.next
        re_data = self.header.next.data
        self.header.next.disconnect()
        self.header.next = newhead
        self.n -= 1
        return re_data

    def delete_last(self):
        if len(self) <= 1:
            return self.delete_first()
        cursor = self.header.next
        prev = self.header
        while cursor.next is not None:
            prev = cursor
            cursor = cursor.next

        prev.next = None
        re_data = cursor.data
        cursor.disconnect()
        return re_data

    def delete_node(self, node):
        if self.is_empty():
            raise Exception()
        else:
            prev_node = None
            for elem in self:
                if elem.next == node:
                    prev_node = elem
            if prev_node == None:
                raise Exception()
            else:
                to_return = prev_node.next
                prev_node.next = prev_node.next.next
                return to_return

    def __repr__(self):
        return "[" + " -> ".join([str(elem) for elem in self]) + "]"
    def __iter__(self):
        cursor = self.header.next
        while cursor is not None:
            yield cursor.data
            cursor = cursor.next