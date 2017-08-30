__author__ = 'lanceli'

from LinkedList import Node

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
            if current is None:
                raise ValueError("data not found in linkedlist")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False

        while current and found is False:
            if current.get_data == data:
                found = True
            else:
                previous = current
                current = current.get_next()
            if current is None:
                raise ValueError("data not found in linkedlist")
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())




