# Power Digit Sum - https://projecteuler.net/problem=16

def power_digit_sum(base, exponent):
    number = base ** exponent
    digit_sum = sum(int(digit) for digit in str(number))
    return digit_sum

if __name__ == "__main__":
    base = 2
    exponent = 1000
    result = power_digit_sum(base, exponent)
    print(f"The sum of the digits of {base}^{exponent} is: {result}")