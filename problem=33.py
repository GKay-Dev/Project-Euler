# Digit Cancelling Fractions - https://projecteuler.net/problem=33

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def digit_cancelling_fractions():
    numerator_product = 1
    denominator_product = 1

    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):
            num_str = str(numerator)
            den_str = str(denominator)

            # Check for common digits
            common_digits = set(num_str) & set(den_str)
            for digit in common_digits:
                if digit != '0':
                    # Create new numbers by removing the common digit
                    new_num_str = num_str.replace(digit, '', 1)
                    new_den_str = den_str.replace(digit, '', 1)

                    if new_num_str and new_den_str:
                        new_numerator = int(new_num_str)
                        new_denominator = int(new_den_str)

                        # Check if the fractions are equivalent
                        if numerator * new_denominator == denominator * new_numerator:
                            numerator_product *= new_numerator
                            denominator_product *= new_denominator

    # Simplify the final product of fractions
    common_divisor = gcd(numerator_product, denominator_product)
    simplified_denominator = denominator_product // common_divisor

    return simplified_denominator


if __name__ == "__main__":
    result = digit_cancelling_fractions()
    print(f"The denominator of the product of the digit cancelling fractions in lowest terms is: {result}")