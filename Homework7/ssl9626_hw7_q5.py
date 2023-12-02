from LinkedBinaryTree import LinkedBinaryTree


def create_expression_tree(prefix_exp_str):
    if not isinstance(prefix_exp_str, str):
        raise TypeError("Invalid Input")
    if len(prefix_exp_str) == 0:
        return LinkedBinaryTree()

    def helper(expr, index):
        if index == len(expr):
            return (None, index)
        if not expr[index].isdigit():
            left = helper(expr, index + 1)
            right = helper(expr, left[1] + 1)
            root = LinkedBinaryTree.Node(expr[index])
            root.left = left[0]
            root.right = right[0]
            return root, max(left[1], right[1])
        else:
            return (LinkedBinaryTree.Node(int(expr[index])), index)

    expressions = prefix_exp_str.split(" ")
    bTree = LinkedBinaryTree()
    bTree.root = helper(expressions, 0)[0]
    bTree.size = len(expressions)
    return bTree


def prefix_to_postfix(prefix_exp_str):
    if prefix_exp_str == "":
        return ""
    tree = create_expression_tree(prefix_exp_str)

    # take left
    def create_string(root):
        if root:
            yield from create_string(root.left)
            yield from create_string(root.right)
            yield root.data

    return " ".join([str(elem) for elem in create_string(tree.root)])
