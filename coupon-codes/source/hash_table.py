from sympy import nextprime

class HashTable():
    def __init__(self, data):
        self.length = nextprime(1.3 * len(data))
        self.data = [[] for _ in range(self.length)]
        for item in data:
            self.insert(item)

    def hash(self, code):
        return hash(code) % self.length

    def insert(self, item):
        self.data[self.hash(item.code)].append(item)

    def search(self, code):
        bucket = self.data[self.hash(code)]
        if len(bucket) == 0:
            return False
        if len(bucket) == 1:
            item = bucket[0]
            return item if item.code == code else False

        for item in bucket:
            if item.code == code:
                return item

        return False
