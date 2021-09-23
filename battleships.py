def new_grid(x, y):
    pass
    grid = [[] for n in range(x)]
    for n in range(len(grid)):
        for m in range(y):
            grid[n].append(["    "])

    return grid

def print_grid(grid):
    for n in range(len(grid)-1, -1, -1):
        print(n, grid[n])
    line = "  "
    for n in range(len(grid[0])):
        line += f"     {n}    "
    print(line)

p1_ship_grid = new_grid(9, 9)
#print(p1_ship_grid)
print_grid(p1_ship_grid)
