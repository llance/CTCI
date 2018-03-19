# Given a binary tree, return the postorder traversal of its nodes' values.

# For example:
# Given binary tree [1,null,2,3],

#    1
#     \
#      2
#     /
#    3
 

# return [3,2,1].

# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.nodelist = list()

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root.val and root.left is None and root.right is None:
            print('no root val')
            return 
            
        if root.left is not None:
            print('left')
            self.postorderTraversal(root.left)
        if root.right is not None:
            print('right')
            self.postorderTraversal(root.right)

        if root.left is None and root.right is None and root.val is not None:
            print('reached a leaf')
            self.nodelist.append(root)





