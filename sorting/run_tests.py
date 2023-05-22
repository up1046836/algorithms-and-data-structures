from unittest import TestSuite, TestLoader, TextTestRunner
from test_merge_sort import TestMergeSort
from test_insertion_sort import TestInsertionSort
from test_recursive_insertion_sort import TestRecursiveInsertionSort

if __name__ == "__main__":
    test_suite = TestSuite()
    test_loader = TestLoader()

    test_suite.addTests(test_loader.loadTestsFromTestCase(TestMergeSort))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestInsertionSort))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestRecursiveInsertionSort))

    runner = TextTestRunner()
    runner.run(test_suite)
