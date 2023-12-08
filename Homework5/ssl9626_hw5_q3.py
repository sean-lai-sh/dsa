from ArrayStack import *
from ArrayDeque import *


class MidStack:
    def __init__(self):
        self.first_half = ArrayStack()
        self.second_half = ArrayDeque()

    def __len__(self):
        return len(self.first_half) + len(self.second_half)

    def is_empty(self):
        return len(self) == 0

    def top(self):
        if self.is_empty():
            raise Exception("Stack Empty")
        if self.second_half.is_empty():
            return self.first_half.top()
        return self.second_half.last()

    def push(self, e):
        if self.is_empty():
            self.second_half.enqueue_first(e)
        else:
            if len(self.second_half) == 2 * len(self.first_half):
                for i in range(len(self.second_half) // 2):
                    self.first_half.push(self.second_half.dequeue_first())
            self.second_half.enqueue_last(e)
            # Odd case:
            if len(self) % 2 == 1:
                f = self.second_half.dequeue_first()
                self.first_half.push(f)

    def mid_push(self, e):
        if self.is_empty():
            self.second_half.enqueue_first(e)
        else:
            if len(self.second_half) >= 2 * len(self.first_half):
                for i in range(len(self.second_half) // 2):
                    self.first_half.push(self.second_half.dequeue_first())
            self.second_half.enqueue_first(e)

    def pop(self):
        if self.is_empty():
            raise Exception("Empty MidStack")
        ret_val = None
        if not self.second_half.is_empty():
            ret_val = self.second_half.dequeue_last()
        else:
            ret_val = self.first_half.pop()
        if len(self.second_half) == len(self) // 4:
            for i in range(len(self.first_half) // 4):
                self.second_half.enqueue_first(self.first_half.pop())
        return ret_val


# midS = MidStack()
# midS.push(2)
# midS.push(4)
# midS.push(6)
# midS.push(8)
# midS.mid_push(10)
# midS.mid_push(15)
#
# while not midS.is_empty():
#     print(midS.pop())
