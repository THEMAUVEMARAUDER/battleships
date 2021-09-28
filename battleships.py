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
    line = " "
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

def ship_setup(player, ship_grid):
    ships = [[["Ca-1"],["Ca-2"],["Ca-3"],["Ca-4"],["Ca-5"],"Carrier",5],
             [["Ba-1"],["Ba-2"],["Ba-3"],["Ba-4"],"Battleship",4],
             [["De-1"],["De-2"],["De-3"],"Destroyer",3],
             [["Su-1"],["Su-2"],["Su-3"],"Submarine",3],
             [["Pa-1"],["Pa-2"],"Patrol Boat",2]]

    min_x = 0
    max_x = len(ship_grid[0]) - 1
    min_y = 0
    max_y = len(ship_grid) - 1

    print(f"\n{player}'s ship chart:")
    print_grid(ship_grid)

    for ship in ships:
        test1 = False
        test2 = False
        while not (test1 and test2):
            print(f"{player}, select the position and heading of your {ship[-2]}")
            print("x (0-9) then y (0-9) then heading (n/e/s/w), each separated by a space")
            response = input("> ")

            position = response.split()
            pos_x = int(position[0])
            pos_y = int(position[1])
            heading = position[2]

            if ship_grid[pos_y][pos_x] == ["    "]:
                test1 = True
            else:
                print("That space is occupied, try another coordinate.")

            if heading == "n":
                min_y = ship[-1] - 1
            elif heading == "e":
                max_x = 10 - ship[-1]
            elif heading == "s":
                max_y = 10 - ship[-1]
            else:
                min_x = ship[-1] - 1

            if pos_x in range(min_x, (max_x+1)) and pos_y in range(min_y, (max_y+1)):
                test2 = True
                if heading == "n":
                    for n in range(0, len(ship)-2):
                        ship_grid[pos_y - n][pos_x] = ship[n]
                elif heading == "e":
                    for n in range(0, len(ship)-2):
                        ship_grid[pos_y][pos_x + n] = ship[n]
                elif heading == "s":
                    for n in range(0, len(ship)-2):
                        ship_grid[pos_y + n][pos_x] = ship[n]
                else:
                    for n in range(0, len(ship)-2):
                        ship_grid[pos_y][pos_x - n] = ship[n]
            else:
                print(f"A {ship[-2]} ({ship[-1]} spaces) cannot fit there, try another heading or coordinate.")

        print(f"\n{player}'s ship chart:")
        print_grid(ship_grid)

def ship_setup_default():
    pass
    p1_ship_grid = [[["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "]],
                    [["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "]],
                    [["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "]],
                    [["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "]],
                    [["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "]],
                    [["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "]],
                    [["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "]],
                    [["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "]],
                    [["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "]],
                    [["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "]]]


    p2_ship_grid = [[["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "]],
                    [["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "]],
                    [["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "]],
                    [["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "]],
                    [["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "]],
                    [["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "]],
                    [["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "]],
                    [["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "]],
                    [["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "]],
                    [["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "],["    "]]]


def game(play):
    print("1 or 2 player game ?")
    play_type = input("1/2 > ")
    if play_type == "2":
        print("Name of first player ?")
        player1 = input("> ")
        print("Name of second player ?")
        player2 = input("> ")
        ship_setup(player1, p1_ship_grid)
        ship_setup(player2, p2_ship_grid)

        while play:
            shoot(player1, p2_ship_grid, p1_shot_grid)
            win_check(player1, p2_ship_grid)
            shoot(player2, p1_ship_grid, p2_shot_grid)
            win_check(player2, p1_ship_grid)
    else:
        print("Maybe next time :)")
        exit()

def main(play):
    while play:
        print("Play Battleships ?")
        response = input("y/n > ")
        if response == "y":
            print("Great")
            game(True)
        else:
            print("Maybe next time :)")
            exit()



# tests
p1_ship_grid = new_grid(10, 10)
p1_shot_grid = new_grid(10, 10)
p2_ship_grid = new_grid(10, 10)
p2_shot_grid = new_grid(10, 10)
# print(p1_ship_grid)
# print_grid(p1_ship_grid)

# p2_ship_grid = [[["Ca-1"],["Ca-2"],["Ca-3"],["Ca-4"],["Ca-5"]],
#                 [["Ba-1"],["Ba-2"],["Ba-3"],["Ba-4"],["    "]],
#                 [["De-1"],["De-2"],["De-3"],["    "],["    "]],
#                 [["Su-1"],["Su-2"],["Su-3"],["    "],["    "]],
#                 [["Pa-1"],["Pa-2"],["    "],["    "],["    "]]]

# p1_ship_grid = [[["    "],["    "],["    "],["    "],["    "]],
#                 [["    "],["    "],["    "],["    "],["    "]],
#                 [["    "],["    "],["    "],["    "],["    "]],
#                 [["    "],["    "],["    "],["    "],["    "]],
#                 [["Pa-1"],["Pa-2"],["    "],["    "],["    "]]]
#
# p2_ship_grid = [[["    "],["    "],["    "],["    "],["    "]],
#                 [["    "],["    "],["    "],["    "],["    "]],
#                 [["    "],["    "],["    "],["    "],["    "]],
#                 [["    "],["    "],["    "],["    "],["    "]],
#                 [["Pa-1"],["Pa-2"],["    "],["    "],["    "]]]


# print_grid(p2_ship_grid)

main(True)
