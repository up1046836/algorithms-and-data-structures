import time
import naive
from code import Code
import find_pairs
import os

class TestCase():
    def __init__(self, file, algorithm1, algorithm2):
        self.algorithm1 = algorithm1
        self.algorithm2 = algorithm2
        self.file = file
        self.status = False
        self.check = False
        self.run()

    def __str__(self):
        green = "\033[0;32m"
        normal = "\033[0m"
        if self.check:
            status_str = f"{green}[OK]{normal} "
            description_str = f"Found {len(self.result1)} pairs in {file} "
            description_str = f"{description_str: <60}"
            algorithm1_str = f"Hash Table ({self.running_time1:.2f}s)"
            algorithm1_str = f"{algorithm1_str: ^30}"
            algorithm2_str = f"Naive ({self.running_time2:.2f}s)"
            algorithm2_str = f"{algorithm2_str: ^30}"
            return status_str + description_str + algorithm1_str + algorithm2_str

    def __repr__(self):
        return self.__str__()

    def run(self):
        self.running_time1 = float('-inf')
        self.running_time2 = float('-inf')
        self.result1 = None
        self.result2 = None
        self.status = False
        self.check = True

        with open(self.file, 'r') as f:
            codes = [Code(code) for code in f.read().splitlines()]

        start = time.process_time()
        self.result1 = self.algorithm1.find_pairs(codes)
        end = time.process_time()

        self.running_time1 = end-start

        start = time.process_time()
        self.result2 = self.algorithm2.find_pairs(codes)
        end = time.process_time()

        self.running_time2 = end-start

        for pair in self.result1:
            if pair not in self.result2: self.check = False

        for pair in self.result2:
            if pair not in self.result1: self.check = False

        self.status = True

if __name__ == "__main__":
    files = os.listdir('inputs/')
    files.sort(key = lambda x: int(x.split('_')[0]))
    print()
    for file in files:
        file = 'inputs/' + file
        with open(file, 'r'): 
            test_case = TestCase(file, find_pairs, naive)    
            print(test_case)
    print()
