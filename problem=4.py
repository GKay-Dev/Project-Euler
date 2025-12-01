# Largest Palindrome Product - https://projecteuler.net/problem=4

def is_palindrome(number):
    return str(number) == str(number)[::-1]

def largest_palindrome_product(digits):
    max_number = 10**digits - 1
    min_number = 10**(digits - 1)
    largest_palindrome = 0

    for i in range(max_number, min_number - 1, -1):
        for j in range(i, min_number - 1, -1):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product

    return largest_palindrome

if __name__ == "__main__":
    digits = 3
    result = largest_palindrome_product(digits)
    print(f"The largest palindrome made from the product of two {digits}-digit numbers is: {result}")