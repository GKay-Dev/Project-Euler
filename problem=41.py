# Pandigital Prime - https://projecteuler.net/problem=41

from itertools import permutations
from prime import is_prime

def largest_pandigital_prime():
    # Check for pandigital numbers from 9 digits down to 1 digit
    for n in range(9, 0, -1):
        # Generate the pandigital number string
        pandigital_str = ''.join(str(i) for i in range(1, n + 1))
        # Generate all permutations of the pandigital number
        pandigital_permutations = sorted(permutations(pandigital_str), reverse=True)
        
        for perm in pandigital_permutations:
            num = int(''.join(perm))
            if is_prime(num):
                return num
    return None


if __name__ == "__main__":
    result = largest_pandigital_prime()
    print(f"The largest n-digit pandigital prime is: {result}")