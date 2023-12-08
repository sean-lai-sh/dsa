from BinarySearchTreeMap import BinarySearchTreeMap


def create_chain_bst(n):
    if n == 0:
        return BinarySearchTreeMap()
    tree = create_chain_bst(n - 1)
    tree.insert(n, None)
    return tree


def add_items(bst, low, high):
    # Consider using a helper with recursion so that we avoid the cost of insert which is huge.
    if low >= high:
        bst.insert(low, None)
    else:
        mid_point = (low + high) // 2
        bst.insert(mid_point, None)
        add_items(bst, low, mid_point - 1)
        add_items(bst, mid_point + 1, high)


def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst
