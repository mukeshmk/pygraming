class TNode():
    def __init__(self, data, max_children = 2):
        self._data = data
        if max_children == 0:
            raise Exception('can\'t create a node with 0 children')
        self._children = [None] * max_children

    def get_data(self):
        return self._data

    def get_children(self):
        return self._children

    def get_left(self):
        if not len(self._children) == 2:
            raise Exception('can\'t use feature with more than 2 childern')
        return self._children[0]
    
    def get_right(self):
        if not len(self._children) == 2:
            raise Exception('can\'t use feature with more than 2 childern')
        return self._children[1]

    def set_left(self, node):
        if not len(self._children) == 2:
            raise Exception('can\'t use feature with more than 2 childern')
        self._children[0] = node
    
    def set_right(self, node):
        if not len(self._children) == 2:
            raise Exception('can\'t use feature with more than 2 childern')
        self._children[1] = node

    def set_child(self, node, child_id):
        if not child_id >= len(self._children):
            raise Exception('child_id is greater than the max_children')
        self._children[child_id] = node

    def get_child(self, node, child_id):
        if not child_id >= len(self._children):
            raise Exception('child_id is greater than the max_children')
        return self._children[child_id]

