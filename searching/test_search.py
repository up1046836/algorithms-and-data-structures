import unittest
import random
from linear_search import linear_search
from binary_search import binary_search

N = 100000
rng = range(0, N)

class TestLinearSearch(unittest.TestCase):

    def test_1(self):
        lst = random.sample(rng, 1)
        value = lst[0]
        self.assertEqual(linear_search(lst, value), 0)

    def test_2(self):
        lst = random.sample(rng, 50)
        value = -1
        self.assertEqual(linear_search(lst, value), None)

    def test_3(self):
        lst = random.sample(rng, 100)
        value = lst[76]
        self.assertEqual(linear_search(lst, value), 76)

    def test_4(self):
        lst = sorted(random.sample(rng, 100))
        value = lst[78]
        self.assertEqual(binary_search(lst, value), 78)

    def test_5(self):
        lst = sorted(random.sample(rng, 1))
        value = lst[0]
        self.assertEqual(binary_search(lst, value), 0)

    def test_5(self):
        lst = sorted(random.sample(rng, 1))
        value = lst[0]
        self.assertEqual(binary_search(lst, value), 0)

    def test_5(self):
        lst = sorted(random.sample(rng, 1))
        value = lst[0]
        self.assertEqual(binary_search(lst, value), 0)

    def test_5(self):
        lst = sorted(random.sample(rng, 1))
        value = lst[0]
        self.assertEqual(binary_search(lst, value), 0)

    def test_5(self):
        lst = sorted(random.sample(rng, 1))
        value = lst[0]
        self.assertEqual(binary_search(lst, value), 0)

    def test_5(self):
        lst = sorted(random.sample(rng, 1))
        value = lst[0]
        self.assertEqual(binary_search(lst, value), 0)

    def test_5(self):
        lst = sorted(random.sample(rng, 1))
        value = lst[0]
        self.assertEqual(binary_search(lst, value), 0)

    def test_5(self):
        lst = sorted(random.sample(rng, 1))
        value = lst[0]
        self.assertEqual(binary_search(lst, value), 0)

    def test_5(self):
        lst = sorted(random.sample(rng, 1))
        value = lst[0]
        self.assertEqual(binary_search(lst, value), 0)

    def test_6(self):
        lst = sorted(random.sample(rng, 2))
        value = lst[1]
        self.assertEqual(binary_search(lst, value), 1)

if __name__ == '__main__':
    unittest.main()
