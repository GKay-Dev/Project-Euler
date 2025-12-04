# Champernowne's Constant - https://projecteuler.net/problem=40

def champernowne_digit(n):
    """Return the nth digit of Champernowne's constant."""
    digit_length = 1
    count = 9
    start = 1

    # Find the range in which the nth digit lies
    while n > digit_length * count:
        n -= digit_length * count
        digit_length += 1
        count *= 10
        start *= 10

    # Find the actual number that contains the nth digit
    number = start + (n - 1) // digit_length
    digit_index = (n - 1) % digit_length

    return int(str(number)[digit_index])


if __name__ == "__main__":
    positions = [1, 10, 100, 1000, 10000, 100000, 1000000]
    product = 1
    for pos in positions:
        product *= champernowne_digit(pos)
    print(f"The product of the digits at the specified positions is: {product}")