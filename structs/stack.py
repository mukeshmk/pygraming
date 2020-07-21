# basic stack data structure - https://www.geeksforgeeks.org/stack-data-structure/
from node import Node

class Stack():
    def __init__(self):
         self._items = []

    def get_stack(self):
        return self._items

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise Exception('Stack Empty!')
        return self._items.pop()
    
    def top(self):
        if self.is_empty():
            raise Exception('Stack Empty!')
        return self._items[-1]

    def search(self, element):
        if self.is_empty():
            raise Exception('Stack Empty!')
        for item in self._items:
            if item == element:
                return True
        return False


class NodeStack():
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def print(self):
        if self.is_empty():
            raise Exception('Stack Empty!')

        cur_node = self._top
        while cur_node:
            print(cur_node.get_data())
            cur_node = cur_node.get_next()

    def push(self, item):
        new_node = Node(item)
        if self.is_empty():
            self._top = new_node
        else:
            new_node.set_next(self._top)
            self._top = new_node
    
    def pop(self):
        if self.is_empty():
            raise Exception('Stack Empty!')

        top_node = self._top
        self._top = self._top.get_next()
        return top_node.get_data()
    
    def top(self):
        if self.is_empty():
            raise Exception('Stack Empty!')
        return self._top.get_data()

    def search(self, element):
        if self.is_empty():
            raise Exception('Stack Empty!')
        
        cur_node = self._top
        while cur_node:
            if cur_node.get_data() == element:
                return True
            cur_node = cur_node.get_next()
        return False
