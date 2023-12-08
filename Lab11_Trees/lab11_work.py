def bt_sum_even(root):
    if root is None:
        return 0
    left = bt_sum_even(root.left)
    right = bt_sum_even(root.right)
    if root.data % 2 == 0:
        return root.data + left + right
    else:
        return left + right


def contains(self, item):
    def c_helper(node, item):
        if self.root is None:
            return False
        if node.data == item:
            return True
        return c_helper(node.left, item) or c_helper(node.right, item)

    return c_helper(self.root, item)


def is_full(root):
    if root.left and not root.right:
        return False
    elif not root.left and root.right:
        return False
    elif root.left is None and root.right is None:
        return True
    else:
        return is_full(root.left) and is_full(root.right)
