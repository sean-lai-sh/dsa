from LinkedBinaryTree import *

def is_perfect_recur(root):
    if not root:
        return False
    left = is_perfect_recur(root.left)
    right = is_perfect_recur(root.right)
    return (left and right) or not (left or right)


def is_perfect_recur_itr(root):
    line = ArrayQueue()
    line.enqueue(root)
    is_per = False
    while (line.is_empty() == False):
        curr_node = line.dequeue()
        if (curr_node.left and curr_node.right) or not (curr_node.left or curr_node.right):
            is_per = True
        else:
            return False
        if (curr_node.left is not None):
            line.enqueue(curr_node.left)
        if (curr_node.right is not None):
            line.enqueue(curr_node.right)
    return is_per


def invert_bt_recur(root):
    if root:
        left = invert_bt_recur(root.left)
        right = invert_bt_recur(root.right)
        root.left = right
        root.right = left
    return root

def invert_bt_itr(root):
    queue = ArrayQueue()
    queue.enqueue(root)
    while not queue.is_empty():
        n = queue.dequeue()
        n.left, n.right = n.right, n.left
        if n.left:
            queue.enqueue(n.left)
        if n.right:
            queue.enqueue(n.right)
    return root

def merge_bt(t1, t2):
    def helper(node_from, node_to):
        if not node_from:
            return None
        else:
            if not node_to:
                new_node = LinkedBinaryTree.Node(node_from.data)
                new_node.left = helper(node_from.left, None)
                new_node.right = helper(node_from.right, None)
                return new_node
            else:
                node_to.data = node_to.data + node_from.data
                node_to.left = helper(node_from.left, node_to.left)
                node_to.right = helper(node_from.right, node_to.right)
                return node_to

    new_root = helper(t1.root, None)
    return helper(t2.root, new_root)
