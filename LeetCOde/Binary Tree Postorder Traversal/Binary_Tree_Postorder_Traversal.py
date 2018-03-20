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
        # print('root.val is : ', root.val)
        
        if not root:
             # and root.left is None and root.right is None:
            print('no root val')
            return self.nodelist
            
        if root.left is not None:
            print('root.left.val is : ', root.val)
            self.nodelist = self.postorderTraversal(root.left)
            
            if root.right is not None:
                print('root.right.val is : ', root.val)
                self.nodelist = self.postorderTraversal(root.right)
                self.nodelist.append(root.val)
                print('self.nodelist is : ', self.nodelist)
                return self.nodelist

            
            self.nodelist.append(root.val)
            print('self.nodelist is : ', self.nodelist)

            return self.nodelist
            
        if root.right is not None:
            print('root.right.val is : ', root.val)
            self.nodelist = self.postorderTraversal(root.right)
            self.nodelist.append(root.val)
            print('self.nodelist is : ', self.nodelist)

            return self.nodelist


        if root.left is None and root.right is None and root.val is not None:
            print('reached a leaf')
            self.nodelist.append(root.val)
            print('self.nodelist is : ', self.nodelist)
            return self.nodelist



