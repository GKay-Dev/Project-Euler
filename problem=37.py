# Truncatable Primes - https://projecteuler.net/problem=37

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


def truncate_left_to_right(n):
    """Remove digits from left to right."""
    s = str(n)
    truncations = []
    for i in range(len(s)):
        truncations.append(int(s[i:]))
    return truncations


def truncate_right_to_left(n):
    """Remove digits from right to left."""
    s = str(n)
    truncations = []
    for i in range(len(s)):
        truncations.append(int(s[:len(s) - i]))
    return truncations


def is_truncatable_prime(n):
    """Check if n is truncatable from both directions."""
    if n < 10:  # Single digit primes don't count
        return False
    
    left_truncations = truncate_left_to_right(n)
    right_truncations = truncate_right_to_left(n)
    
    return all(is_prime(t) for t in left_truncations) and all(is_prime(t) for t in right_truncations)


def find_truncatable_primes(count=11):
    """Find the first 'count' truncatable primes."""
    truncatable = []
    num = 10  # Start from 10 (first 2-digit number)
    
    while len(truncatable) < count:
        if is_truncatable_prime(num):
            truncatable.append(num)
        num += 1
    
    return truncatable


if __name__ == "__main__":
    primes = find_truncatable_primes(11)
    print(f"Truncatable primes: {primes}")
    result = sum(primes)
    print(f"Sum of the eleven truncatable primes: {result}")

