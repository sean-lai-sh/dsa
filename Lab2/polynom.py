import copy
import math


class Polynomial:
    def __init__(self, coefficients):
        # Get coefficents,
        if not isinstance(coefficients, list):
            self.coef = [0]
            self.rev_coef = [0]
        else:
            self.coef = coefficients  # ex: [1,2,3,4] 4x^3 + 3x^2 + 2x^2 + 1
            self.rev_coef = copy.copy(self.coef)  # ex: [4,3,2,1]
            self.rev_coef.reverse()

    def __add__(self, other):
        # Shallow copy each
        s_sh_copy = copy.copy(self.coef)
        o_sh_copy = copy.copy(other.coef)
        # reverse list
        # Above code works since we're working with immutable data
        # get shorter list len
        s_len = len(self.coef)
        o_len = len(other.coef)
        if s_len == o_len:
            for i in range(o_len):
                s_sh_copy[i] += o_sh_copy[i]
            return Polynomial(s_sh_copy)
        elif s_len > o_len:
            for i in range(o_len):
                s_sh_copy[i] += o_sh_copy[i]
            return Polynomial(s_sh_copy)
        else:
            for i in range(s_len):
                o_sh_copy[i] += s_sh_copy[i]
            return Polynomial(o_sh_copy)

    def __call__(self, param):
        f_sum = 0
        for i in range(len(self.coef)):
            f_sum += self.coef[i] * math.pow(param, i)
        return f_sum

    def __repr__(self):
        rev_len = len(self.rev_coef)
        # tip to self
        # DONT WRITE CODE LIKE THIS UNLESS U WANNA PISS UR FUTURE SELF OFF
        # Just write legible code ( THis was practice for list comphrension
        info = [(str(self.rev_coef[i]) + "x^" + str(rev_len - i - 1)) for i in range(rev_len - 1)]
        info.append(str(self.rev_coef[rev_len - 1]))
        return " + ".join(info)

    def derive(self):
        if len(self.coef) <= 1:
            return 0
        d_lst = copy.copy(self.coef)
        for i in range(1,len(d_lst)):
            d_lst[i] *= i
        d_lst.pop(0)
        self.coef = copy.copy(d_lst)
        d_lst.reverse()
        self.rev_coef = d_lst


    def __mul__(self,other):
        l_self = len(self.coef)
        l_oth = len(other.coef)
        results = [0] * (l_self+l_oth-1)
        for i in range(l_self):
            for j in range(l_oth):
                results[i+j] = results[i+j] + (self.rev_coef[i] * other.rev_coef[j])
                print(self.rev_coef[i] * other.rev_coef[j])
                print(i + j)
        results.reverse()
        return Polynomial(results)



poly1 = Polynomial([3, 7, 0, -9, 2]); # represents 2x4 - 9x3 + 7x + 3
poly2 = Polynomial([2, 0, 0, 5, 0, 0, 3]); # represents 3x6 + 5x 3 + 2
poly3 = poly1 + poly2
print(poly3.coef) # return [5, 7, 0, -4, 2, 0, 3]
print(poly1(1)) # return 3
print(poly2(1)) # return 10
print(poly3(1)) # return 13
poly3 = Polynomial([1,1]) * Polynomial([1,2])
print(poly3)
# Optional test values
poly1.derive() # returns none
print(poly1) # returns '8x^3 + -27x^2 + 7’
poly4 = poly1 * Polynomial([1, 2])
print(poly4) # return array of 8x3 -27x2 + 7 * (x + 2)
