# basic stack data structure - https://www.geeksforgeeks.org/stack-data-structure/

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
