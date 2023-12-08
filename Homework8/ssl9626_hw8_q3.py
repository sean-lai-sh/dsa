from BinarySearchTreeMap import BinarySearchTreeMap as BSTMap


def restore_bst(prefix_lst):
    if len(prefix_lst) == 0:
        return BSTMap()

    def res_helper(lst, i_parent, i_self):
        if len(lst) <= i_self:
            return None, i_self
        else:
            print(lst[i_self])
            new_node = BSTMap.Node(BSTMap.Item(lst[i_self], None))
            r_ptr = i_self
            if i_self + 1 <= len(lst):
                if lst[i_self + 1] < lst[i_self]:
                    print("I'm searching:", lst[i_self + 1])
                    l_data = res_helper(lst, i_self, i_self + 1)
                    new_node.left = l_data[0]
                    r_ptr = l_data[1]
                    print(l_data)
                if i_self == i_parent:
                    if r_ptr + 1 < len(lst) and lst[i_self] < lst[r_ptr + 1]:
                        r_data = res_helper(lst, i_self, r_ptr + 1)
                        new_node.right = r_data[0]
                        r_ptr = r_data[1]
                else:
                    if (
                        r_ptr + 1 < len(lst)
                        and lst[i_self] < lst[r_ptr + 1] < lst[i_parent]
                    ):
                        r_data = res_helper(lst, i_self, r_ptr + 1)
                        new_node.right = r_data[0]
                        r_ptr = r_data[1]

            return new_node, r_ptr

    data = res_helper(prefix_lst, 0, 0)
    tree = BSTMap()
    tree.root = data[0]
    tree.n = len(prefix_lst)
    return tree


t = restore_bst([9, 7, 3, 1, 5, 13, 11, 15])
for elem in t:
    print(elem)
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
