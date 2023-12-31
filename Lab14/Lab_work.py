from ChainingHashTableMap import *


def most_frequent(lst):
    if len(lst) == 0:
        return None
    HashMap = ChainingHashTableMap()
    for elem in lst:
        if elem in HashMap:
            HashMap[elem] += 1
        else:
            HashMap[elem] = 1

    max = 0
    key = None
    for elem in HashMap:
        count = HashMap[elem]
        if count > max:
            max = count
            key = elem
    return key


def first_unique(lst):
    if len(lst) == 0:
        return None
    HashMap = ChainingHashTableMap()
    for elem in lst:
        if elem in HashMap:
            HashMap[elem] += 1
        else:
            HashMap[elem] = 1
    for elem in lst:
        count = HashMap[elem]
        if count == 1:
            return elem
    return None


def two_sum(lst, target):
    map = ChainingHashTableMap()

    for index in range(len(lst)):
        value = lst[index]
        if target - value in map:
            return map[target - value], index
        else:
            map[value] = index

    return None, None


class MAD:
    def __init__(self, N):
        self.N = N
        self.p = 107
        self.a = 1
        self.b = 2

    def __call__(self, key):
        return ((self.a * hash(key) + self.b) % self.p) % self.N


map = MAD(14)
print(map(47))
print(map(51))
print(map(65))
print(map(104))
print(map(8))
print(map(5))
print(map(10))
print(map(7))
