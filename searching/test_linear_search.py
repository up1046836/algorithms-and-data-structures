import unittest
import random
from linear_search import linear_search

N = 100000
rng = range(0, N)

class TestLinearSearch(unittest.TestCase):

    def test_1(self):
        lst = random.sample(rng, 1)
        value = lst[0]
        self.assertEqual(linear_search(lst, value), 0)

    def test_50(self):
        lst = random.sample(rng, 50)
        value = -1
        self.assertEqual(linear_search(lst, value), None)

    def test_100(self):
        lst = random.sample(rng, 100)
        value = lst[76]
        self.assertEqual(linear_search(lst, value), 76)

if __name__ == '__main__':
    unittest.main()
