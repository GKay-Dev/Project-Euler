# Reciprocal Cycles - https://projecteuler.net/problem=26

def reciprocal_cycle_length(d):
    """Returns the length of the recurring cycle in the decimal representation of 1/d."""
    remainders = {}
    value = 1
    position = 0

    while value != 0:
        if value in remainders:
            return position - remainders[value]
        remainders[value] = position
        value *= 10
        value %= d
        position += 1

    return 0

def find_longest_reciprocal_cycle(limit):
    """Finds the value of d < limit for which 1/d contains the longest recurring cycle."""
    max_length = 0
    result = 0

    for d in range(2, limit):
        cycle_length = reciprocal_cycle_length(d)
        if cycle_length > max_length:
            max_length = cycle_length
            result = d

    return result


if __name__ == "__main__":
    limit = 1000
    answer = find_longest_reciprocal_cycle(limit)
    print(f"The value of d < {limit} for which 1/d contains the longest recurring cycle is: {answer}")
    