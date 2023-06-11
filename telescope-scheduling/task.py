class Task:
    def __init__(self, name, start, finish, value, predecessor_index=None):
        self.name = name
        self.start = start
        self.finish = finish
        self.value = value
        self.predecessor_index = predecessor_index

    def __repr__(self):
        return f'({self.name}, {self.start}, {self.finish}, {self.value})'
