import unittest
import random
from merge_sort import merge_sort

class TestMergeSort(unittest.TestCase):
    def test_1(self):
        lst = random.sample(range(0,100000), 2)
        self.assertEqual(merge_sort(lst), sorted(lst))

    def test_2(self):
        lst = random.sample(range(0,100000), 10)
        self.assertEqual(merge_sort(lst), sorted(lst))

    def test_3(self):
        lst = random.sample(range(0,100000), 50)
        self.assertEqual(merge_sort(lst), sorted(lst))

    def test_4(self):
        lst = random.sample(range(0,100000), 100)
        self.assertEqual(merge_sort(lst), sorted(lst))

    def test_5(self):
        lst = random.sample(range(0,100000), 1000)
        self.assertEqual(merge_sort(lst), sorted(lst))
    
    def test_6(self):
        lst = random.sample(range(0,100000), 10000)
        self.assertEqual(merge_sort(lst), sorted(lst))

    def test_7(self):
        lst = random.sample(range(0,100000), 100000)
        self.assertEqual(merge_sort(lst), sorted(lst))

if __name__ == '__main__':
    unittest.main()
