table = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"],
]

first_player = True


def main(tab, player):
    game_over = False
    while not game_over:
        print_table(tab)
        get_input(tab, player)
        game_over = check(tab, player)
        player = not player
    if player:
        print('\n\nPlayer 0 won')
    else:
        print('\n\nPlayer X won')


def print_table(tab):
    print("\t 0   1   2\n")
    for i, row in enumerate(tab):
        print(i, end="\t ")
        for x, box in enumerate(row):
            if x != 2:
                print(box, end=" | ")
            else:
                print(box, end="")
        if i != 2:
            print("\n\t-----------")


def get_input(tab, player):
    possibilities = [0, 1, 2, "0", "1", "2"]
    print ('\n')
    if player:
        print('Player: X')
    else:
        print('Player: O')
    
    try:
        pos = input("Insert row and column with a column between. Ex: 1,2\t").split(",")

        if pos[0] not in possibilities or pos[1] not in possibilities:
            print("\nyou can only choose between 0, 1, 2", end="")
            get_input(tab,player)
    except:
        print('\nYou must type two numbers (row,column)')
        get_input(tab, player)

    for i in range(2):
        pos[i] = int(pos[i])

    if tab[pos[0]][pos[1]] == "_":
        if player:
            sign = "X"
        else:
            sign = "O"
        tab[pos[0]][pos[1]] = sign
    else:
        print("\nspot already taken", end="")
        get_input(tab, player)


def check(tab, player):
    # check row
    for i in range(len(tab)):
        if tab[i][0] == tab[i][1] == tab[i][2] != "_":
            print_table(tab)
            return True

    # check column
    for i in range(len(tab)):
        if tab[0][i] == tab[1][i] == tab[2][i] != "_":
            print_table(tab)
            return True

    # check diagonals
    if tab[0][0] == tab[1][1] == tab[2][2] != "_" or tab[0][2] == tab[1][1] == tab[2][0] != "_":
        print_table(tab)
        return True

    # not empty spaces
    not_space = []
    for row in tab:
        if "_" not in row:
            not_space.append(True)
        else:
            not_space.append(False)
    if not_space[0] == not_space[1] == not_space[2] == True:
        print("Pari")
        print_table(tab)
        return True

    return False


main(table, first_player)