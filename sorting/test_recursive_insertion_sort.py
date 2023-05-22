import unittest
import random
import sys
from recursive_insertion_sort import recursive_insertion_sort

class TestRecursiveInsertionSort(unittest.TestCase):
    def test_1(self):
        lst = random.sample(range(0,100000), 2)
        self.assertEqual(recursive_insertion_sort(lst), sorted(lst))

    def test_2(self):
        lst = random.sample(range(0,100000), 10)
        self.assertEqual(recursive_insertion_sort(lst), sorted(lst))

    def test_3(self):
        lst = random.sample(range(0,100000), 50)
        self.assertEqual(recursive_insertion_sort(lst), sorted(lst))

    def test_4(self):
        lst = random.sample(range(0,100000), 100)
        self.assertEqual(recursive_insertion_sort(lst), sorted(lst))

if __name__ == '__main__':
    sys.setrecursionlimit(100000000)
    unittest.main()
