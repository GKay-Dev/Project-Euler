# Factorial Digit Sum - https://projecteuler.net/problem=20

def factorial_digit_sum(n):
    from math import factorial
    fact = factorial(n)
    return sum(int(digit) for digit in str(fact))

if __name__ == "__main__":
    n = 100
    result = factorial_digit_sum(n)
    print(f"The sum of the digits in the factorial of {n} is: {result}")