# Circular Primes - https://projecteuler.net/problem=35

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

def get_rotations(n):
    """Generate all rotations of a number's digits."""
    s = str(n)
    rotations = []
    for i in range(len(s)):
        rotations.append(int(s[i:] + s[:i]))
    return rotations

def is_circular_prime(n):
    """Check if all rotations of n are prime."""
    return all(is_prime(rotation) for rotation in get_rotations(n))

def count_circular_primes(limit):
    """Count circular primes below the given limit."""
    count = 0
    for num in range(2, limit):
        if is_circular_prime(num):
            count += 1
    return count


if __name__ == "__main__":
    limit = 1_000_000
    result = count_circular_primes(limit)
    print(f"Number of circular primes below {limit}: {result}")