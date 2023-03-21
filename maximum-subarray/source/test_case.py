import random
from result import Result
from algorithms import algorithm_4

random.seed(1046836)

class TestCase:

    count = 1

    def __init__(self, n):
        self.count = TestCase.count
        self.input = random.choices(range(-100, 101), k=n)
        TestCase.count += 1

    def __str__(self): 
        return f'Test Case {self.count} (n = {len(self.input)})'

    def __repr__(self):
        return self.__str__()
