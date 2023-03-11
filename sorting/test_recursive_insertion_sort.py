import unittest
import random
import sys
from recursive_insertion_sort import recursive_insertion_sort

class TestInsertionSort(unittest.TestCase):

    def test_2(self):
        lst = random.sample(range(0,100000), 2)
        self.assertEqual(recursive_insertion_sort(lst,len(lst)-1), sorted(lst))

    def test_10(self):
        lst = random.sample(range(0,100000), 10)
        self.assertEqual(recursive_insertion_sort(lst,len(lst)-1), sorted(lst))

    def test_50(self):
        lst = random.sample(range(0,100000), 50)
        self.assertEqual(recursive_insertion_sort(lst,len(lst)-1), sorted(lst))

    def test_100(self):
        lst = random.sample(range(0,100000), 100)
        self.assertEqual(recursive_insertion_sort(lst,len(lst)-1), sorted(lst))

    def test_1000(self):
        lst = random.sample(range(0,100000), 1000)
        self.assertEqual(recursive_insertion_sort(lst,len(lst)-1), sorted(lst))
    
    def test_10000(self):
        lst = random.sample(range(0,100000), 10000)
        self.assertEqual(recursive_insertion_sort(lst,len(lst)-1), sorted(lst))

    def test_100000(self):
        lst = random.sample(range(0,100000), 100000)
        self.assertEqual(recursive_insertion_sort(lst,len(lst)-1), sorted(lst))


if __name__ == '__main__':
    sys.setrecursionlimit(10000000)
    unittest.main()
