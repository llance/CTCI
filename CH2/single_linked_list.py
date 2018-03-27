class Node(object):
	"""
		docstring for Node
		hold a node value and reference to the next node
	"""
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next
		
	def setNext(self, next):
		self.next = next

	def getNext():
		return self.next

	def getData(self, data):
		self.data = data



"""
The Linked List

My simple implementation of a linked list includes the following methods:

Insert: inserts a new node into the list
Size: returns size of list
Search: searches list for a node containing the requested data and returns that node if found, otherwise raises an error
Delete: searches list for a node containing the requested data and removes it from list if found, otherwise raises an error
"""		

class LinkedList(object):

	def __init__(self, head = None):
		self.head = head


	def insert(self, data):
		new_node = Node(data)
		self.setNext(self.head)
		self.head = new_node

	def getSize(self):
		count = 0
		current = self.head
		while current.getNext() is not None:
			count += 1
			current = current.getNext()
		return count


	def search(self, data):
		found = False
		current = self.head
		while found is False:
			if current.getData() == data:
				found = True
				return current
			else:
				current = current.getNext()
		if found is False:
			raise "did not find node in list"


	def delete(self, data):		
		found = False
		current = self.head
		while found is False:
			if current.getData() == data:
				found = True
				nextNode = current.getNext():
				current.data = nextNode
				current.setNext(nextNode.getNext())
				return
			else:
				current = current.getNext()
		if found is False:
			raise "couldn't delete node from List because it wasn't found"






