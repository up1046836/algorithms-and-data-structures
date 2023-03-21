from test_case import TestCase
from algorithms import algorithm_1, algorithm_2, algorithm_3, algorithm_4
import os.path
from result import Result

NUMBER_OF_TEST_CASES = 28
TIMEOUT = 60

def create_test_cases(n):
    test_cases = []
    print()
    for i in range(n):
        test_cases.append(TestCase(2**i))
        print(f'\rCreating test cases: {(i+1)/n:.0%}', end='', flush=True)
    print()
    return test_cases

if __name__ == '__main__':
    test_cases = create_test_cases(NUMBER_OF_TEST_CASES)
    algorithms = [algorithm_1, algorithm_2, algorithm_3, algorithm_4]

    results = {}
    for algorithm in algorithms:
        results[algorithm] = {}
        print()
        for test_case in test_cases:
            result = algorithm(test_case, timeout=TIMEOUT)
            result.status = result == algorithm_4(test_case, TIMEOUT)
            print(result)

            if result.running_time == float('inf'):
                break

            results[algorithm][test_case] = result

    with open(os.path.dirname(__file__) + '/../results/report.results', 'w') as f:
        f.write(f'{"": ^20}{"Algorithm 1": ^20}{"Algorithm 2": ^20}{"Algorithm 3": ^20}{"Algorithm 4": ^20}\n\n')

        for test_case in test_cases:
            f.write(f'{len(test_case.input): <20}')
            for algorithm in algorithms: 
                if test_case in results[algorithm].keys():
                    f.write(f'{format(results[algorithm][test_case].running_time, "07.4f"): ^20}')
                else:
                    f.write(f'{"-": ^20}')
            f.write('\n')
