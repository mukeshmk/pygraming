class Node():
    def __init__(self, data):
        self._data = data
        self._next = None
        self._prev = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next
    
    def get_prev(self):
        return self._prev

    def set_next(self, node):
        self._next = node
    
    def set_prev(self, node):
        self._prev = node
