# Prime Permutations - https://projecteuler.net/problem=49

from itertools import permutations
from prime import is_prime

def find_prime_permutations():
    prime_permutations = []
    for num in range(1000, 10000):
        if is_prime(num):
            perms = set(int(''.join(p)) for p in permutations(str(num)) if p[0] != '0')
            prime_perms = [p for p in perms if is_prime(p) and p >= 1000]
            if len(prime_perms) >= 3:
                prime_permutations.append(sorted(prime_perms))
    return prime_permutations

def find_arithmetic_sequences(prime_permutations):
    sequences = []
    for primes in prime_permutations:
        length = len(primes)
        for i in range(length):
            for j in range(i + 1, length):
                diff = primes[j] - primes[i]
                third = primes[j] + diff
                if third in primes:
                    sequences.append((primes[i], primes[j], third))
    return sequences


if __name__ == "__main__":
    prime_permutations = find_prime_permutations()
    sequences = find_arithmetic_sequences(prime_permutations)
    for seq in sequences:
        if seq != (1487, 4817, 8147):  # Exclude the known sequence
            twelve_digit_number = "".join(map(str, seq))
            break

    print(f"The 12-digit number formed by the new sequence is: {twelve_digit_number}")
