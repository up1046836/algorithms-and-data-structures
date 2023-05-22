class Heap:
    """
    Dynamic array (list) implementation of heap with
    constant time searching using hash table (dictionary)
    
    Heap only keeps the last entry of equal elements

    insert: remove + O(logn)
    remove: search + O(logn)
    search: O(1)

    Compare must be implemented by subclass and returns 
    True if comparison rule is satisfied
    """

    def __init__(self):
        self.list = [None]
        self.size = 0
        self.elements = {}

    def insert(self, element):
        # remove element if it exists 
        self.remove(element)
        # add to the heap
        self.list.append(element)
        self.size += 1
        index = self.size
        self.elements[element] = index
        self.up_heap_bubbling(index)

    def swap(self, index_a, index_b):
        a = self.list[index_a]
        b = self.list[index_b]
        self.list[index_a] = b
        self.list[index_b] = a
        self.elements[a] = index_b
        self.elements[b] = index_a

    def remove(self, element):
        index = self.search(element)
        if index:
            last_index = self.size
            self.swap(index, last_index)
            self.size -= 1
            self.elements.pop(element)
            self.list.pop()
            self.down_heap_bubbling(index)
        return element

    def up_heap_bubbling(self, index):
        parent_index = index//2
        current = self.list[index]
        parent = self.list[parent_index]
        if not parent_index == 0 and not self.compare(current, parent):
            self.swap(index, parent_index)
            self.up_heap_bubbling(parent_index)

    def down_heap_bubbling(self, index):
        if index < self.size:
            current = self.list[index]
            left_index = 2*index
            right_index = 2*index + 1
            if left_index <= self.size and right_index > self.size:
                left = self.list[left_index]
                if not self.compare(current, left):
                    self.swap(index, left_index)
                    self.down_heap_bubbling(left_index)
            elif left_index < self.size and right_index <= self.size:
                left = self.list[left_index]
                right = self.list[right_index]
                element = self.choose(current, left, right)
                if element == left:
                    self.swap(index, left_index)
                    self.down_heap_bubbling(left_index)
                elif element == right:
                    self.swap(index, right_index)
                    self.down_heap_bubbling(right_index)

    def search(self, element):
        if element in self.elements:
            return self.elements[element]
        return None

    def first(self):
        if self.size > 0: return self.list[1]
        else: return None

class MaxHeap(Heap):
    """
    Max heap implementation
    
    Comparison rule: child < parent
    """

    def compare(self, child, parent):
        return child.__lt__(parent)

    def choose(self, a, b, c):
        return max(a, b, c)

class MinHeap(Heap):
    """
    Min heap implementation

    Comparison rule: child > parent
    """

    def compare(self, child, parent):
        return child.__gt__(parent)

    def choose(self, a, b, c):
        return min(a, b, c)
