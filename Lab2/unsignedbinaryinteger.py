import copy
import math


class Unsignedbinaryinteger:
    def __init__(self, num_str):
        self.str_val = num_str

    # < > = Op
    def __lt__(self, other):
        return self.decimal() < other.decimal()

    def __gt__(self, other):
        # return len(self.str_val) > len(other.str_val)
        return other < self

    def __eq__(self, other):
        return self.str_val == other.str_val

    # + op
    def __add__(self, other):
        num1 = int(self.str_val)
        num2 = int(other.str_val)
        f_sum = num1 + num2
        # final = self.recur(f_sum)
        final = ""
        still_Comp = True
        while still_Comp:
            temp = f_sum % 10
            if temp == 1:
                f_sum = f_sum / 10
                final += "1"
            elif temp == 2:
                f_sum = (f_sum / 10) + 1
                final += "1"
            else:
                final += "10"
                still_Comp = False
        return final

    def decimal(self):
        str_rev = self.str_val[::-1]  # Reverses string by slicing and going backwards
        f_sum = 0
        for i in range(len(str_rev)):
            f_sum += int(str_rev[i] * int(math.pow(2, i)))
        return f_sum

    def recur(self, amt):
        temp = amt % 10
        if temp == 1:
            return self.recur(amt / 10) + "1"
        elif temp == 2:
            return self.recur(amt / 10 + 1) + "0"
        else:
            return "10"

    def is_twos_power(self):
        return self.largest_twos_power() == self.str_val

    def largest_twos_power(self):
        if self.str_val[0] == "0":
            return 0
        else:
            s_len = len(self.str_val)
            largest_pow = "1" + "0" * (s_len - 1)
            return largest_pow

    def __repr__(self):
        return "0b" + self.str_val


USB1 = Unsignedbinaryinteger("100")
USB2 = Unsignedbinaryinteger("110")
print(USB1.largest_twos_power())
print(USB1.is_twos_power())
print(USB2.largest_twos_power())
print(USB2.is_twos_power())
