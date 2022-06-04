from random import randint
from re import T
import sys
import os
from tkinter import E
 
board = []
board2 = []
board_guess = []
board_guess2 = []
board_size = 0
round = 0
player = 0
blocks = 0
is_ai = False
already_chosen = []
already_chosen2 = []
small_ship = 1
medium_ship = 2
small_left = 3
medium_left = 2
coordinates = []
temporary_choices = []
map_size = 5
letter_list = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")

def get_menu_option():
    

    print (70 * "-" , "MENU" , 70 * "-")
    print(" ")
    print("---------- BATTLESHIP ---------")
    print(" ")
    option = input("* START GAME ..............[1]\n* MAP SIZE ................[2]\n* IF YOU WANNA EXIT .......[3]\n* ENTER YOUR CHOICE .....[1-3] ")
    print("")
    print(67 * "-")
    while True:
        if option == "1":
            print("You've chosen START GAME")
        elif option == "2":
            player_map_size_menu()
        elif option == "3":
            print("You've chosen EXIT")
            sys.exit()
        else:
            print(" ")
            print("Please choose correct number!")
            option = input("* START GAME ..............[1]\n* MAP SIZE ................[2]\n* IF YOU WANNA EXIT .......[3]\n* ENTER YOUR CHOICE .....[1-3] ")
            print("")
            continue
        return option

def player_map_size_menu():

    print(" ")
    print("---------- BATTLESHIP MAP ---------")
    print(" ")
    print("* MAP 5 = 5x5, MAP 10 = 10x10")
    print(" ")
    map_size = input("* CHOSE MAP SIZE FROM [5] TO [10] ")


    if map_size == "5":
        print(" ")
        print("* SIZE 5 LOAD")
        get_menu_option()
    elif map_size == "6":
        print(" ")
        print("* SIZE 6 LOAD")
        get_menu_option()
    elif map_size == "7":
        print(" ")
        print("* SIZE 7 LOAD")
        get_menu_option()
    elif map_size == "8":
        print(" ")
        print("* SIZE 8 LOAD")
        get_menu_option()
    elif map_size == "9":
        print(" ")
        print("* SIZE 9 LOAD")
        get_menu_option()
    elif map_size == "10":
        print(" ")
        print("* SIZE 10 LOAD")
        get_menu_option()
    else:
        cls()
        print("       INCORECT MAP SIZE !")
        print(" ")
        player_map_size_menu()
    return map_size
 
def get_empty_board(board):
    for i in range(5):
        row = []
        for j in range(5):
            row.append(("0"))
        board.append(row)
    return board
 
def get_empty_board2(board2):
    for i in range(5):
        row = []
        for j in range(5):
            row.append(("0"))
        board2.append(row)
    return board2
 
def get_type_board(board_guess):
    for i in range(5):
        row = []
        for j in range(5):
            row.append(("0"))
        board_guess.append(row)
    return board_guess
 
def get_type_board2(board_guess2):
    for i in range(5):
        row = []
        for j in range(5):
            row.append(("0"))
        board_guess2.append(row)
    return board_guess2
 
def get_coordinates(board, coordinates):
    for i in range(len(board)):
        row = []
        for j in range(len(board)):
            row.append((letter_list[i], j+1))
        coordinates.append(row)
    return coordinates
 
def is_correct_letter(userInput, letter_list):
    entered_letter = userInput[0].upper()
    if entered_letter not in letter_list:
        return False
    return True
 
def is_number(userInput, map_size):
    try:
        value = int(userInput)
    except ValueError:
        return False
    if value > map_size or value < 1:
        return False
    return True
 
def valid_coordinates(coordinates, placement):
    possible_coordinators = []
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            if placement == coordinates[i][j]:
                #conditions for the second block of the medium ship
                if i != 0 and j != 0 and i < (len(coordinates) - 1) and j < (len(coordinates) - 1):
                    possible_coordinators = [coordinates[i+1][j], coordinates[i-1][j], coordinates[i][j+1], coordinates[i][j-1]]
                elif i == 0 and j < (len(coordinates) - 1):
                    possible_coordinators = [coordinates[i+1][j], coordinates[i][j+1]]
                    if j != 0:
                        possible_coordinators.append(coordinates[i][j-1])
                elif j == 0 and i < (len(coordinates) - 1):
                    possible_coordinators = [coordinates[i+1][j], coordinates[i][j+1]]
                    if i != 0:
                        possible_coordinators.append(coordinates[i-1][j])
                elif i == (len(coordinates) - 1) or j == (len(coordinates) - 1):
                    possible_coordinators = [coordinates[i-1][j], coordinates[i][j-1]]
                    if i < (len(coordinates) - 1):
                        possible_coordinators.append(coordinates[i+1][j])
                    elif j < (len(coordinates) - 1):
                        possible_coordinators.append(coordinates[i][j+1])
                elif i == 0 or j == 0:
                    possible_coordinators = [coordinates[i+1][j], coordinates[i][j+1]]
                else: 
                    possible_coordinators = [coordinates[i+1][j], coordinates[i-1][j], coordinates[i][j+1], coordinates[i][j-1]]
    return possible_coordinators
        
 
def check_position(board, coordinates, placement, ship_type, turn):
    
    error_msg = "Ships are too close!"
    for row in range(len(board)):
        for column in range(len(coordinates)):
            if placement == coordinates[row][column]:
                if turn == 1:
                    if row == 0 and column == 0:
                        if board[row+1][column] == "X" or board[row][column+1] == "X":
                            print(error_msg)
                            return False
                    if row == (len(board)-1):
                        if column != 0:
                            if board[row-1][column] == "X" or board[row][column-1] == "X":
                                print(error_msg)
                                return False
                    elif column == (len(board)-1):
                        if row != 0:
                            if board[row-1][column] == "X" or board[row][column-1] == "X":
                                print(error_msg)
                                return False
                    elif board[row+1][column] == "X" or board[row-1][column] == "X":
                        if row != 0:
                            print(error_msg)
                            return False
                    elif board[row][column+1] == "X" or board[row][column-1] == "X":
                        if column != 0:
                            print(error_msg)
                            return False
                elif turn == 2:
                    if row == 0 and column == 0:
                        if board[row+1][column] == "X" or board[row][column+1] == "X":
                            print(error_msg)
                            return False
                    if row == (len(board)-1):
                        if column != 0:
                            if board[row-1][column] == "X" or board[row][column-1] == "X":
                                print(error_msg)
                                return False
                        else:
                            if board[row-1][column] == "X" or board[row][column+1] == "X":
                                print(error_msg)
                                return False
                    elif column == (len(board)-1):
                        if row != 0:
                            if board[row-1][column] == "X" or board[row][column-1] == "X":
                                print(error_msg)
                                return False
                        else:
                            if board[row+1][column] == "X" or board[row][column-1] == "X":
                                print(error_msg)
                                return False
                    elif board[row+1][column] == "X" or board[row-1][column] == "X":
                        if row != 0:
                            print(error_msg)
                            return False
                    elif board[row][column+1] == "X" or board[row][column-1] == "X":
                        if column != 0:
                            print(error_msg)
                            return False                   
    return True
    
def check_coordinates(player, already_chosen, already_chosen2, ship_type):
    global blocks
    error_msg = "Invalid input"
    while True:
        if player == 1:
            user_input = input('Player 1 please choose coordinates to place your ship: ')
        else:
            user_input = input('Player 2 please choose coordinates to place your ship: ')
        if len(user_input) != 2:
            if user_input == "3":
                print("Bye Bye")
                sys.exit()
            else:
                print(error_msg)
                continue
        isLetter = is_correct_letter(user_input[0], letter_list)
        isNumber = is_number(user_input[1], map_size)
        try:
            coordinate = (user_input[0].upper(), int(user_input[1]))
            if isLetter is False or isNumber is False:
                print(error_msg)
                continue
        except:
            print(error_msg)
            continue
        if player == 1 and coordinate not in already_chosen:
            if ship_type == 1:
                already_chosen.append(coordinate)
            else:
                if blocks == 0:
                    blocks += 1
                else:
                    if len(temporary_choices) == 2:
                        already_chosen.append(temporary_choices[0], temporary_choices[1])
        elif player == 2 and coordinate not in already_chosen2:
            if ship_type == 1:
                already_chosen2.append(coordinate)
            else:
                if blocks == 0:
                    blocks += 1
                else:
                    if len(temporary_choices) == 2:
                        already_chosen2.append(temporary_choices[0], temporary_choices[1])
        else:
            print("This coordinate is already occupied!")
            continue
        return coordinate
 
def display_board(board, board2):
 
    row_list = ("A", "B", "C", "D", "E")
    index = 0
 
    for element, element2 in zip(board, board2):
        if index < 1:
            print("   ", end="")
            for item in range(1, 6):
                print(item, end="   ")
            print("      ", end="")
            for item2 in range(1, 6):
                print(item2, end="   ")
            print("\n")
        print(row_list[index], end="  ")
        for i in range(len(board)):
            print(element[i], end="   ")
        print("   ", end="")
        print(row_list[index], end="  ")
        for j in range(len(board2)):
            print(element2[j], end="   ")
        print("\n")
        index += 1
        
def save_status_to_board():
    pass
 
def update_board(board, coordinates, placement, ship_type):
    if placement == None:
        return board
    if ship_type == 1:
        for row in range(len(coordinates)):
            for index in range(len(board)):
                if placement == coordinates[row][index]:
                    board[row][index] = "X"
        return board
    else:
        #saving the placements in temporary choices list
        temporary_choices.append(placement)
        if len(temporary_choices) == 2:
            for row in range(len(coordinates)):
                for index in range(len(board)):
                    if temporary_choices[0] == coordinates[row][index] or temporary_choices[1] == coordinates[row][index]:
                        board[row][index] = "X"
        return board
 
def verify_ship(chosen_ship, ship_type, small_ship, medium_ship):
    global small_left, medium_left
    while True:
        if chosen_ship == "1":
            print("You've chosen a small ship")
            ship_type = small_ship
            small_left -= 1
        elif chosen_ship == "2":
            print("You've chosen a medium ship")
            ship_type = medium_ship
            medium_left -=1
        else:
            print("Please choose correct ship!")
            chosen_ship = input("Please choose the type of ship: 1. Small, 2. Medium: ")
            continue
        return ship_type
    
def get_ship(board, coordinates, player, already_chosen, already_chosen2, small_ship, medium_ship):
    global temporary_choices, round, small_left, medium_left
    ship_type = 0
    turn = 0
    if round % 2 == 1:
        small_left = 3
        medium_left = 2
    index = 0
    print("You have 3 small ships and 2 medium ships.")
 
    while index < 5:
        temporary_choices = []
        if(index > 0):
            print(f"You have {small_left} small ships and {medium_left} medium ships available for placement.")
        if(small_left > 0 and medium_left > 0):
            chosen_ship = input("Please choose the type of ship: 1. Small, 2. Medium: ")
            choice = verify_ship(chosen_ship, ship_type, small_ship, medium_ship)
        elif(small_left == 0):
            chosen_ship = "2"
            choice = verify_ship(chosen_ship, ship_type, small_ship, medium_ship)
        elif(medium_left == 0):
            chosen_ship = "1"
            choice = verify_ship(chosen_ship, ship_type, small_ship, medium_ship)
        #check if ships are placed correctly on the board 
        placement = check_coordinates(player, already_chosen, already_chosen2, choice)
        is_correct_position = False
        while is_correct_position == False:
            if placement == None:
                break
            if choice == 1:
                turn = 1
                is_correct_position = check_position(board, coordinates, placement, choice, turn)
                if is_correct_position == False:
                    if player == 1:
                        already_chosen.pop()
                    elif player == 2:
                        already_chosen2.pop()
                    placement = check_coordinates(player, already_chosen, already_chosen2, choice)
                    continue
            elif choice == 2:
                turn = 1
                while turn <= 2:
                    if turn == 1:
                        are_valid_coords = valid_coordinates(coordinates, placement)
                        is_correct_position = check_position(board, coordinates, placement, choice, turn)
                        if is_correct_position == True:
                            update_board(board, coordinates, placement, choice)
                            turn += 1
                        else:
                            placement = check_coordinates(player, already_chosen, already_chosen2, choice)
                        continue
                    placement = check_coordinates(player, already_chosen, already_chosen2, choice)
                    if placement not in are_valid_coords:
                        print("These coordinates are not valid.")
                        coords = str(are_valid_coords).strip('[]')
                        print("Correct coordinates are: " + coords)
                        continue
                    is_correct_position = check_position(board, coordinates, placement, choice, turn)
                    if is_correct_position == False:
                        turn = 1
                        print("Please place the ship again from the first block.")
                        placement = check_coordinates(player, already_chosen, already_chosen2, choice)
                        temporary_choices = []
                        continue
                    turn += 1
            if player == 1:
                update_board(board, coordinates, placement, choice)
            else:
                update_board(board2, coordinates, placement, choice)
            display_board(board, board2)
        index += 1
    return board



def player_turn(round, player):
    if round % 2 == 0:
        player = 1
    else:
        player = 2
    return player
 
def hit_miss(board):
 
    # M = Missed
    # 0 = Undiscovered
    # H = Hit part ship
    # S = Sunk ship
    
    data = []
    
    for data in board:
        for board in data:
            if board == "M":
                print("Miss")
            elif board == "0":
                print("Undiscovered")
            elif board == "H":
                print("Hit")
            elif board == "S":
                print("Sunk ship")
        return data
 
def player_display():
    cls()
    player = input("Press any key to start")
    
 
def cls():
    os.system('cls' if os.name=='nt' else 'clear') 
 
get_empty_board(board)
get_empty_board2(board2)
get_coordinates(board, coordinates)  
display_board(board, board2) # only for check
player = 1
get_ship(board, coordinates, player, already_chosen, already_chosen2, small_ship, medium_ship)
round += 1
player = 2
get_ship(board2, coordinates, player, already_chosen, already_chosen2, small_ship, medium_ship)