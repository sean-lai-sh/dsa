from ArrayStack import *


class MaxStack:
    def __init__(self):
        self.data = ArrayStack()
        self.prev_max = None

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def top(self):
        if self.is_empty():
            raise Exception("Empty Stack")
        return self.data.top()[1]

    def push(self, e):
        if self.is_empty() or e > self.prev_max:
            self.data.push((e, e))
            self.prev_max = e
        else:
            self.data.push((self.prev_max, e))

    def pop(self):
        if self.is_empty():
            raise Exception("Empty Stack")
        return_values = self.data.pop()
        if self.is_empty():
            self.prev_max = None
        return return_values[1]

    def max(self):
        if self.is_empty():
            raise Exception("Empty Stack")
        return self.data.top()[0]


# maxS = MaxStack()
# maxS.push(3)
# maxS.push(1)
# maxS.push(6)
# maxS.push(4)
# print(maxS.max())
# print(maxS.pop())
# print(maxS.pop())
# print(maxS.max())
