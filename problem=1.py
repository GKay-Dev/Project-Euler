# Multiples of 3 or 5 - https://projecteuler.net/problem=1

def sum_of_multiples_3_5(limit):
    total = sum(number for number in range(limit) if number % 3 == 0 or number % 5 == 0)
    return total

if __name__ == "__main__":
    limit = 1000
    result = sum_of_multiples_3_5(limit)
    print(f"The sum of all multiples of 3 or 5 below {limit} is: {result}")