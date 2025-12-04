# Coin Sums - https://projecteuler.net/problem=31

def coin_sums(target, coins):
    # Create a list to store the number of ways to make each amount
    ways = [0] * (target + 1)
    ways[0] = 1  # There is one way to make 0 pence

    # Iterate over each coin
    for coin in coins:
        # Update the ways array for each amount from coin to target
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]

    return ways[target]


if __name__ == "__main__":
    target_amount = 200
    coin_denominations = [1, 2, 5, 10, 20, 50, 100, 200]
    result = coin_sums(target_amount, coin_denominations)
    print(f"The number of ways to make £2 using any number of coins is: {result}")