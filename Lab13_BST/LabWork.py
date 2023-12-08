import sys


def min_max_BST(bst):
    if bst.is_empty():
        return (None, None)
    # Least is by going all the way down left
    # Max is all the way down the right
    # Iterative
    # Left ptr, Right ptr
    # Stop each when both are leaves
    # Then return the values of these nodes as tuples
    left_node = bst.root
    right_node = bst.root
    found_least = False
    found_max = False
    while not found_least or not found_max:
        if not found_least:
            if left_node.left:
                left_node = left_node.left
            else:
                found_least = True
        if not found_max:
            if right_node.right:
                right_node = right_node.right
            else:
                found_max = True
    return left_node.item.key, right_node.item.key

def glt_n(bst, n):
    if bst.root.item.key == n:
        return bst.root.item.key
    curr_glt = -1
    node_ptr = bst.root
    prev_node = bst.root
    while node_ptr:
        if node_ptr.item.key == n: # We found key no point iterating
            return n

        if node_ptr.right and node_ptr.right.item.key < n:
            prev_node = node_ptr
            node_ptr = node_ptr.right
            curr_glt = node_ptr.item.key


        if node_ptr.left and   node_ptr.item.key > n:
            prev_node = node_ptr
            node_ptr = node_ptr.left
            curr_glt = node_ptr.item.key


        if node_ptr == prev_node:
            break
        # Check their l diff and r diff, if they exist
        # if either is < difference, we change our ptr to there
        # else we have arrived at the minimum and we've found our "glt"
    # return value
    if curr_glt > -1:
        return curr_glt
    else:
        return -1

def compare_bst(bst1, bst2): # O(n log n)
    if bst1.n != bst2.n:
        return False
    lst_1 = [elem for elem in bst1] # O(n)
    lst_2 = [elem for elem in bst2] # O(n)
    lst_1.sort() # assume this is merge sorting O(n log n)
    lst_2.sort() # Same here
    for i in range(len(lst_1)):
        if lst_1[i] != lst_2[i]:
            return False
    return True

def is_BST(root):
    return is_BST_helper(root)[2]

def is_BST_helper(root):
    if root:
      left_data = is_BST_helper(root.left)
      right_data = is_BST_helper(root.right)
      if left_data[2] is False or right_data[2] is False:
          return root.item.key, root.item.key, False
      if left_data[0] is None and right_data[0] is None:
          return root.item.key, root.item.key, True
      is_searchTree = True
      min = root.item.key
      max = root.item.key
      if right_data[0] is not None:
          if root.item.key < right_data[0] and right_data[1] > root.item.key:
            max = right_data[1]
          else:
            is_searchTree = False
      if left_data[0] is not None:
          if root.item.key > left_data[0] and left_data[1] < root.item.key:
            min = left_data[0]
          else:
            is_searchTree = False
      return min, max, is_searchTree
    else:
        return (None, None, True)
