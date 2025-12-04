# Quadratic Primes - https://projecteuler.net/problem=27

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

def consecutive_primes_count(a, b):
    n = 0
    while True:
        quadratic_value = n * n + a * n + b
        if not is_prime(quadratic_value):
            break
        n += 1
    return n 

def find_best_coefficients(limit):
    max_count = 0
    best_a = 0
    best_b = 0
    for a in range(-limit + 1, limit):
        for b in range(-limit, limit + 1):
            count = consecutive_primes_count(a, b)
            if count > max_count:
                max_count = count
                best_a = a
                best_b = b
    return best_a, best_b


if __name__ == "__main__":
    limit = 1000
    a, b = find_best_coefficients(limit)
    print(f"The coefficients are a = {a}, b = {b}")
    print(f"The product of the coefficients is {a * b}")