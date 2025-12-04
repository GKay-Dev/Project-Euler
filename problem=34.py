# Digit Factorials - https://projecteuler.net/problem=34

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def sum_of_digit_factorials(num):
    return sum(factorial(int(digit)) for digit in str(num))

def find_curious_numbers(limit):
    curious_numbers = []
    for i in range(10, limit):
        if i == sum_of_digit_factorials(i):
            curious_numbers.append(i)
    return curious_numbers


if __name__ == "__main__":
    limit = 50000  # A reasonable upper limit for searching curious numbers
    curious_numbers = find_curious_numbers(limit)
    result = sum(curious_numbers)
    print("Curious numbers:", curious_numbers)
    print("Sum of curious numbers:", result)