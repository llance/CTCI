__author__ = 'lanceli'

from math import ceil

class BinaryTree(object):
    def __init__(self, nodeVal):
        self.nodeVal = nodeVal
        self.leftNode= None
        self.rightNode = None

    def getLeftNode(self):
        return self.leftNode

    def getRightNode(self):
        return self.rightNode

    def setLeftNode(self, nodeVal):
        self.leftNode = nodeVal

    def setRightNode(self, nodeVal):
        self.rightNode = nodeVal

    def setNodeVal(self, val):
        self.nodeVal = val

    def getNodeVal(self, val):
        return self.nodeVal


def getMiddleElementIndex(sortedArray):
    s_array_size = len(sortedArray)

    #is even sized 
    if (s_array_size % 2) == 0:
        return (s_array_size/2)

    #is odd sized 
    if (s_array_size % 2) != 0:
        return ((s_array_size/2) + 1)

def getLeftTreeElems(sortedArray, middleNodeIndex):
    return sortedArray[:middleNodeIndex]

def getRightTreeElems(sortedArray, middleNodeIndex):
    return sortedArray[middleNodeIndex:]




def buildLeftTree(leftTreeArray, binaryTree):
    middle_elem_index = getMiddleElementIndex(leftTreeArray)

    leftTreeElems = getLeftTreeElems(leftTreeArray, middle_elem_index)

    rightTreeElems = getRightTreeElems(leftTreeArray, middle_elem_index)

    binaryTree.setLeftNode(leftTreeArray[middle_elem_index])

    if leftTreeElems:
        buildLeftTree(leftTreeElems, binaryTree.getLeftNode)

    if rightTreeElems:
        buildRightTree(rightTreeElems, binaryTree.getRightNode)


def buildRIghtTree(rightTreeArray, binaryTree):
    middle_elem_index = getMiddleElementIndex(rightTreeArray)

    leftTreeElems = getLeftTreeElems(rightTreeArray, middle_elem_index)

    rightTreeElems = getRightTreeElems(rightTreeArray, middle_elem_index)

    binaryTree.setRightNode(rightTreeArray[middle_elem_index])

    if leftTreeElems:
        buildLeftTree(leftTreeElems, binaryTree.getLeftNode)

    if rightTreeElems:
        buildRightTree(rightTreeElems, binaryTree.getRightNode)




def createBSTRoot(sortedArray):
    middle_elem_index = getMiddleElementIndex(sortedArray)

    leftTreeElems = getLeftTreeElems(sortedArray, middle_elem_index)

    rightTreeElems = getRightTreeElems(sortedArray, middle_elem_index)

    myMinimalTree = BinaryTree(sortedArray[middle_elem_index])

    if leftTreeElems:
        buildLeftTree(leftTreeElems, myMinimalTree.getLeftNode)

    if rightTreeElems:
        buildRightTree(rightTreeElems, myMinimalTree.getRightNode)


    return myMinimalTree


intarray1=[1,2,3,4,5,6,7,8,9,10,12,15,18,22,43,144,515]

print str(createBSTRoot(intarray1))

