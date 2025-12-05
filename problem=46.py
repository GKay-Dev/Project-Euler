# Goldbach's Other Conjecture - https://projecteuler.net/problem=46

from prime import is_prime
from itertools import count

def is_goldbach_other_conjecture(n):
    if is_prime(n):
        return True
    for i in range(1, int(n ** 0.5) + 1):
        square = i * i
        if square >= n:
            break
        if is_prime(n - 2 * square):
            return True
    return False

def find_smallest_odd_composite():
    for n in count(9, 2):  # Start from the first odd composite number
        if not is_prime(n):
            if not is_goldbach_other_conjecture(n):
                return n


if __name__ == "__main__":
    result = find_smallest_odd_composite()
    print(f"The smallest odd composite that cannot be written as the sum of a prime and twice a square is: {result}")