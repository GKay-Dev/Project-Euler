# Sub-string Divisibility - https://projecteuler.net/problem=43

from itertools import permutations

def has_substring_divisibility(p):
    """Check if the pandigital number has the required substring divisibility properties."""
    primes = [2, 3, 5, 7, 11, 13, 17]
    for i, prime in enumerate(primes):
        substring = int(''.join(p[i+1:i+4]))
        if substring % prime != 0:
            return False
    return True


if __name__ == "__main__":
    total_sum = 0
    digits = '0123456789'
    
    for p in permutations(digits):
        if has_substring_divisibility(p):
            pandigital_number = int(''.join(p))
            total_sum += pandigital_number
    
    print(f"The sum of all 0 to 9 pandigital numbers with substring divisibility properties is: {total_sum}")