__author__ = 'admin'
import sys

def initialise_board(): #create a 10x10 board
    game_board = []
    opponent_board = []
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    for x in range(len(letters)):
        game_board.append([])
        opponent_board.append([])
        for y in range(1, 11):
            game_board[x].append(str(letters[x])+str(y))
            opponent_board[x].append(str(letters[x])+str(y))

    choose_ships(game_board, opponent_board) #call function to choose ships

def choose_ships(game_board, opponent_board):
    Ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2} #size of each ship
    P1_Ships = [['Carrier', 1], ['Battleship', 1], ['Cruiser', 1], ['Submarine', 1], ['Destroyer', 1]] #number of ships to place
    P2_Ships = [['Carrier', 1], ['Battleship', 1], ['Cruiser', 1], ['Submarine', 1], ['Destroyer', 1]]

    for x in P1_Ships: #place ships
        r = 0

        while x[1] > 0: #check there's ships available
            r += 1
            type = x[0]
            ship_size = Ships[x[0]]
            position = input("Player 1, enter start position of {0}: ".format(x[0])) #choose position (i.e, A1)
            check = place_ship(game_board, ship_size, position, type)
            if check is True:
                x[1] -= 1
            else:
                print("Can't place ship here.")

    for z in P2_Ships: #place ships
        r = 0

        while z[1] > 0: #check there's ships available
            r += 1
            type = z[0]
            ship_size = Ships[z[0]]
            position = input("Player 2, enter start position of {0}: ".format(z[0])) #choose position (i.e, A1)
            check = place_ship(opponent_board, ship_size, position, type)
            if check is True:
                z[1] -= 1
            else:
                print("Can't place ship here.")
    play_game(game_board, opponent_board)

def check_availability(game_board, ship_size, col, row, direction): #check that ship can be placed
    check_ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
    if direction == 'up':
        if row - int(ship_size) >= 0: #check ship within boundaries
            for i in range(0, ship_size):
                if game_board[int(row-i)][int(col)-1] not in check_ships: #check for collision
                    pass
                else:
                    return False
            return True
        else:
            return False
    elif direction == 'down':
        space = row + int(ship_size)
        if space <= 11: #check ship within boundaries
            for i in range(0, ship_size):
                rawr = game_board[int(row+i)][int(col)-1]
                if rawr not in check_ships: #check for collision
                    pass
                else:
                    return False
            return True
        else:
            return False
    elif direction == 'right':
        if col + int(ship_size) <= 11: #check ship within boundaries
            for i in range(0, ship_size):
                if game_board[int(row)][int(col)+i-1] not in check_ships: #check for collision
                    pass
                else:
                    return False
            return True
        else:
            return False
    elif direction == 'left':
        if col - int(ship_size) >= 0: #check ship within boundaries
            for i in range(0, ship_size+1):
                if game_board[int(row)][int(col-1)-i] not in check_ships: #check for collision
                    pass
                else:
                    return False
            return True
        else:
            return False

def place_ship(game_board, ship_size, position, ship_type):
    row = position[0]
    row = ord(row)-65
    if len(position) > 2:
        col = (position[1]+position[2])
    else:
        col = position[1]
    row = int(row)
    col = int(col)



    orientation = int(input("Place ship: \n"
                            "1. Vertically \n"
                            "2. Horizontally")) #horizontal or vertical
    if orientation == 1:
        direction = int(input("Choose direction: \n"
                          "1. Up \n"
                          "2. Down")) #up or down
        if direction == 1:
            result = check_availability(game_board, ship_size, col, row, 'up')
            if result is True:
                for i in range(0, ship_size):
                    game_board[int(row-i)][int(col)-1] = str(ship_type)

            print(game_board)
        else:
            result = check_availability(game_board, ship_size, col, row, 'down')
            if result is True:
                for i in range(0, ship_size):
                    game_board[int(row+i)][int(col)-1] = str(ship_type)

            print(game_board)


    else:
        direction = int(input("Choose direction: \n"
                          "1. Right\n"
                          "2. Left"))
        if direction == 1:
            result = check_availability(game_board, ship_size, col, row, 'right')
            if result is True:
                for i in range(0, ship_size):
                    game_board[int(row)][int(col)+i-1] = str(ship_type)
            print(game_board)

        else:
            result = check_availability(game_board, ship_size, col, row, 'left')
            if result is True:
                for i in range(0, ship_size):
                    game_board[int(row)][int(col)-i-1] = str(ship_type)
            print(game_board)

    return result

def play_game(game_board, opponnent_board):
    print("Player 1 starts.")
    P1_turn = True
    P2_turn = False
    check_ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
    victory = False

    while True:
        if P1_turn:
            while not victory:
                pos = input("Player 1, enter target: ")
                row = pos[0]
                row = ord(row)-65
                if len(pos) > 2:
                    col = (pos[1]+pos[2])
                else:
                    col = pos[1]
                row = int(row)
                col = int(col) - 1
                target = opponnent_board[row][col]
                ship_hit = target
                target = str(ship_hit)
                if target in check_ships:
                    print("Hit")
                else:
                    print("Miss")
                opponnent_board[row][col] = "X"



                destroyed = True
                for y in opponnent_board:
                    if destroyed:
                        for x in y:
                            if x == ship_hit:
                                destroyed = False
                                break
                    else:
                        break

                if destroyed:
                    if target in check_ships:
                        print("{0} DESTROYED.".format(target))

                victory = True
                for y in opponnent_board:
                    if victory:
                        for j in y:
                            if j not in check_ships:
                                victory = True
                            else:
                                victory = False
                                break
                if victory:
                    print("PLAYER 1 WINS")
                    sys.exit()
                P1_turn = False
                P2_turn = True
                break

        elif P2_turn:
            while not victory:
                pos = input("Player 2, enter target: ")
                row = pos[0]
                row = ord(row)-65
                if len(pos) > 2:
                    col = (pos[1]+pos[2])
                else:
                    col = pos[1]
                row = int(row)
                col = int(col) - 1
                target = game_board[row][col]
                ship_hit = target
                target = str(ship_hit)
                if target in check_ships:
                    print("Hit")
                else:
                    print("Miss")
                game_board[row][col] = "X"



                destroyed = True
                for y in game_board:
                    if destroyed:
                        for x in y:
                            if x == ship_hit:
                                destroyed = False
                                break
                    else:
                        break

                if destroyed:
                    if target in check_ships:
                        print("{0} DESTROYED.".format(target))

                victory = True
                for y in game_board:
                    if victory:
                        for j in y:
                            if j not in check_ships:
                                victory = True
                            else:
                                victory = False
                                break
                if victory:
                    print("PLAYER 2 WINS")
                    sys.exit()
                P1_turn = True
                P2_turn = False
                break


initialise_board()