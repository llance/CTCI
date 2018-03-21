# Given a binary tree

#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Note:

# You may only use constant extra space.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
# For example,
# Given the following perfect binary tree,
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

# solx: 
# set root node next to none

# while visiting node, check if parent node is set, if not, set next pointer to null
# if parent node is set, check if parent node.right is None, if is None, set next pointer to null
# else : set next pointer to point to parent node.right 



class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        self.next = None


        while (root.val is not None):
            pass

    def checkIfHasRightNode(self, root, parent):


