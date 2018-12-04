#
#A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
#
#Given the root to a binary tree, count the number of unival subtrees.
#
#For example, the following tree has 5 unival subtrees:
#
#   0
#  / \
# 1   0
#    / \
#   1   0
#  / \
# 1   1


class Btree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count(btree):
    if btree.left == None and btree.right == None:
        return 1

    if btree.left.val == btree.right.val == btree.val:
        return 1 + count(btree.left) + count(btree.right)
    
    return count(btree.left) + count(btree.right)

def main():
    btree = Btree(0, 
        Btree(1), Btree(0, 
            Btree(1, Btree(1), Btree(1)), Btree(0)))
    print(count(btree))

if __name__ == "__main__":
    main()