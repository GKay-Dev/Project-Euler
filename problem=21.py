# Amicable Numbers - https://projecteuler.net/problem=21

def sum_of_proper_divisors(n):
    """Returns the sum of proper divisors of n."""
    divisors_sum = 1  # 1 is a proper divisor of any n > 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum

def find_amicable_numbers(limit):
    amicable_numbers = set()
    for num in range(2, limit):
        partner = sum_of_proper_divisors(num)
        if partner != num and sum_of_proper_divisors(partner) == num:
            amicable_numbers.add(num)
            amicable_numbers.add(partner)
    return amicable_numbers


if __name__ == "__main__":
    limit = 10000
    amicable_numbers = find_amicable_numbers(limit)
    result = sum(amicable_numbers)
    print(f"The sum of all amicable numbers under {limit} is: {result}")