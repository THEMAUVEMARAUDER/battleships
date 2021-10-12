#imports

import random


# functions

def spacer(string):
    spaced_string = f"""
\n
****    ****    ****    ****    ****    ****    ****    ****    ****    ****    ****
\n
        {string}
\n
****    ****    ****    ****    ****    ****    ****    ****    ****    ****    ****
\n"""
    print(spaced_string)

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
        print(n, grid[n], "\n")
    print("\n")

def get_choice(prompt, choices):
    choice = input(prompt)
    while choice not in choices:
        if choice == "quit":
            exit()
        print(f"{choice} is not a valid choice, try again:")
        choice = input(prompt)
    return choice

def shoot_random(ship_grid, shot_grid, shots, counter):
    while True:
        shot_x = random.randint(0,9)
        shot_y = random.randint(0,9)

        if shot_grid[shot_y][shot_x] == ["    "]:
            break
        else:
            continue

        print(f"\nFiring at {shot_x},{shot_y}")

    if ship_grid[int(shot_y)][int(shot_x)] == ["    "]:
        print("MISS")
        shot_grid[int(shot_y)][int(shot_x)] = ["MISS"]
    else:
        print("HIT!")
        shot_grid[int(shot_y)][int(shot_x)] = ["HIT!"]
        ship_grid[int(shot_y)][int(shot_x)] = ["HIT!"]
        counter+=1
    print_grid(shot_grid)

def shoot(player, ship_grid, shot_grid):
    print(f"\n{player}'s firing chart:")
    print_grid(shot_grid)
    print(f"{player}, enter coordinates for your shot ! (x then y separated by a space)")

    while True:
        response = input("x y > ")
        if response == "quit":
            exit()
        try:
            shot = response.split()
            shot_x = int(shot[0])
            shot_y = int(shot[1])
            if shot_grid[shot_y][shot_x] != ["    "]:
                print("This space has already been fired on.")
                raise ValueError("just here to end the try block")
            break
        except:
            print("Invalid input, try again:")
            continue


    if ship_grid[shot_y][shot_x] == ["    "]:
        spacer(f"{player}'s shot is a MISS")
        shot_grid[shot_y][shot_x] = ["MISS"]
    else:
        spacer(f"{player}'s shot is a HIT!")
        shot_grid[shot_y][shot_x] = ["HIT!"]
        ship_grid[shot_y][shot_x] = ["HIT!"]

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
    min_x = 0
    max_x = len(ship_grid[0]) - 1
    min_y = 0
    max_y = len(ship_grid) - 1

    print(f"\n{player}'s ship chart:")
    print_grid(ship_grid)

    for ship in ships:
        test1 = False
        test2 = False

        print(f"{player}, select the position and heading of your {ship[-2]}")
        print("x (0-9) then y (0-9) then heading (n/e/s/w), each separated by a space")

        while not (test1 and test2):
            response = input("x y h > ")
            if response == "quit":
                exit()
            try:
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

            except:
                print("Invalid input, try again.")
                continue

        print(f"\n{player}'s ship chart:")
        print_grid(ship_grid)

def ship_setup_random(ship_grid):
    min_x = 0
    max_x = len(ship_grid[0]) - 1
    min_y = 0
    max_y = len(ship_grid) - 1

    for ship in ships:
        test1 = False
        test2 = False
        while not (test1 and test2):

            headings = ["n","e","s","w"]

            pos_x = random.randint(0, 9)
            pos_y = random.randint(0, 9)
            heading = headings[random.randint(0,3)]

            if ship_grid[pos_y][pos_x] == ["    "]:
                test1 = True

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

def game(play):

    print("1 or 2 player game ?")
    play_type = get_choice("1/2 > ", ["1", "2", "3"])
    if play_type == "2":
        print("Name of first player ?")
        player1 = input("> ")
        print("Name of second player ?")
        player2 = input("> ")

        print("How would you like to place the ships\n1: personally\n2: randomly")
        response = get_choice("1/2 > ", ["1", "2"])
        if response == "1":
            pass
            spacer(f"Avast {player1} ! setup your fleet.")
            ship_setup(player1, p1_ship_grid)
            spacer(f"Avast {player2} ! setup your fleet.")
            ship_setup(player2, p2_ship_grid)
        else:
            ship_setup_random(p1_ship_grid)
            ship_setup_random(p2_ship_grid)

        spacer("LET BATTLE COMMENCE !")
        turn = 0
        while play:
            turn += 1
            print(f"Turn {turn}")
            shoot(player1, p2_ship_grid, p1_shot_grid)
            win_check(player1, p2_ship_grid)
            shoot(player2, p1_ship_grid, p2_shot_grid)
            win_check(player2, p1_ship_grid)

    elif play_type == "1":
        print("Name of first player ?")
        player1 = input("> ")
        player2 = "Captain Computer"

        print("How would you like to place the ships\n1: personally\n2: randomly")
        response = get_choice("1/2 > ", ["1", "2"])
        if response == "1":
            pass
            spacer(f"Avast {player1} ! setup your fleet.")
            ship_setup(player1, p1_ship_grid)
            spacer(f"Avast {player2} ! setup your fleet.")
            ship_setup_random(p2_ship_grid)
        else:
            ship_setup_random(p1_ship_grid)
            ship_setup_random(p2_ship_grid)

        spacer(f"Ahoy thar, here comes the fleet of {player2} looking for trouble")
        spacer("LET BATTLE COMMENCE !")
        turn = 0
        while play:
            turn += 1
            print(f"Turn {turn}")
            shoot(player1, p2_ship_grid, p1_shot_grid)
            win_check(player1, p2_ship_grid)
            shoot_random(p1_ship_grid, p2_shot_grid)
            win_check(player2, p1_ship_grid)

    elif play_type == "3":
        player1 = "Admiral AI"
        player2 = "Captain Computer"
        ship_setup_random(p1_ship_grid)
        ship_setup_random(p2_ship_grid)
        spacer("Exhibition battle mode engaged!")
        turn = 0

        while play:
            turn += 1
            print(f"Turn {turn}")
            shoot_random(p2_ship_grid, p1_shot_grid)
            win_check(player1, p2_ship_grid)
            shoot_random(p1_ship_grid, p2_shot_grid)
            win_check(player2, p1_ship_grid)
    else:
        print("Not sure what you mean :)")
        exit()

def main(play):
    spacer("Welcome to Battleships, the poorly implemented command line edition")
    print("Type quit at any time to exit.")
    while play:
        print("Play Battleships ?")
        response = get_choice("y/n > ", ["y","n"])
        if response == "y":
            print("Great")
            game(True)
        else:
            print("Maybe next time :)")
            exit()


#global variables

ships = [[["Ca-1"],["Ca-2"],["Ca-3"],["Ca-4"],["Ca-5"],"Carrier",5],
         [["Ba-1"],["Ba-2"],["Ba-3"],["Ba-4"],"Battleship",4],
         [["De-1"],["De-2"],["De-3"],"Destroyer",3],
         [["Su-1"],["Su-2"],["Su-3"],"Submarine",3],
         [["Pa-1"],["Pa-2"],"Patrol Boat",2]]

p1_shots = []
p2_shots = []

p1_counter = 0
p2_counter = 0

p1_ship_grid = new_grid(10, 10)
p1_shot_grid = new_grid(10, 10)
p2_ship_grid = new_grid(10, 10)
p2_shot_grid = new_grid(10, 10)


# tests

main(True)
