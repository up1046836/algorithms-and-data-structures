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
        yellow = "\033[1;33m"
        normal = "\033[0m"
        if self.check and self.result2:
            status_str = f"{green}[OK]{normal} "
            description_str = f"Found {len(self.result1)} pairs in {self.file.replace(os.path.dirname(__file__)+'/../inputs/', '')} "
            description_str = f"{description_str: <60}"
            algorithm1_str = f"Hash Table ({self.running_time1:07.4f}s)"
            algorithm1_str = f"{algorithm1_str: ^40}"
            algorithm2_str = f"Naive ({self.running_time2:07.4f}s)"
            algorithm2_str = f"{algorithm2_str: <40}"
            return status_str + description_str + algorithm1_str + algorithm2_str
        elif self.check and not self.result2:
            status_str = f"{green}[OK]{normal} "
            description_str = f"Found {len(self.result1)} pairs in {self.file.replace(os.path.dirname(__file__)+'/../inputs/', '')} "
            description_str = f"{description_str: <60}"
            algorithm1_str = f"Hash Table ({self.running_time1:07.4f}s)"
            algorithm1_str = f"{algorithm1_str: ^40}"
            algorithm2_str = f"Naive {yellow}TIMEOUT{normal}"
            algorithm2_str = f"{algorithm2_str: <40}"
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

        if self.result2:
            for pair in self.result1:
                if pair not in self.result2: self.check = False

            for pair in self.result2:
                if pair not in self.result1: self.check = False

        self.status = True

def get_input_length(file):
    return int(file.split('_')[0])

if __name__ == "__main__":
    running_times_hash = {}
    running_times_naive = {}
    input_files_dir = os.path.dirname(__file__) + '/../inputs/'
    files = {input_files_dir + file: get_input_length(file) for file in os.listdir(input_files_dir)}
    print()
    for path, length in sorted(list(files.items()), key=lambda x: x[1]):
        with open(path, 'r'): 
            test_case = TestCase(path, find_pairs, naive)    
            running_times_hash[length] = test_case.running_time1
            running_times_naive[length] = test_case.running_time2 if test_case.result2 else '-'
            print(test_case)
    print()
    with open(os.path.dirname(__file__) + '/../results/running_times.results', 'w') as f:
        f.write(f'{"": ^20}{"Naive": ^30}{"Hash Table": ^30}\n\n')
        for length in sorted(list(files.values())):
            running_time1_str = f'{running_times_hash[length]:07.4f}'
            running_time2_str = running_times_naive[length] if running_times_naive[length] == '-' else f'{running_times_naive[length]:07.4f}'
            f.write(f'{length: <20}{running_time2_str: ^30}{running_time1_str: ^30}\n')
