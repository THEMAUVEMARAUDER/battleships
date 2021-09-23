
# functions
def new_grid(x, y):
    pass
    grid = [[] for n in range(x)]
    for n in range(len(grid)):
        for m in range(y):
            grid[n].append(["    "])

    return grid

def print_grid(grid):
    line = "  "
    for n in range(len(grid[0])):
        line += f"     {n}    "
    print(line)

    for n in range(len(grid)):
        print(n, grid[n])

def shoot(player, ship_grid, shot_grid):
    print_grid(shot_grid)
    print(f"{player}, enter coordinates for your shot ! (x then y separated by a space)")
    response = input("x y > ")
    shot = response.split()
    if ship_grid[int(shot[0])][int(shot[1])] != ["    "]:
        print("HIT!")
        shot_grid[int(shot[0])][int(shot[1])] = ["HIT!"]
    else:
        print("MISS")
        shot_grid[int(shot[0])][int(shot[1])] = ["MISS"]
    print_grid(shot_grid)

def ai_shoot(ship_grid, shot_grid):
    # set a global variable to record hit/miss and counter to search adjacent to hit
    # check hit/miss to govern aiming behaviour
    # module to search around hits, updating coounter and hit/miss
    # 2 random numbers from a range of the grid length for random shots

    shot = response.split()
    if ship_grid[int(shot[0])][int(shot[1])] != ["    "]:
        print("HIT!")
        shot_grid[int(shot[0])][int(shot[1])] = ["HIT!"]
    else:
        print("MISS")
        shot_grid[int(shot[0])][int(shot[1])] = ["MISS"]
    print_grid(shot_grid)




def game(play):
    while play:
        shoot("player1", p2_ship_grid, p1_shot_grid)
        ai_shoot(p1_ship_grid, p2_shot_grid)
        play = False

def main(play):
    while play:
        print("Play Battleships ?")
        response = input("y/n > ")
        if response == "y":
            print("Great")
            game(True)
        else:
            print("Maybe next time :)")
            play = False



# tests
p1_ship_grid = new_grid(5, 5)
p1_shot_grid = new_grid(5, 5)
#p2_ship_grid = new_grid(10, 10)
p2_shot_grid = new_grid(5, 5)
#print(p1_ship_grid)
#print_grid(p1_ship_grid)

p2_ship_grid = [[["Ca-1"],["Ca-2"],["Ca-3"],["Ca-4"],["Ca-5"]],
                [["Ba-1"],["Ba-2"],["Ba-3"],["Ba-4"],["    "]],
                [["De-1"],["De-2"],["De-3"],["    "],["    "]],
                [["Su-1"],["Su-2"],["Su-3"],["    "],["    "]],
                [["Pa-1"],["Pa-2"],["    "],["    "],["    "]]]


print_grid(p2_ship_grid)

main(True)
