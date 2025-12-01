# Summation of Primes - https://projecteuler.net/problem=10

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_of_primes(n):
    i, prime_sum = 5, 5
    while i < n:
        if is_prime(i):
            prime_sum += i
        i += 2 if i % 6 == 5 else 4
    return prime_sum

if __name__ == "__main__":
    limit = 2_000_000
    result = sum_of_primes(limit)
    print(f"The sum of all primes below {limit} is: {result}")