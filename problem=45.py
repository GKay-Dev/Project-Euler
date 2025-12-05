# Triangular, Pentagonal, and Hexagonal - https://projecteuler.net/problem=45

def is_pentagonal(x):
    n = (1 + (1 + 24 * x) ** 0.5) / 6
    return n.is_integer()

def is_hexagonal(x):
    n = (1 + (1 + 8 * x) ** 0.5) / 4
    return n.is_integer()

def triangular(n):
    return n * (n + 1) // 2

def find_next_tri_pent_hex(start):
    n = start
    while True:
        t = triangular(n)
        if is_pentagonal(t) and is_hexagonal(t):
            return t
        n += 1


if __name__ == "__main__":
    # The first triangle number that is also pentagonal and hexagonal is 1
    # The second such number is 40755
    # We need to find the next one after 40755
    start_index = 286  # Since T(285) = 40755
    result = find_next_tri_pent_hex(start_index + 1)
    print(f"The next triangular number that is also pentagonal and hexagonal is: {result}")