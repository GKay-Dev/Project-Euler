# Largest Prime Factor - https://projecteuler.net/problem=3

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

if __name__ == "__main__":
    number = 600_851_475_143
    result = largest_prime_factor(number)
    print(f"The largest prime factor of {number} is: {result}")