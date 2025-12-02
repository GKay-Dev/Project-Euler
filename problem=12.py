# Highly Divisible Triangular Number - https://projecteuler.net/problem=12

def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 2  # i and n/i
    if int(n**0.5)**2 == n:
        count -= 1  # Correct for a perfect square
    return count

def first_triangular_with_divisors(min_divisors):
    n = 1
    triangular_number = 0
    while True:
        triangular_number += n
        if count_divisors(triangular_number) > min_divisors:
            return triangular_number
        n += 1

if __name__ == "__main__":
    min_divisors = 500
    result = first_triangular_with_divisors(min_divisors)
    print(f"The first triangular number with over {min_divisors} divisors is: {result}")