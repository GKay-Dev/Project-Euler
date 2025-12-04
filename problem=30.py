# Digit Fifth Powers - https://projecteuler.net/problem=30

def sum_of_digit_fifth_powers(limit):
    total_sum = 0
    for number in range(10, limit):
        digit_fifth_power_sum = sum(int(digit) ** 5 for digit in str(number))
        if digit_fifth_power_sum == number:
            total_sum += number
    return total_sum


if __name__ == "__main__":
    limit = 6 * (9 ** 5)  # 6 digits is the maximum for fifth powers
    result = sum_of_digit_fifth_powers(limit)
    print(f"The sum of all numbers that can be written as the sum of fifth powers of their digits is: {result}")