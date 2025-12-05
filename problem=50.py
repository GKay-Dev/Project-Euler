# Consecutive Prime Sum - https://projecteuler.net/problem=50

from prime import is_prime

def consecutive_prime_sum(limit):
    primes = []
    num = 2
    while len(primes) < limit:
        if is_prime(num):
            primes.append(num)
        num += 1

    max_length = 0
    prime_with_max_length = 0

    for i in range(len(primes)):
        for j in range(i + max_length, len(primes)):
            prime_sum = sum(primes[i:j])
            if prime_sum > 1000000:
                break
            if is_prime(prime_sum):
                current_length = j - i
                if current_length > max_length:
                    max_length = current_length
                    prime_with_max_length = prime_sum

    return prime_with_max_length, max_length


if __name__ == "__main__":
    result, length = consecutive_prime_sum(1000)
    print(f"The prime {result} can be written as the sum of {length} consecutive primes.")