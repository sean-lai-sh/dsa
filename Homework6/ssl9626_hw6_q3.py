from DoublyLinkedList import *

class CompactString:

    def __init__(self, orig_str):
        ''' Initializes a CompactString object
        representing the string given in orig_str'''
        self.data = DoublyLinkedList()
        if len(orig_str) == 0:
            pass
        counter = 0
        curr_char = orig_str[0]
        for i in range(len(orig_str)):
            if curr_char == orig_str[i]:
                counter += 1
            else:
                self.data.add_last((curr_char, counter))
                counter = 1
                curr_char = orig_str[i]
        self.data.add_last((curr_char,counter))

    def __add__(self, other):
        """ Creates and returns a CompactString object that
        represent the concatenation of self and other,
        also of type CompactString"""
        new_cs = CompactString("")
        for elem in self:
            new_cs.data.add_last(elem)
        for elem in other:
            new_cs.data.add_last(elem)

    def __lt__(self, other):
        """ returns True if”f self is lexicographically
        less than other, also of type CompactString"""
        s_cursor = self.data.header.next
        o_cursor = other.data.header.next
        while s_cursor != self.data.trailer and o_cursor != s_cursor:

    def __le__(self, other):
        """ returns True if”f self is lexicographically
        less than or equal to other, also of type
        CompactString"""

    def __gt__(self, other):
        ''' returns True if”f self is lexicographically
        greater than other, also of type CompactString'''
        return not self <= other
    def __ge__(self, other):
        ''' returns True if”f self is lexicographically
        greater than or equal to other, also of type
        CompactString'''
        return not self < other

    def __iter__(self):
        if self.data.is_empty():
            yield ""
        ptr = self.data.header.next
        while ptr != self.data.trailer:
            yield ptr.data
            ptr = ptr.next

    def __repr__(self):
        ''' Creates and returns the string representation
        (of type str) of self'''
        def p_repeat(ptr):
            return "".join(ptr.data[0] for i in range(ptr.data[1]))
        if self.data.is_empty():
            return ""
        return "".join([p_repeat(elem) for elem in self])


print(CompactString("aaaaaabbbbbccccc"))