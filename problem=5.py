# Smallest Multiple - https://projecteuler.net/problem=5

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def smallest_multiple(n):
    multiple = 1
    for i in range(2, n + 1):
        multiple = lcm(multiple, i)
    return multiple

if __name__ == "__main__":
    n = 20
    result = smallest_multiple(n)
    print(f"The smallest positive number that is evenly divisible by all of the numbers from 1 to {n} is: {result}")