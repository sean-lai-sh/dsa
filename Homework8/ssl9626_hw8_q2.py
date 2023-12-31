from BinarySearchTreeMap import BinarySearchTreeMap


def create_chain_bst(n):
    if n == 0:
        return BinarySearchTreeMap()
    tree = create_chain_bst(n - 1)
    tree.insert(n, None)
    return tree


def add_items(bst, low, high):
    def add_item_helper(l, h):
        if l == h:
            return BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(l, None))
        else:
            midpoint = (l + h)//2
            mid_key_val = BinarySearchTreeMap.Item(midpoint, None)
            mid_node = BinarySearchTreeMap.Node(mid_key_val)
            if l - (midpoint-1) == l:
                left = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(l, None))
            else:
                left = add_item_helper(l, midpoint-1)
            if h - (midpoint + 1) == h:
                right = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(h, None))
            else:
                right = add_item_helper(midpoint + 1, h)
            mid_node.left = left
            left.parent = left
            mid_node.right = right
            right.parent = right
            return mid_node

    bst.root = add_item_helper(low, high)
    bst.n = high
    # Consider using a helper with recursion so that we avoid the cost of insert which is huge.
    # if low >= high:
    #     bst.insert(low, None)
    # else:
    #     mid_point = (low + high) // 2
    #     bst.insert(mid_point, None)
    #     add_items(bst, low, mid_point - 1)
    #     add_items(bst, mid_point + 1, high)


def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst


# tree = BinarySearchTreeMap()
# tree[9] = None
# tree[3] = None
# tree[1] = None
# tree[5] = None
# tree[4] = None
# tree[6] = None
# tree[13] = None
# tree[11] = None
# tree[12] = None
# tree[15] = None
# tree[14] = None
#
# del tree[9]
# del tree[13]
# del tree[1]
# del tree[3]
# for elem in tree:
#     print(elem)
