"""
incorporate get_grid into methods...
if this is possible?

resolve_shot should use player not grid to add to hit list

spacing between results and grid prints needs to be improved for
legibility

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
    choice = choice.lower()
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
        grid[y][x] = result[2]
        spacer(f"{player}, your shot is a MISS")
        print_grid_game(grid)
    else:
        grid[y][x] = result[3]
        spacer(f"{player}, your shot is a HIT!")
        print_grid_game(grid)

        # shortcut to add to hits without an extra argument...
        if grid == grid_p1:
            hits_p2.append([x, y])
        else:
            hits_p1.append([x, y])

def shoot(player, grid):
    spacer(f"\n{player}'s firing chart:")
    print_grid_game(grid)
    spacer(f"{player}, take aim at your opponent and OPEN FIRE !")
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

# takes player and returns players grid
def get_grid(player):
    if player == player1:
        return grid_p1
    else:
        return grid_p2

def get_hits(player):
    if player == player1:
        hits = hits_p1
    else:
        hits = hits_p2
    return hits

def get_last_hit(player):
    hits = get_hits(player)
    x = hits[-1][0]
    y = hits[-1][1]

    return x, y

# takes player and returns opposing players grid
def get_grid_opp(player):
    if player == player1:
        return grid_p2
    else:
        return grid_p1

def get_coord_window(player, grid):
    hits = get_hits(player)
    if len(hits) < 1:
        return False, None, None

    print("!! Window mode !!")

    x1, y1 = get_last_hit(player)
    possible_coords = []
    # range max is +2 as range is not inclusive of specified max...
    for y2 in range(y1 - 1, y1 + 2):
        for x2 in range(x1 - 1, x1 + 2):
            adjacent = check_adjacent(x1, y1, x2, y2)
            inrange = check_inrange_coord(x2, y2)

            if adjacent and inrange:
                empty = check_shot(grid, x2, y2)

                if empty:
                    possible_coords.append([x2, y2])

    if len(possible_coords) == 0:
        return False, None, None
    else:
        shot = random.choice(possible_coords)

    return True, shot[0], shot[1]


def check_shot(grid, x, y):
    if grid[y][x] == result[0] or grid[y][x] == result[1]:
        return True
    else:
        return False

def check_adjacent(x1, y1, x2, y2):
    if abs(x2 - x1) + abs(y2 - y1) > 1:
        return False
    else:
        return True

def check_inrange_coord(x, y):
    if x > 9 or x < 1:
        return False
    elif y > 9 or y < 1:
        return False
    else:
        return True

def check_inrange_list(coords):
    for i in range(len(coords)):
        for j in range(2):
            if coords[i][j] > 9:
                coords[i][j] = 9
            elif coords[i][j] < 0:
                coords[i][j] = 0
            else:
                pass
    return coords

def get_coord_axis(player):
    hits = get_hits(player)
    if len(hits) < 2:
        return False, None, None

    for m in range(len(hits)-1,0,-1):
        for n in range(m-1,-1,-1):
            possible_coords = []
            x1 = hits[m][0]
            y1 = hits[m][1]
            x2 = hits[n][0]
            y2 = hits[n][1]

            delta_x = x2 - x1
            delta_y = y2 - y1

            adjacent = check_adjacent(x1, y1, x2, y2)

            if not adjacent:
                continue

            elif delta_x > 0:
                possible_coords.append([x1 - 1, y1])
                possible_coords.append([x2 + 1, y2])
            elif delta_x < 0:
                possible_coords.append([x1 + 1, y1])
                possible_coords.append([x2 - 1, y2])
            elif delta_y > 0:
                possible_coords.append([x1, y1 - 1])
                possible_coords.append([x2, y2 + 1])
            else:
                possible_coords.append([x1, y1 + 1])
                possible_coords.append([x2, y2 - 1])

            possible_coords = check_inrange_list(possible_coords)

            grid = get_grid_opp(player)

            check1 = check_shot(grid, possible_coords[0][0], possible_coords[0][1])
            check2 = check_shot(grid, possible_coords[1][0], possible_coords[1][1])

            if check1:
                return True, possible_coords[0][0], possible_coords[0][1]
            elif check2:
                return True, possible_coords[1][0], possible_coords[1][1]
            else:
                continue

    return False, None, None

def shoot_random(player, grid):
    while True:
        x, y = get_coord_random(grid)
        check = check_shot(grid, x, y)
        if check:
            resolve_shot(player, grid, x, y)
            break
        else:
            continue

# WIP ...
def shoot_ai(player, grid):
    success, x, y = get_coord_axis(player)
    if success:
        resolve_shot(player, grid, x, y)
    else:
        # success = False indicates no possible shots around last hit...
        success, x, y = get_coord_window(player, grid)
        if success:
            resolve_shot(player, grid, x, y)
        else:
            shoot_random(player, grid)

def win_check(player, grid):
    counter = 0
    for n in range(len(grid)):
        for m in range(len(grid)):
            if grid[n][m] != result[1]:
                counter += 1

    if counter == len(grid) * len(grid):
        turns(grid)
        spacer(f"Congratulations {player}, you have sunk the enemy vessels !")
        exit()

def turns(grid):
    pass
    counter = 0
    for n in range(len(grid)):
        for m in range(len(grid)):
            if grid[n][m] == result[2] or grid[n][m] == result[3]:
                counter += 1
    print(counter, "turns have elapsed.")


def player_setup(player, grid):
    spacer(f"Avast {player}, prepare your fleet for nautical comabt !.")
    print("How would you like to deploy your fleet ?\n1)personally\n2)randomly")
    choice = get_choice("1/2 > ", ["1", "2"])
    if choice == "1":
        ship_setup(player, grid)
    else:
        ship_setup_random(grid)

def pvp():
    global player1, player2
    player1 = get_name("First")
    player2 = get_name("Second")

    player_setup(player1, grid_p1)
    player_setup(player2, grid_p2)

    spacer("LET BATTLE COMMENCE !")
    while True:
        shoot(player1, grid_p2)
        win_check(player1, grid_p2)
        shoot(player2, grid_p1)
        win_check(player2, grid_p1)

def pve():
    global player1, player2
    player1 = get_name("First")
    player2 = "Admiral AI"

    player_setup(player1, grid_p1)
    ship_setup_random(grid_p2)

    spacer(f"Ahoy thar, here comes the fleet of {player2} looking for trouble")
    spacer("LET BATTLE COMMENCE !")
    while True:
        # WIP needs shoot_random to be more complex....
        shoot(player1, grid_p2)
        win_check(player1, grid_p2)
        shoot_ai(player2, grid_p1)
        win_check(player2, grid_p1)

# WIP ...
# insert shoot_ai in here and begin testing !
def eve():
    global player1, player2
    player1 = "Captain Computer"
    player2 = "Admiral AI"

    ship_setup_random(grid_p1)
    ship_setup_random(grid_p2)

    while True:
        shoot_ai(player1, grid_p2)
        win_check(player1, grid_p2)
        shoot_ai(player2, grid_p1)
        win_check(player2, grid_p1)

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


hits_p1 = []
hits_p2 = []

grid_p1 = new_grid(dim_x, dim_y)
grid_p2 = new_grid(dim_x, dim_y)


# test
test_grid = [["SHIP","~~~~","MISS","HIT!"],
             ["~~~~","SHIP","MISS","~~~~"],
             ["~~~~","HIT!","~~~~","~~~~"],
             ["MISS","~~~~","~~~~","HIT!"]]

# print_grid(test_grid)
# print_grid_game(test_grid)

# ship_setup("player1", grid_p1)

# x, y = get_coord(test_grid)
# print(x, y)
# ship_setup_random(grid_p1)
# ship_setup("player1",grid_p1)


main()
