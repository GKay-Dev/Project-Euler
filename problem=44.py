# Pentagon Numbers - https://projecteuler.net/problem=44

def pentagonal(n):
    """Return the nth pentagonal number."""
    return n * (3 * n - 1) // 2

def is_pentagonal(x):
    """Check if x is a pentagonal number."""
    n = (1 + (1 + 24 * x) ** 0.5) / 6
    return n.is_integer()

def find_min_pentagonal_difference():
    """Find the minimum difference of pentagonal numbers Pj and Pk such that both their sum and difference are pentagonal."""
    pentagonals = []
    
    # Generate pentagonal numbers and check pairs
    for k in range(1, 3000):  # Upper limit to prevent infinite loop
        Pk = pentagonal(k)
        pentagonals.append(Pk)
        
        # Check all previous pentagonal numbers
        for j in range(k - 1, 0, -1):
            Pj = pentagonals[j - 1]
            diff = Pk - Pj
            summ = Pk + Pj
            
            # If both sum and difference are pentagonal, we found the answer
            # Since we search in order of increasing k, the first match is minimal
            if is_pentagonal(diff) and is_pentagonal(summ):
                return diff
    
    return None  # No solution found within limit


if __name__ == "__main__":
    result = find_min_pentagonal_difference()
    print(f"The minimum difference of pentagonal numbers Pj and Pk such that both their sum and difference are pentagonal is: {result}")