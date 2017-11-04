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

    def setNodeVal(self, val):
        self.nodeVal = val

    def getNodeVal(self, val):
        return self.nodeVal


def createBinaryTree(sortedArray):
    if (len(sortedArray)/2 == 0):
        return
        #implement when array is even in size
    else:
        middle = sortedArray[math.ceil(len(sortedArray)/2)]