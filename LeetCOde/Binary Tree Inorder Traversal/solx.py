# Given a binary tree, return the inorder traversal of its nodes' values.

# For example:
# Given binary tree [1,null,2,3],
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.traversal = []
        print("initialized traversal : ", self.traversal)
        
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        
        if root is None:
            return []
        
        else:                      
            if root.left:
                self.inorderTraversal(root.left)
            
            self.traversal.append(root.val)
            print("traversal is : ", self.traversal)

            if root.right:
                self.inorderTraversal(root.right)
        
        return self.traversal
            
        