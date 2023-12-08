import sys
from LinkedBinaryTree import *


def min_and_max(bin_tree):
    if not isinstance(bin_tree, LinkedBinaryTree):
        raise TypeError("Invalid input")
    if bin_tree.is_empty():
        raise Exception("Empty Tree")

    def subtree_min_and_max(root):
        if root is None:
            return None
        lSide = subtree_min_and_max(root.left)
        rSide = subtree_min_and_max(root.right)
        if lSide is None and rSide is None:
            return (root.data, root.data)
        else:
            data = root.data
            t_min, t_max = sys.maxsize, -sys.maxsize
            if rSide is not None:
                if rSide[0] < t_min:  # Our data is the new min
                    t_min = rSide[1]
                if rSide[1] > t_max:  # Data is new max
                    t_max = rSide[1]
            if lSide is not None:
                if lSide[0] < t_min:  # Our data is the new min
                    t_min = lSide[0]
                if lSide[1] > t_max:  # Data is new max
                    t_max = lSide[1]
            if data < t_min:
                t_min = data
            if data > t_max:
                t_max = data
            return (t_min, t_max)

    return subtree_min_and_max(bin_tree.root)
