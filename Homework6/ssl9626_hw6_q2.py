from DoublyLinkedList import DoublyLinkedList


class Integer:
    ASCII_CONST = 48
    def __init__(self, num_str):
        self.data = DoublyLinkedList()
        got_int = False
        if num_str == "0":
            self.data.add_last(num_str)
        for i in range(len(num_str)):
            if num_str[i] != "0":
                self.data.add_last(num_str[i])
                got_int = True
            elif got_int and num_str[i] == "0":
                self.data.add_last(num_str[i])


    def __add__(self, other):
        lower_len = None
        longer_lst = None
        short_lst = None
        if len(self.data) > len(other.data):
            lower_len = len(other.data)
            longer_lst = self
            short_lst = other
        else:
            lower_len = len(self.data)
            longer_lst = other
            short_lst = self
        temp = "0"
        to_re = Integer("")
        t_range = len(longer_lst.data) - lower_len
        s_cursor = short_lst.data.trailer.prev
        o_cursor = longer_lst.data.trailer.prev
        for i in range(lower_len):
            s_digit = s_cursor.data
            o_digit = o_cursor.data
            t_sum = int(s_digit) + int(o_digit) + int(temp)
            s_cursor = s_cursor.prev
            o_cursor = o_cursor.prev
            if t_sum < 10:
                to_re.data.add_first(str(t_sum))
                temp = "0"
            else:
                t_sum = str(t_sum)
                temp = t_sum[0]
                to_re.data.add_first(t_sum[1])
        for k in range(t_range):
            digit = o_cursor.data
            t_sum = int(digit) + int(temp)
            o_cursor = o_cursor.prev
            if t_sum < 10:
                to_re.data.add_first(str(t_sum))
                temp = "0"
            else:
                t_sum = str(t_sum)
                temp = t_sum[0]
                to_re.data.add_first(t_sum[1])
        if temp != "0":
            to_re.data.add_first(temp)
        return to_re




    def __mul__(self, other):
        lower_len = None
        longer_lst = None
        short_lst = None
        if len(self.data) > len(other.data):
            lower_len = len(other.data)
            longer_lst = self
            short_lst = other
        else:
            lower_len = len(self.data)
            longer_lst = other
            short_lst = self
        to_re = Integer("")
        t_range = len(longer_lst.data)
        s_cursor = short_lst.data.trailer.prev
        o_cursor = longer_lst.data.trailer.prev
        c = 0
        if s_cursor.data == "0" or o_cursor.data == "0":
            return Integer("0")
        for i in range(lower_len):
            digit = s_cursor.data
            if i > 0:
                c += 1
            t_int = Integer("")
            for k in range(c):
                t_int.data.add_first("0")
            temp = "0"
            s_cursor = s_cursor.prev
            for k in range(t_range):
                l_digit = o_cursor.data
                # print("l_digit:", l_digit)
                # print("s_digit", digit)
                # print("temp:", temp)
                t_sum = int(digit) * int(l_digit) + int(temp)
                o_cursor = o_cursor.prev
                if t_sum < 10:
                    t_int.data.add_first(str(t_sum))
                    temp = "0"
                else:
                    t_sum = str(t_sum)
                    l_sum = len(t_sum)
                    temp = t_sum[0:l_sum-1]
                    t_int.data.add_first(t_sum[l_sum-1])
            if temp != "0":
                t_int.data.add_first(temp)
            # print("Temp Int:", t_int)
            if to_re.data.trailer.prev == to_re.data.header:
                to_re = t_int
            elif t_int.data.header.next != "0":
                to_re = to_re + t_int
            o_cursor = longer_lst.data.trailer.prev
        return to_re

    def __repr__(self):
        re_val = "".join([elem for elem in self.data])
        return re_val

# # #
# i1 = Integer("13")
# i2 = Integer("11")
# print(i1 * i2)
# print(Integer("007"))
