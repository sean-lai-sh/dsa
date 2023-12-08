from ArrayQueue import *


class ArrayDeque:
    INITIAL_CAPACITY = 4

    def __init__(self):
        self.data = make_array(self.INITIAL_CAPACITY)
        self.n = 0
        self.first_ind = None

        self.capacity = 2

    def __len__(self):
        return self.n

    def is_empty(self):
        return len(self) == 0

    def first(self):
        if self.is_empty():
            raise Exception("Empty Deque")
        return self.data[self.first_ind]

    def last(self):
        if self.is_empty():
            raise Exception("Empty Deque")
        return self.data[(self.first_ind + self.n) % self.capacity]

    def enqueue_first(self, elem):
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
        if self.is_empty():
            self.data[0] = elem
            self.first_ind = 0
            self.n += 1
        else:
            new_idx = self.first_ind - 1
            if new_idx < 0:
                new_idx = self.capacity + new_idx
            self.data[new_idx] = elem
            self.first_ind = new_idx
            self.n += 1

    def enqueue_last(self, elem):
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
        if self.is_empty():
            self.data[0] = elem
            self.front_ind = 0
            self.n += 1
        else:
            back_ind = (self.front_ind + self.n) % self.capacity
            self.data[back_ind] = elem
            self.n += 1

    def dequeue_first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % self.capacity
        self.n -= 1
        if self.is_empty():
            self.first = None
        if (self.n < self.capacity // 4) and (self.capacity > self.INITIAL_CAPACITY):
            self.resize(self.capacity // 2)
        return value

    def dequeue_last(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        index = (self.front_ind + self.n) % self.capacity
        value = self.data[index]
        self.data[index] = None
        self.n -= 1
        if self.is_empty():
            self.first_ind = None
        if (self.n < self.capacity // 4) and (self.capacity > self.INITIAL_CAPACITY):
            self.resize(self.capacity // 2)
        return value

    def resize(self, new_cap):
        new_data = make_array(new_cap)
        old_ind = self.first_ind
        for new_ind in range(self.n):
            new_data[new_ind] = self.data[old_ind]
            old_ind = (old_ind + 1) % self.capacity
        self.data = new_data
        self.capacity = new_cap
        self.first_ind = 0
