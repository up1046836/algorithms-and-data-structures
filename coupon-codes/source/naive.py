import sys
from code import Code
from pair import Pair
import time

YELLOW = "\033[1;33m"
NORMAL = "\033[0m"

def hamming_distance(code1, code2):
    return sum([char1 != char2 for char1, char2 in zip(code1, code2)])

def find_pairs(codes):
    pairs = []
    for i, code in enumerate(codes):
        for j in range(i, len(codes)):
            candidate = codes[j]
            if hamming_distance(code.code, candidate.code) == 1:
                new_pair = Pair(code, candidate)
                if new_pair not in pairs:
                    pairs.append(new_pair)
        end = time.process_time()
    return pairs

if __name__ == "__main__":
    file = sys.argv[1]

    with open(file, 'r') as f:
        codes = [Code(code) for code in f.read().splitlines()]

    start = time.process_time()
    pairs = find_pairs(codes)
    end = time.process_time()

    if pairs != None:
        print(f"\nFound {len(pairs)} pairs with hamming distance of 1 in {end-start:.2f}s\n")

        if pairs:
            for i, pair in enumerate(pairs):
                print(f"{i+1}. {pair}")
            print()
    else:
        print()
        print(f"{YELLOW}TIMEOUT{NORMAL}")
        print()
