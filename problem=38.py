# Pandigital Multiples - https://projecteuler.net/problem=38

def is_pandigital(num_str):
    """Check if the string num_str is 1 to 9 pandigital."""
    return len(num_str) == 9 and set(num_str) == set('123456789')

def find_largest_pandigital_multiple():
    largest_pandigital = 0
    for i in range(1, 10000):  # 4-digit base number is sufficient
        concatenated_product = ''
        n = 1
        while len(concatenated_product) < 9:
            concatenated_product += str(i * n)
            n += 1
        if is_pandigital(concatenated_product):
            largest_pandigital = max(largest_pandigital, int(concatenated_product))
    return largest_pandigital


if __name__ == "__main__":
    result = find_largest_pandigital_multiple()
    print(f"The largest 1 to 9 pandigital 9-digit number formed as described is: {result}")