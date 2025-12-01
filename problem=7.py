# 10 001st Prime - https://projecteuler.net/problem=7

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

def find_nth_prime_number(n):
    count = 2
    i = 5
    
    while count < n:
        if is_prime(i):
            count += 1
            if count == n:
                return i
        i += 2 if i % 6 == 5 else 4
    
    return i

if __name__ == "__main__":
    n = 10_001
    result = find_nth_prime_number(n)
    print(f"The {n}st prime number is: {result}")