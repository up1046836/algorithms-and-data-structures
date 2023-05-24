class PriorityQueue1:
    """
    insert: O(n)
    remove: O(1)
    """
    def __init__(self):
        self._values = [None]

    def remove(self):
        return self._values.pop()

    def insert(self, value):
        self._values.append(value)
        i = len(self._values) - 2
        while i > 0 and self._values[i] < value:
            self._values[i + 1] = self._values[i]
            i -= 1
        self._values[i + 1] = value

    def size(self):
        return len(self._values) - 1
