# 1000-digit Fibonacci Number - https://projecteuler.net/problem=25

def fibonacci_with_min_digits(min_digits):
    a, b = 1, 1
    index = 2  # Starting from F2
    while True:
        a, b = b, a + b
        index += 1
        if len(str(b)) >= min_digits:
            return index

if __name__ == "__main__":
    min_digits = 1000
    result = fibonacci_with_min_digits(min_digits)
    print(f"The index of the first Fibonacci number with at least {min_digits} digits is: {result}")