# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
#     2
#    / \
#   1   3
# Binary tree [2,1,3], return true.
# Example 2:
#     1
#    / \
#   2   3
# Binary tree [1,2,3], return false.



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.range_min = float('-inf')
        self.range_max = float('+inf')

    def isValidBST(self, root, range_min, range_max):
        """gs
        :type root: TreeNode
        :rtype: bool
        """
        self.range_min = range_min
        self.range_max = range_max

        print('range_min is : ', range_min, ' and range_max is : ', range_max)

        if root is None:
            return True

        else:
            
            if root.left:
                return self.isValidBST(root.left, self.range_min, root.val)

            if root.right:
                return self.isValidBST(root.right, root.val, self.range_max)

            if not root.left and not root.right:
                if root.val < range_max and root.val >= range_min:
                    return True
                else:
                    return False
            
            # print('root.left is : ', root.left.val, ' root.right is : ', root.right.val, ' root is : ', root.val)
            # if root.left.val > root.val or root.right.val < root.val:
            #     return False

