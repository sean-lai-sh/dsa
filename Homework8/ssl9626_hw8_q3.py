import sys

from BinarySearchTreeMap import BinarySearchTreeMap as BSTMap


def getPreIndex():
    return constructTreeUtil.preIndex


def incrementPreIndex():
    # Use global scoped value to help with parameters and not losing value as we recursively go
    # through list
    constructTreeUtil.preIndex += 1
def constructTreeUtil(lst, key, mini, maxi, size):
    # Base Case
    if (getPreIndex() >= size):
        return None

    root = None

    # Is our current key element in the subtree or not
    if (key > mini and key < maxi):

        # Add an index to check and create the node
        root = BSTMap.Node(BSTMap.Item(key))
        incrementPreIndex()

        if (getPreIndex() < size):
            root.left = constructTreeUtil(lst, lst[getPreIndex()],mini, key, size)
        if (getPreIndex() < size):
            root.right = constructTreeUtil(lst, lst[getPreIndex()], key, maxi, size)

    return root
def restore_bst(prefix_lst):
    if len(prefix_lst) == 0:
        return BSTMap()
    INT_MAX = sys.maxsize
    INT_MIN = -sys.maxsize
    def help(pre):
        constructTreeUtil.preIndex = 0
        size = len(pre)
        return constructTreeUtil(pre, pre[0], INT_MIN, INT_MAX, size)
    tree = BSTMap()
    tree.root = help(prefix_lst)
    tree.n = len(prefix_lst)
    return tree



# t = restore_bst([9,7,3,1,5,13,11,15])
# for elem in t:
#     print(elem)
# if i_self >= len(lst):
#     return None, i_self
# else:
#     new_item = BinarySearchTreeMap.Item(lst[i_self], None)
#     new_node = BinarySearchTreeMap.Node(new_item)
#     if i_self + 1 < len(lst) and i_parent != i_self and lst[i_self + 1] > lst[i_parent]:
#         left_data = (None, i_self)
#     else:
#         left_data = res_helper(lst, i_self, i_self + 1)
#     right_data = None
#     if left_data[1] + 1 < len(lst) and i_parent != i_self and lst[int(left_data[1]) + 1] > lst[i_parent]:
#         right_data = (None, i_self)
#     else:
#         right_data = res_helper(lst, i_self, int(left_data[1]) + 1)
#     new_node.left = left_data[0]
#     new_node.right = right_data[0]
#     return new_node, max(left_data[1], right_data[1])
