import ctypes


def make_array(n):
    return (n * ctypes.py_object)()


class ArrayList:
    def __init__(self, iterable=None):
        try:
            self.array = make_array(1)
            self.size = 0
            self.capacity = 1
            for i in iter(iterable):
                self.append(i)
        except TypeError as te:
            self.array = make_array(1)
            self.size = 0
            self.capacity = 1

    def __iadd__(self, other):
        temp_arrList = self + other
        self.array = temp_arrList.array
        self.size = temp_arrList.size
        self.capacity = temp_arrList.capacity
        return self

    def insert(self, index, val):
        if not isinstance(index, int):
            raise TypeError("Invalid indexing type, use integers")
        if index > self.size or index < -self.size:
            raise IndexError("Index out of bounds")
        if index < 0:
            index = self.size + index  # Format indicies
        if self.size == self.capacity:  # Do we need to change size?
            self.resize(2 * self.capacity)
        self.array[self.size] = val
        for i in range(self.size, index, -1):  # backwards swap
            self.array[i], self.array[i - 1] = self.array[i - 1], self.array[i]
        self.size += 1
        return 0

    def __len__(self):
        return self.size

    def __iter__(self):
        for k in range(self.size):
            yield self.array[k]

    def append(self, val):  # Amortized O(n)
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.size] = val
        self.size += 1

    def __rmul__(self, other):
        return self * other

    def __mul__(self, other):
        new_array = ArrayList()
        for i in range(0, other):
            for k in range(self.size):
                new_array.append(self.array[k])
        return new_array

    def remove(self, val):
        i = 0
        found_val = False
        while i < self.size and found_val is False:
            if self.array[i] == val:
                found_val = True
            else:
                i += 1
        if found_val:
            for k in range(i, self.size - 1):
                self.array[k], self.array[k + 1] = self.array[k + 1], self.array[k]
            self.array[self.size - 1] = ctypes.py_object
            self.size -= 1
            return 0
        else:
            return -1

    def remove_all(self, val):
        val_exists = 0
        while val_exists == 0:
            val_exists = self.remove(val)
        return 0

    def resize(self, new_size):  # O(n) - Worst Case
        self.capacity = new_size
        temp_arr = make_array(self.capacity)
        for i in range(self.size):
            temp_arr[i] = self.array[i]
        self.array = temp_arr

    def pop(self, index=None):
        if index is None:
            index = self.size - 1
        if index >= self.size or index < -self.size:
            raise IndexError("Invalid Index")
        elif not isinstance(index, int):
            raise TypeError("Invalid Type. Function supports integers only.")
        if index < 0:
            return self.array[self.size + index]
        if self.size * 4 == self.capacity:
            self.resize(self.capacity // 2)
        to_r = self.array[index]
        self.array[index] = None
        self.size -= 1
        return to_r

    def __getitem__(self, index):
        if index >= self.size or index < -self.size:
            raise IndexError("Invalid Index")
        elif not isinstance(index, int):
            raise TypeError("Invalid Type. Function supports integers only.")
        if index < 0:
            return self.array[self.size + index]
        return self.array[index]

    def __setitem__(self, key, value):
        if key >= self.size or key < -self.size:
            raise IndexError("Invalid Index")
        elif not isinstance(key, int):
            raise TypeError("Invalid Type. Function supports integers only.")
        if key < 0:
            self.array[self.size + key] = value
        self.array[key] = value

    def __add__(self, other):
        t_arr = ArrayList()
        for i in range(self.size):
            t_arr.append(self.array[i])
        for i in range(other.size):
            t_arr.append(other.array[i])
        return t_arr

    def __reversed__(self):
        l_pointer = 0
        r_pointer = self.size - 1
        while l_pointer < r_pointer:
            self.array[l_pointer], self.array[r_pointer] = (
                self.array[r_pointer],
                self.array[l_pointer],
            )
            l_pointer += 1
            r_pointer += 1
        pass

    def __repr__(self):
        return "[" + ", ".join(str(self.array[i]) for i in range(self.size)) + "]"


# ARRAY RESULTS IN NULL ERROR if value is not instantiated
#
# lst = ArrayList([1,2,3,4,5])
# print(lst.pop())
