from result import Result
from time import process_time
import functools

def algorithm_1(test_case, timeout):
    start_time = process_time()

    lst = test_case.input
    max_sum = float('-inf')
    start = None
    end = None

    for i in range(len(lst)):
        for j in range(i, len(lst)):
            current_sum = 0
            for k in range(i, j + 1):
                if process_time() - start_time >= timeout: return Result(algorithm_1, test_case, timeout=timeout)
                current_sum += lst[k]
            if current_sum >= max_sum:
                max_sum = current_sum
                start = i
                end = j

    end_time = process_time()
    return Result(algorithm_1, test_case, max_sum, start, end, round(end_time - start_time, 4))

def algorithm_2(test_case, timeout):
    start_time = process_time()

    lst = test_case.input
    max_sum = float('-inf')
    start = None
    end = None

    for i in range(len(lst)):
        current_sum = 0
        for j in range(i, len(lst)):
            if process_time() - start_time >= timeout: return Result(algorithm_1, test_case, timeout=timeout)
            current_sum += lst[j]
            if current_sum >= max_sum:
                max_sum = current_sum
                start = i
                end = j

    end_time = process_time()
    return Result(algorithm_2, test_case, max_sum, start, end, round(end_time - start_time, 4))

def algorithm_3(test_case, timeout):
    
    @functools.total_ordering
    class Res:
        def __init__(self, max_sum, start, end):
            self.max_sum = max_sum
            self.start = start
            self.end = end
        
        def __eq__(self, other):
            return self.max_sum == other.max_sum

        def __lt__(self, other):
            return self.max_sum < other.max_sum

    start_time = process_time()
    def max_sum(lst, start, end):
        if start == end: return Res(lst[start], start, end)

        middle_index = (start + end)//2
        left = max_sum(lst, start, middle_index)
        right = max_sum(lst, middle_index + 1, end)
        middle_left = Res(float('-inf'), None, middle_index)
        middle_right = Res(float('-inf'), middle_index + 1, None)

        if process_time() - start_time >= timeout: return None

        current_sum = 0
        for i in range(middle_index, start - 1, -1):
            current_sum += lst[i]
            if current_sum >= middle_left.max_sum:
                middle_left.max_sum = current_sum
                middle_left.start = i

        current_sum = 0
        for i in range(middle_index + 1, end + 1):
            current_sum += lst[i]
            if current_sum >= middle_right.max_sum:
                middle_right.max_sum = current_sum
                middle_right.end = i

        middle_left_right = Res(middle_left.max_sum + middle_right.max_sum, middle_left.start, middle_right.end)
        return max(left, right, middle_left, middle_right, middle_left_right)

    result = max_sum(test_case.input, 0, len(test_case.input) - 1)
    end_time = process_time()
    
    if not result: return Result(algorithm_3, test_case, timeout=timeout)

    return Result(algorithm_3, test_case, result.max_sum, result.start, result.end, round(end_time - start_time, 4))

def algorithm_4(test_case, timeout):
    start_time = process_time()

    lst = test_case.input
    max_sums = [float('-inf')]
    max_sum = float('-inf')
    start = None
    end = None
    current_start = 0

    for i in range(len(lst)):
        if process_time() - start_time >= timeout: return Result(algorithm_1, test_case, timeout=timeout)
        if lst[i] + max_sums[i] < lst[i]:
            current_start = i
            max_sums.append(lst[i])
        else:
            max_sums.append(lst[i] + max_sums[i])
        if max_sums[-1] >= max_sum:
            max_sum = max_sums[-1]
            start = current_start
            end = i

    end_time = process_time()
    return Result(algorithm_4, test_case, max_sum, start, end, round(end_time - start_time, 4))
