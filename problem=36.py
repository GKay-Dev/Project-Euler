# Double-base Palindromes - https://projecteuler.net/problem=36

def is_palindrome(s):
    return s == s[::-1]

def sum_double_base_palindromes(limit):
    total = 0
    for number in range(1, limit):
        decimal_str = str(number)
        binary_str = bin(number)[2:]  # Convert to binary and remove '0b' prefix
        if is_palindrome(decimal_str) and is_palindrome(binary_str):
            total += number
    return total


if __name__ == "__main__":
    limit = 1000000
    result = sum_double_base_palindromes(limit)
    print(f"The sum of all numbers less than {limit} which are palindromic in base 10 and base 2 is: {result}")