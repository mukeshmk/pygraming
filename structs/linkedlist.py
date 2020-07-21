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

    def insert_after(self, element_to_be_inserted, insert_after_element):
        if self.is_empty():
            raise Exception('LinkedList Empty! Can\'t insert after!')

        if not self.search(insert_after_element):
            raise Exception('Element doesn\'t exist in LinkedList')

        node = Node(element_to_be_inserted)
        cur_node = self._head

        while cur_node:
            if cur_node.get_data() == insert_after_element:
                temp_node = cur_node.get_next()
                cur_node.set_next(node)
                node.set_next(temp_node)
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

    def remove(self, element_to_be_removed):
        if self.is_empty():
            raise Exception('LinkedList Empty! Can\'t insert after!')
        if not self.search(element_to_be_removed):
            raise Exception('Element doesn\'t exist in LinkedList')

        cur_node = self._head
        poped_node = self._head
        prev_node = cur_node

        if self._head.get_data() == element_to_be_removed:
            self._head = self._head.get_next()
            return poped_node.get_data()
        
        cur_node = cur_node.get_next()
        while cur_node:
            if cur_node.get_data() == element_to_be_removed:
                poped_node = cur_node
                prev_node.set_next(cur_node.get_next())
                break
            prev_node = cur_node
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


l = LinkedList()
l.append('a')
l.append('b')
l.append('c')
# print(l.search('d'))
# l.print()
l.insert_after('x', 'b')
#l.print()
l.remove('a')
l.print()

# print(l.pop())
# print(l.pop())
# l.append('d')
# print(l.pop())
# l.print()
