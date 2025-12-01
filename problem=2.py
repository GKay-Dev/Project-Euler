# Even Fibonacci Numbers - https://projecteuler.net/problem=2

def even_fibonacci_sum(limit):
    a, b = 1, 2  # Starting values for Fibonacci sequence
    even_sum = 0

    while a <= limit:
        if a % 2 == 0:
            even_sum += a
        a, b = b, a + b  # Update to next Fibonacci numbers

    return even_sum    

if __name__ == "__main__":
    limit = 4_000_000
    result = even_fibonacci_sum(limit)
    print(f"The sum of even Fibonacci numbers not exceeding {limit} is: {result}")