class BinarySearchTree:
    """
    Left child values are less or equal than parent value
    Right child values are greater than parent value
    """
    class Node:
        """
        Binary tree node
        External nodes have no value, no children and no descendants
        Only root node has no parent
        """
        def __init__(self, parent=None, left=None, right=None, descendants=None,  value=None):
            self.value = value
            self.left = left
            self.right = right
            self.parent = parent
            self.descendants = descendants
        
        def is_internal(self):
            return True if self.value != None else False

        def is_external(self):
            return not self.is_internal()

        def is_root(self):
            return True if self.parent == None else False

        def depth(self):
            # number of ancestors
            if self.is_root(): return 0
            else: return 1 + self.parent.depth()

        def __repr__(self):
            if self.is_root(): description = 'Root'
            elif self.is_internal(): description = 'Internal'
            else: description = 'External'
            return (f'{description} Node {id(self)} '
                    f'(value: {self.value} '
                    f'descendants: {self.descendants})'
            )

    def __init__(self, iterable=None):
        self.root = self.create_external()
        if iterable:
            for element in iterable:
                self.insert(element)

    def create_external(self, parent=None):
        return BinarySearchTree.Node(parent=parent)

    def insert(self, value):
        if self.root.is_external():
            self.external_to_internal(self.root, value)
        else:
            current = self.search(value, update=True)

            while current.is_internal():
                current.descendants += 1
                current = self.search(value, current.left, update=True)

            self.external_to_internal(current, value)

    def external_to_internal(self, node, value):
        # transform external node to internal node
        node.value = value
        node.descendants = 0
        node.left = self.create_external(parent=node)
        node.right = self.create_external(parent=node)

    def search(self, value, node=None, update=False):
        if not node: node = self.root

        if node.is_external(): return node

        if node.value == value: return node

        if update: node.descendants += 1

        if value > node.value: return self.search(value, node.right, update)
        else: return self.search(value, node.left, update)

    def inorder(self, node=None):
        if not node: 
            node = self.root
        if node.is_internal():
            self.inorder(node.left)
            print(node)
            self.inorder(node.right)

    def select(self, index=None, node=None):
        if not node: node = self.root
        
        if node.left.descendants == None: node_index = 0
        else: node_index = node.left.descendants + 1

        if node_index == index: return node
        elif node_index > index: return self.select(index, node.left)
        else: return self.select(index - node_index - 1, node.right)

    def find_min(self, node=None, update=False):
        if not node: node = self.root
        if node.is_external(): return node.parent
        else: 
            if update: node.descendants -= 1
            return self.find_min(node.left)

    def remove_above_external(self, node):
        if node.left.is_external():
            if node == self.root: 
                node.right.parent = None
                self.root = node.right
            elif node.parent.left == node: 
                node.parent.descendants -= 1
                node.right.parent = node.parent
                node.parent.left = node.right
            else: 
                node.parent.descendants -= 1
                node.right.parent = node.parent
                node.parent.right = node.right
        else: 
            if node == self.root: 
                node.left.parent = None
                self.root = node.left
            elif node.parent.left == node:
                node.parent.descendants -= 1
                node.left.parent = node.parent
                node.parent.left = node.left
            else: 
                node.parent.descendants -= 1
                node.left.parent = node.parent
                node.parent.right = node.left

    def remove(self, value):
        current = self.search(value)
        if current.is_external(): return None
        elif current.left.is_external() or current.right.is_external():
            self.remove_above_external(current)
        else:
            right_min = self.find_min(current.right, update=True)
            current.value = right_min.value
            self.remove_above_external(right_min)
