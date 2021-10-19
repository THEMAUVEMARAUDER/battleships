"""
computer decision making needs to be improved

spacing between results and grid prints needs to be improved for
legibility

comments

???
"""

# imports
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

def get_name(order):
    pass
    print(f"Name of {order} player:")
    name = input("> ")
    return name

def get_choice(prompt, choices):
    choice = input(prompt)
    while choice not in choices:
        if choice == "quit":
            exit()
        print(f"{choice} is not a valid choice, try again:")
        choice = input(prompt)
    return choice

def get_coord():
    correct = False
    print("\nPlease provide coordinate:")
    print(f"x (0-{dim_x-1}) then y (0-{dim_y-1}), each separated by a space")
    while not correct:
        response = input("x y > ")
        if response == "quit":
            exit()
        try:
            position = response.split()
            x = int(position[0])
            y = int(position[1])
            if x in range(dim_x) and y in range(dim_y):
                return x, y
            else:
                continue
        except:
            print(f"\nInvalid entry, please use 0-{dim_x-1} separated by a space.")

def check_empty(grid, x, y, heading, ship):
    if heading == "n":
        for n in range(0, ship[1]):
            if grid[y - n][x] == result[1]:
                return False
    elif heading == "e":
        for n in range(0, ship[1]):
            if grid[y][x + n] == result[1]:
                return False
    elif heading == "s":
        for n in range(0, ship[1]):
            if grid[y + n][x] == result[1]:
                return False
    else:
        for n in range(0, ship[1]):
            if grid[y][x - n] == result[1]:
                return False
    return True

def check_placement(grid, x, y, heading, ship):
    min_x = 0
    max_x = len(grid[0]) - 1
    min_y = 0
    max_y = len(grid) - 1

    if heading == "n":
        min_y = ship[1] - 1
    elif heading == "e":
        max_x = 10 - ship[1]
    elif heading == "s":
        max_y = 10 - ship[1]
    else:
        min_x = ship[1] - 1

    if x in range(min_x, (max_x+1)) and y in range(min_y, (max_y+1)):
        return True
    else:
        return False

def place_ship(grid, x, y, heading, ship):
    if heading == "n":
        for n in range(0, ship[1]):
            grid[y - n][x] = result[1]
    elif heading == "e":
        for n in range(0, ship[1]):
            grid[y][x + n] = result[1]
    elif heading == "s":
        for n in range(0, ship[1]):
            grid[y + n][x] = result[1]
    else:
        for n in range(0, ship[1]):
            grid[y][x - n] = result[1]

def new_grid(x, y):
    pass
    grid = [[] for n in range(x)]
    for n in range(len(grid)):
        for m in range(y):
            grid[n].append(result[0])

    return grid

def print_grid(grid):
    line = " "
    for n in range(len(grid[0])):
        line += f"    {n}   "
    print("\n", line)

    for n in range(len(grid)):
        print(n, grid[n], "\n")
    print("\n")

def print_grid_game(grid):
    game_grid = new_grid(len(grid), len(grid[0]))

    for m in range(len(game_grid)):
        for n in range(len(game_grid)):
            if grid[m][n] != result[1]:
                game_grid[m][n] = grid[m][n]
    print_grid(game_grid)

def ship_setup(player, grid):
    for ship in ships:
        empty = False
        placement = False

        print(f"\n{player}'s ship chart:")
        print_grid(grid)
        print(f"\n{player}, place your {ship[0]} ({ship[1]} spaces long).")

        while not (empty and placement):
            x, y = get_coord()
            print("\nPlease provide heading:")
            heading = get_choice("n/e/s/w > ", ['n','e','s','w'])

            placement = check_placement(grid, x, y, heading, ship)
            if placement:
                empty = check_empty(grid, x, y, heading, ship)
                if not empty:
                    pass
                    print("\nClash with other ship, try again.")
            else:
                pass
                print(f"\nA {ship[0]} ({ship[1]} spaces) cannot fit there, try again.")
                continue

        place_ship(grid, x, y, heading, ship)

def ship_setup_random(grid):
    for ship in ships:
        empty = False
        placement = False

        while not (empty and placement):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            heading = random.choice(['n','e','s','w'])

            placement = check_placement(grid, x, y, heading, ship)
            if placement:
                empty = check_empty(grid, x, y, heading, ship)
            else:
                continue

        place_ship(grid, x, y, heading, ship)

def resolve_shot(player, grid, x, y):
    if grid[y][x] != result[1]:
        spacer(f"{player}, your shot is a MISS")
        grid[y][x] = result[2]
    else:
        spacer(f"{player}, your shot is a HIT!")
        grid[y][x] = result[3]

def check_shot(grid, x, y):
    if grid[y][x] == result[0] or grid[y][x] == result[1]:
        return True
    else:
        return False

def shoot(player, grid):
    print(f"\n{player}'s firing chart:")
    print_grid_game(grid)
    print(f"{player}, take aim at your opponent and OPEN FIRE !")
    while True:
        x, y = get_coord()
        check = check_shot(grid, x, y)
        if check:
            resolve_shot(player, grid, x, y)
            break
        else:
            print("You have already used that coordinate, try again.")
            continue

def get_coord_random(grid):
    x = random.randint(0, dim_x-1)
    y = random.randint(0, dim_y-1)
    return x, y

def shoot_random(player, grid):
    while True:
        x, y = get_coord_random(grid)
        check = check_shot(grid, x, y)
        if check:
            resolve_shot(player, grid, x, y)
            break
        else:
            print(f"{player} is thinking")
            continue

def win_check(player, grid):
    counter = 0
    for n in range(len(grid)):
        for m in range(len(grid)):
            if grid[n][m] != result[1]:
                counter += 1

    if counter == len(grid) * len(grid):
        spacer(f"Congratulations {player}, you have sunk the enemy vessels !")
        exit()

def player_setup(player, grid):
    spacer(f"Avast {player}, prepare your fleet for nautical comabt !.")
    print("How would you like to deploy your fleet ?\n1)personally\n2)randomly")
    choice = get_choice("1/2 > ", ["1", "2"])
    if choice == "1":
        ship_setup(player, grid)
    else:
        ship_setup_random(grid)

def pvp():
    player1 = get_name("First")
    player2 = get_name("Second")

    player_setup(player1, p1_grid)
    player_setup(player2, p2_grid)

    spacer("LET BATTLE COMMENCE !")
    while True:
        shoot(player1, p2_grid)
        win_check(player1, p2_grid)
        shoot(player2, p1_grid)
        win_check(player2, p1_grid)

def pve():
    player1 = get_name("First")
    player2 = "Admiral AI"

    player_setup(player1, p1_grid)
    ship_setup_random(p2_grid)

    spacer(f"Ahoy thar, here comes the fleet of {player2} looking for trouble")
    spacer("LET BATTLE COMMENCE !")
    while True:
        # WIP needs shoot_random to be more complex....
        shoot(player1, p2_grid)
        win_check(player1, p2_grid)
        shoot_random(player2, p1_grid)
        win_check(player2, p1_grid)

def eve():
    player1 = "Captain Computer"
    player2 = "Admiral AI"

    ship_setup_random(p1_grid)
    ship_setup_random(p2_grid)

    while True:
        shoot_random(player1, p2_grid)
        win_check(player1, p2_grid)
        shoot_random(player2, p1_grid)
        win_check(player2, p1_grid)

def main():
    spacer("Welcome to Battleships, the poorly implemented command line edition")
    print("(Type quit at any time to exit.)\n")
    print("Select a game mode:\n\n1)single player.\n2)two player\n")
    choice = get_choice("1/2 > ", ["1", "2", "3"])
    if choice == "1":
        pve()
    elif choice == "2":
        pvp()
    else:
        eve()


# global variables
result = ["~~~~", "SHIP", "MISS", "HIT!"]

ships = [["Aircraft Carrier", 5], ["Battleship", 4], ["Destroyer", 3],
         ["Submarine", 3], ["Patrol Boat", 2]]

dim_x = 10
dim_y = 10

p1_grid = new_grid(dim_x, dim_y)
p2_grid = new_grid(dim_x, dim_y)


# test
main()
