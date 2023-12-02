from DoublyLinkedList import *

class CompactString:

    def __init__(self, orig_str):
        ''' Initializes a CompactString object
        representing the string given in orig_str'''
        self.data = DoublyLinkedList()
        if len(orig_str) == 0:
            self.data.add_first(('', 1))
            return
        counter = 0
        curr_char = orig_str[0]
        for i in range(len(orig_str)):
            if curr_char == orig_str[i]:
                counter += 1
            else:
                self.data.add_last((curr_char, counter))
                counter = 1
                curr_char = orig_str[i]
        self.data.add_last((curr_char, counter))
        # print(self.data)

    def __add__(self, other):
        """ Creates and returns a CompactString object that
        represent the concatenation of self and other,
        also of type CompactString"""
        new_cs = CompactString("")
        elem1 = None
        for elem in self:
            if elem.next != self.data.trailer:
                new_cs.data.add_last(elem.data)
            elif elem.data[0] != "":
                elem1 = elem.data
        counter = 0
        for elem in other:
            if counter == 0:
                if elem1 is not None and elem.data[0] == elem1[0]:
                    new_cs.data.add_last((elem.data[0], elem.data[1] + elem1[1]))
                    counter += 1
                else:
                    new_cs.data.add_last(elem1)
                    new_cs.data.add_last(elem.data)
                    counter += 1
            elif elem.data[0] != "":
                new_cs.data.add_last(elem.data)
        if new_cs.data.is_empty():
            new_cs.data.add_last(("", 1))
        return new_cs

    def __lt__(self, other):
        """ returns True if”f self is lexicographically
        less than other, also of type CompactString"""
        s_cursor = self.data.header.next
        o_cursor = other.data.header.next
        while s_cursor.data is not None:
            if o_cursor.data is None:
                return False
            if s_cursor.data[0] == o_cursor.data[0]:
                if s_cursor.data[1] != o_cursor.data[1]:
                    if not (s_cursor.next.data and o_cursor.next.data):
                        return s_cursor.data[1] < o_cursor.data[1]
                    else:
                        return s_cursor.data[1] > o_cursor.data[1]
            else:
                return s_cursor.data[0] < o_cursor.data[0]
            s_cursor = s_cursor.next
            o_cursor = o_cursor.next

        return o_cursor.data is not None



    def __le__(self, other):
        """ returns True if”f self is lexicographically
        less than or equal to other, also of type
        CompactString"""
        s_cursor = self.data.header.next
        o_cursor = other.data.header.next
        if len(self.data) != len(other.data):
            return self < other
        while s_cursor.data is not None and o_cursor is not None:
            if s_cursor.data != o_cursor.data:
                return self < other
            s_cursor = s_cursor.next
            o_cursor = o_cursor.next
        return True


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
        ptr = self.data.header.next
        while ptr != self.data.trailer:
            yield ptr
            ptr = ptr.next

    def __repr__(self):
        ''' Creates and returns the string representation
        (of type str) of self'''
        def p_repeat(ptr):
            return "".join(ptr.data[0] for i in range(ptr.data[1]))
        if self.data.is_empty():
            return ""
        return "".join([p_repeat(elem) for elem in self])

# s1 = CompactString('aaaaabbbaaac')
# s2 = CompactString('aaaaaaacccaaaa')
# print(s1 + s2)  # aaaaabbbaaacaaaaaaacccaaaa
# print(s2 + s1)   # aaaaaaacccaaaaaaaaabbbaaac
# print(s1 < s2) # False
# print(s2 < s1)   # Tru
# print(s1 <= s2) # False
# print(s2 <= s1) # True
# print(s1 > s2)  # True
# print(s2 > s1) # False
# print(s1 >= s2)  # True
# print(s2 >= s1)
