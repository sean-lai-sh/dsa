class Vector:
    def __init__(self, d):
        if isinstance(d, int):
            self.coords = [0] * d
        elif isinstance(d, list):
            self.coords = d
        else:  # Edge case detection
            raise ValueError("Data type not supported")

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, j):
        return self.coords[j]

    def __setitem__(self, j, val):
        self.coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not (self == other)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Compatible with select types only : Vector")
        s_len = len(self)
        o_len = len(other)
        if s_len != o_len:
            raise ArithmeticError("Vectors must be of the same length")
        else:
            lst = [0] * s_len
            for i in range(len(lst)):
                lst[i] = self.coords[i] - other.coords[i]
            return Vector(lst)

    def __neg__(self):
        return Vector([x * -1 for x in self.coords])

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector([x * other for x in self.coords])
        elif isinstance(other, Vector):
            dp = 0
            for i in range(len(self)):
                dp += self.coords[i] * other.coords[i]
            return dp

    def __rmul__(self, other):
        if isinstance(other, int):
            return self * other
        elif isinstance(other, Vector):
            return other * self

    def __str__(self):
        return "<" + str(self.coords)[1:-1] + ">"

    def __repr__(self):
        return str(self)
