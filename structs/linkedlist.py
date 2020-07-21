from node import Node


class LinkedList():
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def print(self):
        if self.is_empty():
            raise Exception('LinkedList Empty!')

        node = self._head

        while node:
            print(node.get_data())
            node = node.get_next()

    def append(self, item):
        new_node = Node(item)

        if self.is_empty():
            self._head = new_node
        else:
            cur_node = self._head
            while cur_node:
                if cur_node.get_next() is None:
                    cur_node.set_next(new_node)
                    break
                cur_node = cur_node.get_next()

    def pop(self):
        if self.is_empty():
            raise Exception('LinkedList Empty!')

        cur_node = self._head
        poped_node = self._head

        if self._head.get_next() is None:
            self._head = None
        else:
            while cur_node:
                if cur_node.get_next().get_next() is None:
                    poped_node = cur_node.get_next()
                    cur_node.set_next(None)
                    break
                cur_node = cur_node.get_next()
        return poped_node.get_data()

    def head(self):
        if self.is_empty():
            raise Exception('LinkedList Empty!')
        return self._head.get_data()

    def search(self, element):
        if self.is_empty():
            raise Exception('LinkedList Empty!')
        cur_node = self._head
        while cur_node:
            if cur_node.get_data() == element:
                return True
            cur_node = cur_node.get_next()
        return False

