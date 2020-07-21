# basic Queue data structure - https://www.geeksforgeeks.org/queue-data-structure/
# not using from collections import deque

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
