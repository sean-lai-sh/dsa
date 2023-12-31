from ssl9626_BinarySearchTreeMap import *

def main():
    bst = BinarySearchTreeMap()
    bst[7] = None
    bst[5] = None
    bst[1] = None
    bst[14] = None
    bst[10] = None
    bst[3] = None
    bst[9] = None
    bst[13] = None
    print(bst.get_ith_smallest(3))
    # 5
    print(bst.get_ith_smallest(6))
    # 10
    print([elem for elem in bst])
    print([elem.lcount for elem in bst.inorder()])
    del bst[14]
    del bst[5]

    print([(elem.item.key, elem.lcount)for elem in bst.inorder()])
    print(bst.get_ith_smallest(3))
    # 7
    print(bst.get_ith_smallest(6))
    # 13
    print(bst.get_ith_smallest(2))

main()