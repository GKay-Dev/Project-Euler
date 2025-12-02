# Longest Collatz Sequence - https://projecteuler.net/problem=14

def collatz_sequence_length(start):
    length = 1
    n = start
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    return length

def longest_collatz_sequence(limit):
    max_length = 0
    starting_number = 0
    for i in range(1, limit):
        length = collatz_sequence_length(i)
        if length > max_length:
            max_length = length
            starting_number = i
    return starting_number

if __name__ == "__main__":
    limit = 1_000_000
    result = longest_collatz_sequence(limit)
    print(f"The starting number under {limit} that produces the longest Collatz sequence is: {result}")