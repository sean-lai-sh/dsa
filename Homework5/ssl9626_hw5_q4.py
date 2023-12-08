from ArrayStack import *


class Queue:
    def __init__(self):
        self.back_view = ArrayStack()
        self.front_view = ArrayStack()

    def __len__(self):
        if self.back_view.is_empty():
            return len(self.front_view)
        else:
            return len(self.back_view)

    def enqueue(self, e):
        self.back_view.push(e)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Empty Queue")
        if self.front_view.is_empty():  # Reverse as needed
            while not self.back_view.is_empty():  # O(N) run only after n enqeues
                self.front_view.push(self.back_view.pop())

        return self.front_view.pop()

    def first(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        if self.front_view.is_empty():
            while not self.back_view.is_empty():
                self.front_view.push(self.back_view.pop())
        return self.front_view.top()

    def is_empty(self):
        return len(self) == 0
