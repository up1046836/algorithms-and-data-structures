import random
import string 
from code import Code

random.seed(1046836)

def generate_codes(n):
    codes = []
    letters = string.ascii_uppercase[:11]
    digits = string.digits[0:6]

    while len(codes) < n:
        new_code =  "-".join([
            "".join(random.choices(letters, k=4)),
            "".join(random.choices(digits, k=4)), 
            "".join(random.choices(letters, k=4))
        ])
        
        if new_code not in codes:
            codes.append(new_code)

    codes = [Code(code) for code in codes]
    return codes
