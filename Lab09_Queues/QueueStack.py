from ArrayQueue import *

class QueueStack:
    def __init__(self):
        self.data = ArrayQueue()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, e):
        # Optimized version for push only
        self.data.enqueue(e)
        # pop will have O(n)

    def pop(self):
        if self.is_empty():
            raise Exception("Empty Stack")

        return self.data.dequeue()
        # This optimizes pop() but push will have a O(n) run time to reorder each time to
        # allow first to be the last index just inserted

    def top(self):
        # Optimized pop will make Top run in O(1) Amortized
        # unoptimized runs in O(n) to find the last one and maintain order
        pass
