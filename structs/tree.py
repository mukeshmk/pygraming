from tnode import TNode

class BinaryTree():
    def __init__(self):
        self._root = None
    
    def get_root(self):
        return self._root
     
    def set_root(self, element):
        self._root = TNode(element)

    def add_node(self, element):
        cur_node = self._root
        while cur_node:
            if cur_node.get_left() is None:
                cur_node.set_left(TNode(element))
            elif cur_node.get_right() is None:
                cur_node.set_right(TNode(element))
            cur_node = cur_node.get_left()
