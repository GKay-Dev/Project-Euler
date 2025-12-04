# Non-Abundant Sums - https://projecteuler.net/problem=23

def is_abundant(n):
    """Check if a number is abundant."""
    divisors_sum = sum(i for i in range(1, n // 2 + 1) if n % i == 0)
    return divisors_sum > n

def abundant_numbers_up_to(limit):
    """Generate a list of abundant numbers up to a given limit."""
    return [n for n in range(1, limit + 1) if is_abundant(n)]

def non_abundant_sums(limit):
    """Calculate the sum of all positive integers which cannot be written as the sum of two abundant numbers."""
    abundant_nums = abundant_numbers_up_to(limit)
    can_be_written_as_abundant_sum = [False] * (limit + 1)

    for i in range(len(abundant_nums)):
        for j in range(i, len(abundant_nums)):
            abundant_sum = abundant_nums[i] + abundant_nums[j]
            if abundant_sum <= limit:
                can_be_written_as_abundant_sum[abundant_sum] = True
            else:
                break

    return sum(n for n in range(1, limit + 1) if not can_be_written_as_abundant_sum[n])


if __name__ == "__main__":
    limit = 28123
    result = non_abundant_sums(limit)
    print(f"The sum of all positive integers which cannot be written as the sum of two abundant numbers is: {result}")