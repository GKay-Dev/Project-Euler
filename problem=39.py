# Integer Right Triangles - https://projecteuler.net/problem=39

def count_integer_right_triangles(perimeter_limit):
    perimeter_counts = [0] * (perimeter_limit + 1)

    for a in range(1, perimeter_limit):
        for b in range(a, perimeter_limit):
            c_squared = a * a + b * b
            c = int(c_squared ** 0.5)
            
            # Check if c is an integer and forms a valid triangle
            if c * c == c_squared:
                perimeter = a + b + c
                if perimeter <= perimeter_limit:
                    perimeter_counts[perimeter] += 1

    max_count = max(perimeter_counts)
    max_perimeter = perimeter_counts.index(max_count)

    return max_perimeter, max_count


if __name__ == "__main__":
    limit = 1000
    perimeter, count = count_integer_right_triangles(limit)
    print(f"The perimeter ≤ {limit} that produces the maximum number of integer right triangles is: {perimeter} with {count} solutions.")