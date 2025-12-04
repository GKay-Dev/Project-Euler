# Number Spiral Diagonals - https://projecteuler.net/problem=28

def sum_spiral_diagonals(n):
    total = 1
    for m in range(3, n + 1, 2):  # m = side length of current square layer
        total += 4 * m * m - 6 * m + 6
    return total


if __name__ == "__main__":
    n = 1001
    result = sum_spiral_diagonals(n)
    print(f"The sum of the numbers on the diagonals in a {n}x{n} spiral is: {result}")