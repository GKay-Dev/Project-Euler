# Pandigital Products - https://projecteuler.net/problem=32

def is_pandigital(a, b, c):
    """Check if the concatenation of a, b, and c is a 1-9 pandigital number."""
    concat_str = str(a) + str(b) + str(c)
    return len(concat_str) == 9 and set(concat_str) == set('123456789')

def find_pandigital_products():
    """Find all products whose multiplicand/multiplier/product identity is 1-9 pandigital."""
    pandigital_products = set()
    
    # Check combinations of multiplicand and multiplier
    for a in range(1, 100):  # a can be 1 to 2 digits
        for b in range(100, 10000 // a):  # b can be 3 to 4 digits
            c = a * b
            if is_pandigital(a, b, c):
                pandigital_products.add(c)
    
    return sum(pandigital_products)


if __name__ == "__main__":
    result = find_pandigital_products()
    print(f"The sum of all products whose multiplicand/multiplier/product identity is 1-9 pandigital is: {result}")