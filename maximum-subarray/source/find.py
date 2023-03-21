from time import sleep
from algorithms import algorithm_1, algorithm_2, algorithm_3, algorithm_4
from test_case import TestCase

RUNNING_TIME = 1

def find(algorithm):
    def seek(algorithm, start, end):
        middle = (start + end)//2
        if start == middle:
            print(flush=True)
            return
        result = algorithm(TestCase(middle), timeout=RUNNING_TIME*10)
        print(f'{algorithm_name}: n = {middle} in {result.running_time}s', end='\r', flush=True)
        if RUNNING_TIME <= result.running_time and result.running_time <= RUNNING_TIME + 0.05:
            print(flush=True)
            return
        elif result.running_time > RUNNING_TIME:
            seek(algorithm, start, middle)
        else: 
            seek(algorithm, middle, end)

    algorithm_name = algorithm.__name__.replace("_", ' ').capitalize()
    start = end = 1

    while True:
        test_case = TestCase(end)
        result = algorithm(test_case, timeout=RUNNING_TIME*10)

        print(f'{algorithm_name}: n = {end} in {result.running_time}s', end='\r', flush=True)
        if RUNNING_TIME <= result.running_time and result.running_time <= RUNNING_TIME + 0.05:
            print(flush=True)
            return
        elif result.running_time > RUNNING_TIME:
            break

        start = end
        end = end * 2

    seek(algorithm, start, end)


print('\033[?25l')
algorithms = [algorithm_1, algorithm_2, algorithm_3, algorithm_4]
for algorithm in algorithms:
    find(algorithm)
print('\033[?25h')
