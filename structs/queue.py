# basic Queue data structure - https://www.geeksforgeeks.org/queue-data-structure/
# not using from collections import deque
from node import Node

class Queue():
    def __init__(self):
        self._items = []

    def get_queue(self):
        return self._items

    def is_empty(self):
        return len(self._items) == 0
    
    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue Empty!')
        item = self._items[0]
        del self._items[0]
        return item

    def front(self):
        if self.is_empty():
            raise Exception('Queue Empty!')
        return self._items[0]
    
    def rear(self):
        if self.is_empty():
            raise Exception('Queue Empty!')
        return self._items[-1]


class NodeQueue():
    def __init__(self):
        self._front = None
        self._rear = None
    
    def is_empty(self):
        return self._front == None

    def print(self):
        if self.is_empty():
            raise Exception('Queue Empty!')

        cur_node = self._front
        while cur_node:
            print(cur_node.get_data())
            cur_node = cur_node.get_next()

    def enqueue(self, item):
        node = Node(item)
        if self.is_empty():
            self._front = node
            self._rear = node
        else:
            self._rear.set_next(node)
            self._rear = node
    
    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue Empty!')
        
        node = self._front
        if self._front == self._rear:
            self._rear = None
            self._front = None
        else:
            self._front = self._front.get_next()
        return node.get_data()

    def front(self):
        if self.is_empty():
            raise Exception('Queue Empty!')
        return self._front.get_data()
    
    def rear(self):
        if self.is_empty():
            raise Exception('Queue Empty!')
        return self._rear.get_data()
    
    def search(self, element):
        if self.is_empty():
            raise Exception('Queue Empty!')
        cur_node = self._front
        while cur_node:
            if cur_node.get_data() == element:
                return True
            cur_node = cur_node.get_next()
        return False
