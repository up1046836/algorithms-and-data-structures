class Result:
    def __init__(self, algorithm, test_case, max_sum=None, start=None, end=None, running_time=float('inf'), timeout=float('inf'), status=None):
        self.algorithm = algorithm
        self.test_case = test_case
        self.running_time = running_time
        self.max_sum = max_sum
        self.start = start
        self.end = end
        self.timeout = timeout
        self.status = status

    def __str__(self):
        if self.max_sum:
            if self.status:
                return (f'[\033[92mOK\033[0m] '
                        f'{self.algorithm.__name__.capitalize().replace("_", " ")} run {self.test_case}: '
                        f'{self.max_sum} ({self.start}, {self.end}) in {self.running_time:.4f}s '
                )
            if self.status == False:
                return (f'[\033[91mFL\033[0m] '
                        f'{self.algorithm.__name__.capitalize().replace("_", " ")} run {self.test_case}: '
                        f'{self.max_sum} ({self.start}, {self.end}) in {self.running_time:.4f}s '
                )

            else:
                return (f'[NA] '
                        f'{self.algorithm.__name__.capitalize().replace("_", " ")} run {self.test_case}: '
                        f'{self.max_sum} ({self.start}, {self.end}) in {self.running_time:.4f}s '
                )

        else:
            return (f'[\033[93mTM\033[0m] ' 
                    f'{self.algorithm.__name__.capitalize().replace("_", " ")} run {self.test_case}: '
                    f'aborted after {self.timeout}s'
            )

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.max_sum == other.max_sum and self.start == other.start and self.end == other.end
