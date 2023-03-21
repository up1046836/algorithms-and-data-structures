from time import sleep
from algorithms import algorithm_1, algorithm_2, algorithm_3, algorithm_4
from test_case import TestCase

RUNNING_TIME = 1

def find(algorithm):
    def seek(algorithm, current, previous):
        if current == previous:
            print()
            return
        result = algorithm(TestCase(current), timeout=RUNNING_TIME*10)
        middle = (current + previous)//2
        print(f'{algorithm_name}: n = {current} in {result.running_time}s', end='\r')
        sleep(1)
        if RUNNING_TIME <= result.running_time and result.running_time <= RUNNING_TIME + 0.15:
            print()
            return
        elif result.running_time > RUNNING_TIME:
            seek(algorithm, middle, current)
        else: 
            seek(algorithm, middle, previous)

    algorithm_name = algorithm.__name__.replace("_", ' ').capitalize()
    current = previous = 1

    while True:
        test_case = TestCase(current)
        result = algorithm(test_case, timeout=RUNNING_TIME*10)

        print(f'{algorithm_name}: n = {current} in {result.running_time}s', end='\r')
        if RUNNING_TIME <= result.running_time and result.running_time <= RUNNING_TIME + 0.15:
            print()
            return
        elif result.running_time > RUNNING_TIME:
            break

        previous = current
        current *= 2

    seek(algorithm, current, previous)


print('\033[?25l')
algorithms = [algorithm_1, algorithm_2, algorithm_3, algorithm_4]
for algorithm in algorithms:
    find(algorithm)
print('\033[?25h')
