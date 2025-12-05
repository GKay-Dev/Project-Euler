# Self Powers - https://projecteuler.net/problem=48

def self_powers_last_ten_digits(n):
    total = sum(pow(i, i, 10**10) for i in range(1, n + 1))
    return str(total)[-10:]


if __name__ == "__main__":
    result = self_powers_last_ten_digits(1000)
    print(f"The last ten digits of the series 1^1 + 2^2 + ... + 1000^1000 are: {result}")