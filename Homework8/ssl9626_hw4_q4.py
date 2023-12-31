import math
from BinarySearchTreeMap import *
import sys

def find_min_abs_difference(bst):
    inorder = [elem for elem in bst]
    mini = float("inf")
    N = len(inorder)

    for i in range(N - 1):
        mini = abs(min(mini, inorder[i + 1] - inorder[i]))

    return mini
