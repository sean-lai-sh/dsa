import math


def is_height_balanced(bin_tree):
    if bin_tree.is_empty():
        return True

    def bal_help(root):
        if not root:
            return (0, True)
        lHeight = bal_help(root.left)
        rHeight = bal_help(root.right)
        if lHeight == 0 and rHeight == 0:
            return (1, True)
        else:
            diff = abs(lHeight[0] - rHeight[0])
            h_val = int(max(lHeight[0], rHeight[0])) + 1
            if diff > 1:
                return (h_val, False)
            else:
                is_bal = lHeight[1] and rHeight[1]
                return (h_val, is_bal)

    return bal_help(bin_tree.root)[1]
