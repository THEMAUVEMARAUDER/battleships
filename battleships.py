#imports
import random


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
    print("\n", line)

    for n in range(len(grid)):
        print(n, grid[n])
    print("\n")

def shoot(player, ship_grid, shot_grid):
    print(f"\n{player}'s firing chart:")
    print_grid(shot_grid)
    print(f"{player}, enter coordinates for your shot ! (x then y separated by a space)")
    response = input("x y > ")
    shot = response.split()
    shot_x = shot[0]
    shot_y = shot[1]
    if ship_grid[int(shot_y)][int(shot_x)] == ["    "]:
        print("MISS")
        shot_grid[int(shot_y)][int(shot_x)] = ["MISS"]
    else:
        print("HIT!")
        shot_grid[int(shot_y)][int(shot_x)] = ["HIT!"]
        ship_grid[int(shot_y)][int(shot_x)] = ["HIT!"]
    print(f"\n{player}'s firing chart:")
    print_grid(shot_grid)

def win_check(player, ship_grid):
    counter = 0
    for n in range(len(ship_grid)):
        for m in range(len(ship_grid)):
            if ship_grid[n][m] == ["    "] or ship_grid[n][m] == ["HIT!"]:
                counter += 1

    if counter >= (len(ship_grid) * len(ship_grid)):
        print(f"Congratulations {player}, you have sunk all the enemy vessels !")
        exit()

def game(play):
    print("Name of first player ?")
    player1 = input("> ")
    print("Name of second player ?")
    player2 = input("> ")
    while play:
        shoot(player1, p2_ship_grid, p1_shot_grid)
        win_check(player1, p2_ship_grid)
        shoot(player2, p1_ship_grid, p2_shot_grid)
        win_check(player2, p1_ship_grid)

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
# p1_ship_grid = new_grid(5, 5)
p1_shot_grid = new_grid(5, 5)
# p2_ship_grid = new_grid(10, 10)
p2_shot_grid = new_grid(5, 5)
# print(p1_ship_grid)
# print_grid(p1_ship_grid)

# p2_ship_grid = [[["Ca-1"],["Ca-2"],["Ca-3"],["Ca-4"],["Ca-5"]],
#                 [["Ba-1"],["Ba-2"],["Ba-3"],["Ba-4"],["    "]],
#                 [["De-1"],["De-2"],["De-3"],["    "],["    "]],
#                 [["Su-1"],["Su-2"],["Su-3"],["    "],["    "]],
#                 [["Pa-1"],["Pa-2"],["    "],["    "],["    "]]]

p1_ship_grid = [[["    "],["    "],["    "],["    "],["    "]],
                [["    "],["    "],["    "],["    "],["    "]],
                [["    "],["    "],["    "],["    "],["    "]],
                [["    "],["    "],["    "],["    "],["    "]],
                [["Pa-1"],["Pa-2"],["    "],["    "],["    "]]]

p2_ship_grid = [[["    "],["    "],["    "],["    "],["    "]],
                [["    "],["    "],["    "],["    "],["    "]],
                [["    "],["    "],["    "],["    "],["    "]],
                [["    "],["    "],["    "],["    "],["    "]],
                [["Pa-1"],["Pa-2"],["    "],["    "],["    "]]]


# print_grid(p2_ship_grid)

main(True)
