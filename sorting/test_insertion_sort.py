import unittest
import random
from insertion_sort import insertion_sort

class TestInsertionSort(unittest.TestCase):
    def test_1(self):
        lst = random.sample(range(0,100000), 2)
        self.assertEqual(insertion_sort(lst), sorted(lst))

    def test_2(self):
        lst = random.sample(range(0,100000), 10)
        self.assertEqual(insertion_sort(lst), sorted(lst))

    def test_3(self):
        lst = random.sample(range(0,100000), 50)
        self.assertEqual(insertion_sort(lst), sorted(lst))

    def test_4(self):
        lst = random.sample(range(0,100000), 100)
        self.assertEqual(insertion_sort(lst), sorted(lst))

    def test_5(self):
        lst = random.sample(range(0,100000), 1000)
        self.assertEqual(insertion_sort(lst), sorted(lst))
    
if __name__ == '__main__':
    unittest.main()
