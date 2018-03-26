class Solution:
    def list_of_depths(self, binary_tree, depth):
        """
        return linked list
        """

        tree_max_depth = self.maxDepth(binary_tree)

        list_of_linkedlist = list()

        for number_of_depth in range(ree_max_depth):
            list_of_linkedlist.append(linkedlist())


        if binary_tree.val:
            list_of_linkedlist[depth].append(binary_tree.val)

        if binary_tree.left is None and node.right is None:
            return list_of_linkedlist

        else:
            return list_of_depths(node.left, depth+1), list_of_depths(node.max, depth+1)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root == None:
            return 0

        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right) )+ 1