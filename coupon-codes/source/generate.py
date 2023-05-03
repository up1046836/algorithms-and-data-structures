import random
import string 
from code import Code
import sys
from find_pairs import find_pairs, find_candidates
import os

random.seed(1046836)
letters = string.ascii_uppercase[:11]
digits = string.digits[0:6]

def generate_random_code():
     code = "-".join([
            "".join(random.choices(letters, k=4)),
            "".join(random.choices(digits, k=4)), 
            "".join(random.choices(letters, k=4))
            ])
     return code

def generate_pair_code(code):
    position = random.choice([0,1,2,3,5,6,7,8,10,11,12,13])
    if position in [0,1,2,3,10,11,12,13]:
        letter = random.choice([letter for letter in letters if letter != code[position]])
        new_code = code[:position] + letter + code[position+1:]
    else:
        digit = random.choice([digit for digit in digits if digit != code[position]])
        new_code = code[:position] + digit + code[position+1:]
    return new_code

def generate_codes(n):
    k = random.choice(range(n+1))
    codes = set()
        
    while len(codes) < n:
        codes.add(generate_random_code())

    if n == 100000:
        codes = [Code(code) for code in codes]
        pairs = find_pairs(codes)
        return (len(pairs), codes)

    for _ in range(k):
        code = random.choice(list(codes))
        new_code = generate_pair_code(code)
        codes.add(new_code)

    while len(codes) > n:
        code = random.choice(list(codes))
        codes.remove(code)

    codes = [Code(code) for code in codes]
    pairs = find_pairs(codes)

    return (len(pairs), codes)

def generate_file(n):
    k, codes = generate_codes(n)
    file = os.path.dirname(__file__) + f'/../inputs/{n}_codes_{k}_pairs.input'
    with open(file, 'w') as f:
        for code in codes:
            f.write(code.code + '\n')
        print(f'Generated {file}')

if __name__ == "__main__":
    print()
    for i in range(2, 17):
        n = 2**i
        generate_file(n)
    generate_file(100000)
    print()
