# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

# An example is the root-to-leaf path 1->2->3 which represents the number 123.

# Find the total sum of all root-to-leaf numbers.

# For example,

#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.

# Return the sum = 12 + 13 = 25.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left_tree_val = 0 
        right_tree_val = 0

        if not root:
            return 0

        if root.left is not None:
            left_tree_val = self.traverseToLeaf(root.left, list().append(root.val))
        if root.right is not None:
            right_tree_val = self.traverseToLeaf(root.right, list().append(root.val))

        return left_tree_val + right_tree_val

    def traverseToLeaf(self, root, parent_trail):
        if (not root.left and not root.right):
            sum_without_leaf_val = 0
            for val in parent_trail:
                sum_without_leaf_val = sum_without_leaf_val + val
            return str(root.val) + sum_without_leaf_val
        
        if (root.left):
            if parent_trail is None:
                parent_trail = list()

            return self.traverseToLeaf(root.left, parent_trail.append(str(root.val)))

        if (root.right):
            if parent_trail is None:
                parent_trail = list()

            return self.traverseToLeaf(root.left, parent_trail.append(str(root.val)))
