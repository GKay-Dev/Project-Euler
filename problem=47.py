# Distinct Primes Factors - https://projecteuler.net/problem=47

def prime_sieve(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, limit + 1, start):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]

def distinct_prime_factors_count(n, primes):
    count = 0
    for prime in primes:
        if prime * prime > n:
            break
        if n % prime == 0:
            count += 1
            while n % prime == 0:
                n //= prime
    if n > 1:
        count += 1
    return count

def find_first_sequence(length, distinct_count):
    limit = 1000000
    primes = prime_sieve(limit)
    consecutive = 0

    for i in range(2, limit):
        if distinct_prime_factors_count(i, primes) == distinct_count:
            consecutive += 1
            if consecutive == length:
                return i - length + 1
        else:
            consecutive = 0
    return None


if __name__ == "__main__":
    result = find_first_sequence(4, 4)
    print(f"The first four consecutive integers to have four distinct prime factors each start at: {result}")