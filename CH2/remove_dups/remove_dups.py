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


if __name__ == '__main__':
	print 'hello'

	