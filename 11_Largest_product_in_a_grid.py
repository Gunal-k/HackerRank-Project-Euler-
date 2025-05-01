grid = []
for grid_i in range(20):
	grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
	grid.append(grid_t)

max_product = 0

for r in range(20):
    for c in range(20):
        # Horizontal (right)
        if c + 3 < 20:
            prod = grid[r][c] * grid[r][c+1] * grid[r][c+2] * grid[r][c+3]
            max_product = max(max_product, prod)
        
        # Vertical (down)
        if r + 3 < 20:
            prod = grid[r][c] * grid[r+1][c] * grid[r+2][c] * grid[r+3][c]
            max_product = max(max_product, prod)
        
        # Diagonal (down-right)
        if r + 3 < 20 and c + 3 < 20:
            prod = grid[r][c] * grid[r+1][c+1] * grid[r+2][c+2] * grid[r+3][c+3]
            max_product = max(max_product, prod)
        
        # Diagonal (down-left)
        if r + 3 < 20 and c - 3 >= 0:
            prod = grid[r][c] * grid[r+1][c-1] * grid[r+2][c-2] * grid[r+3][c-3]
            max_product = max(max_product, prod)

print(max_product)