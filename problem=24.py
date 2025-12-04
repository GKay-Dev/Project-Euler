# Lexicographic Permutations - https://projecteuler.net/problem=24

def lexicographic_permutation(digits, n):
    from math import factorial

    permutation = []
    k = n - 1  # Convert to zero-based index
    available_digits = digits[:]
    
    while available_digits:
        f = factorial(len(available_digits) - 1)
        index = k // f
        permutation.append(available_digits.pop(index))
        k %= f
    
    return ''.join(map(str, permutation))


if __name__ == "__main__":
    digits = list(range(10))
    n = 1000000
    result = lexicographic_permutation(digits, n)
    print(f"The {n}th lexicographic permutation of the digits 0-9 is: {result}")