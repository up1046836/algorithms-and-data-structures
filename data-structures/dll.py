class DoubleLinkedList:
    class Node:
        def __init__(self, prev_node=None, next_node=None, element=None):
            self.prev = prev_node
            self.next = next_node
            self.element = element

    def __init__(self, iterable):
        self.size = 0
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
        current = self.head
        for element in iterable:
            self.add(current, element)
            current = current.next

    def add(self, node, element):
        self.size += 1
        new_node = self.Node(element=element)
        tmp = node.next
        node.next = new_node
        new_node.next = tmp
        new_node.prev = node
        new_node.next.prev = new_node

    def remove(self, node):
        self.size += 1
        node.prev.next = node.next
        node.next.prev = node.prev

    def __str__(self):
        current = self.head.next
        string = 'head'
        while current != self.tail:
            string += ' --> ' + str(current.element)
            current = current.next
        string += ' --> tail'
        return string

    def __repr__(self):
        return self.__str__()
