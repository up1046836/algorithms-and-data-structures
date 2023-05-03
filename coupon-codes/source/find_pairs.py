from hash_table import HashTable
from code import Code
from pair import Pair
import string
import time
import sys

def find_candidates(code):
    letters = string.ascii_uppercase[0:11]
    digits = string.digits[0:6]

    section1 = code[0:4]
    section2 = code[5:9]
    section3 = code[10:14]

    candidates = []

    for i in range(4):
        for letter in letters:
            begin1, end1 = section1[:i], section1[i+1:]
            begin3, end3 = section3[:i], section3[i+1:]
            letter1, letter3 = section1[i], section3[i]

            if letter1 != letter:
                candidates.append("-".join([begin1 + letter + end1, section2, section3]))
            if letter3 != letter:
                candidates.append("-".join([section1, section2, begin3 + letter + end3]))

        for digit in digits:
            begin2, end2 = section2[:i], section2[i+1:]
            digit2 = section2[i]

            if digit2 != digit:
                candidates.append("-".join([section1, begin2 + digit + end2, section3]))

    return candidates

def find_pairs(codes):
    hash_table = HashTable(codes)
    pairs = set()
    for code in codes:
        candidates = find_candidates(code.code)
        for candidate in candidates:
            found = hash_table.search(candidate)
            if found:
                pair = Pair(code, found)
                if pair not in pairs:
                    pairs.add(pair)
    return pairs

if __name__ == "__main__":
    args = sys.argv
    codes = []
    with open(sys.argv[1]) as f:
        codes = [Code(code) for code in f.read().splitlines()]
    start = time.process_time()
    pairs = find_pairs(codes)
    end = time.process_time()
    print(f"\nFound {len(pairs)} pairs with hamming distance of 1 in {end-start:.2f}s\n")
    if pairs:
        for i, pair in enumerate(pairs):
            print(f"{i+1}. {pair}")
        print()
