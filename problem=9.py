# Special Pythagorean Triplet - https://projecteuler.net/problem=9

def find_special_pythagorean_triplet(sum_total):
    for a in range(1, sum_total):
        for b in range(a + 1, sum_total - a):
            c = sum_total - a - b
            if a * a + b * b == c * c:
                return a, b, c, a * b * c
    return None

if __name__ == "__main__":
    n = 1_000
    triplet = find_special_pythagorean_triplet(n)
    if triplet:
        a, b, c, product = triplet
        print(f"The special Pythagorean triplet is: a={a}, b={b}, c={c}")
        print(f"The product abc is: {product}")
    else:
        print("No special Pythagorean triplet found.")
