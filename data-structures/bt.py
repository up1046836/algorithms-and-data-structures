class BinaryTree:
    """
    External nodes have no value and no children
    Only root node has no parent
    """

    class Node:
        def __init__(self, parent=None, left=None, right=None, value=None):
            self.value = value
            self.left = left
            self.right = right
            self.parent = parent
        
        def is_internal(self):
            return True if self.value != None else False

        def is_external(self):
            return not self.is_internal()

        def is_root(self):
            return True if self.parent == None else False

        def depth(self):
            if self.is_root(): return 0
            else: return 1 + self.parent.depth()

        def __repr__(self):
            if self.is_root(): description = 'Root'
            elif self.is_internal(): description = 'Internal'
            else: description = 'External'
            return f'{description} Node {id(self)}: {self.value}'

    def __init__(self, iterable=None):
        self.root = BinaryTree.Node()
        
        if iterable:
            for element in iterable:
                self.insert(element)

    def search(self, value, node=None):
        if not node: node = self.root
        if node.is_external() or node.value == value: return node
        elif node.value < value: return self.search(value, node.right)
        else: return self.search(value, node.left)

    def height(self, node=None):
        # maximum depth of external nodes
        if not node: node = self.root
        if node.is_external(): return -1
        else: return 1 + max(self.height(node.left), self.height(node.right))

    def inorder(self, node=None):
        if not node: node = self.root
        if node.is_internal():
            self.inorder(node.left)
            print(node)
            self.inorder(node.right)

    def remove_above_external(self, node):
        if node.left.is_external():
            if node == self.root: 
                node.right.parent = None
                self.root = node.right
            elif node.parent.left == node: 
                node.right.parent = node.parent
                node.parent.left = node.right
            else: 
                node.right.parent = node.parent
                node.parent.right = node.right
        else: 
            if node == self.root: 
                node.left.parent = None
                self.root = node.left
            elif node.parent.left == node:
                node.left.parent = node.parent
                node.parent.left = node.left
            else: 
                node.left.parent = node.parent
                node.parent.right = node.left

    def remove(self, value):
        current = self.search(value)
        if current.is_external(): return None
        elif current.left.is_external() or current.left.is_external():
            self.remove_above_external(current)
        else:
            right_min = self.find_min(current.right)
            current.value = right_min.value
            self.remove_above_external(right_min)

    def find_min(self, node=None):
        if not node: node = self.root
        if node.is_external(): return node.parent
        else: return self.find_min(node.left)

    def insert(self, value):
        if not self.root:
            self.root = BinaryTree.Node(value)
        else:
            current = self.search(value, self.root)

            while current.is_internal():
                current = current.left
            current.value = value
            current.left = BinaryTree.Node(current)
            current.right = BinaryTree.Node(current)
