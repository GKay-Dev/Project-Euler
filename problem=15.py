# Lattice Paths - https://projecteuler.net/problem=15

def lattice_paths(n):
    # Create a 2D array to store the number of paths to each point
    paths = [[0] * (n + 1) for _ in range(n + 1)]
    
    # There is one way to reach any point in the first row or first column
    for i in range(n + 1):
        paths[i][0] = 1
        paths[0][i] = 1
    
    # Fill in the rest of the array
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
    
    return paths[n][n]

if __name__ == "__main__":
    grid_size = 20
    result = lattice_paths(grid_size)
    print(f"The number of lattice paths through a {grid_size}x{grid_size} grid is: {result}")