import random


class LinkedList:
    def __init__(self,content):
        self.content = content
        self.next = None

    def __str__(self):
        return "( " + str(self.content) + str(self.next) + " )"

#binary tree python
class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return "( " + str(self.val) + " ( " + str(self.left) + " | " + str(self.right) + "))" 


class Solution:
    def __init__(self):
        self.list_of_linkedlist = list()
        self.max_depth = 0

    def populate_ll(self, depth):
        self.max_depth = depth
        for number_of_depth in range(0, depth):
            self.list_of_linkedlist.append(list())


    def list_of_depths(self, binary_tree, depth):
        """
        return linked list
        """

        print('self.list_of_linkedlist is : ', self.list_of_linkedlist)


        if binary_tree.val: 
            self.list_of_linkedlist[depth-self.max_depth].append(binary_tree.val)

        if binary_tree.left is None and binary_tree.right is None:
            return self.list_of_linkedlist

        if binary_tree.left:
            return self.list_of_depths(binary_tree.left, depth+1)

        if binary_tree.right:
            return self.list_of_depths(binary_tree.right, depth+1)



def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    
    if root == None:
        return 0

    else:
        return max(maxDepth(root.left), maxDepth(root.right) )+ 1


def make_random_balanced_tree(depth):
    if depth>0:
        tree = BinaryTree(random.randint(0, 100))
        tree.left=make_random_balanced_tree(depth-1)
        tree.right=make_random_balanced_tree(depth-1)
        return tree
    else:
        return None


#testing

if __name__ == '__main__':
    mysolx = Solution()

    #building testcase 1

    balanced_tree = make_random_balanced_tree(5)

    print balanced_tree

    print "\nIs changed to:\n"

    count=0
    
    tree_max_depth = maxDepth(balanced_tree)

    print('tree_max_depth is : ', tree_max_depth)

    mysolx.populate_ll(tree_max_depth)

    for ll in mysolx.list_of_depths(balanced_tree, tree_max_depth):
        count += 1
        print str(count) + ": " + str(ll)

    print("list version : ", mysolx.list_of_linkedlist)
    
#sample output of binary_tree_to_list_of_linked_lists
##( 60 ( ( 59 ( ( 32 ( ( 95 ( ( 42 ( None | None)) | ( 11 ( None | None)))) | ( 1 ( ( 56 ( None | None)) | ( 11 ( None | None)))))) | ( 26 ( ( 25 ( ( 68 ( None | None)) | ( 56 ( None | None)))) | ( 29 ( ( 41 ( None | None)) | ( 21 ( None | None)))))))) | ( 88 ( ( 63 ( ( 58 ( ( 4 ( None | None)) | ( 70 ( None | None)))) | ( 30 ( ( 53 ( None | None)) | ( 38 ( None | None)))))) | ( 4 ( ( 93 ( ( 91 ( None | None)) | ( 21 ( None | None)))) | ( 55 ( ( 62 ( None | None)) | ( 25 ( None | None))))))))))
##
##Is changed to:
##
##1: ( 60None )
##2: ( 88( 59None ) )
##3: ( 4( 63( 26( 32None ) ) ) )
##4: ( 55( 93( 30( 58( 29( 25( 1( 95None ) ) ) ) ) ) ) )
##5: ( 25( 62( 21( 91( 38( 53( 70( 4( 21( 41( 56( 68( 11( 56( 11( 42None ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )

#sample output of binary_tree_to_list_of_linked_lists
#list version [[18], [48, 46], [12, 80, 100, 45], [23, 9, 85, 73, 52, 40, 65, 30], [43, 94, 53, 94, 96, 35, 30, 37, 28, 9, 95, 84, 74, 49, 45, 24]]


