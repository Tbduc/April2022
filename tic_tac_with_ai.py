import random
import os
import sys
 
def get_menu_option():
    print (30 * "-" , "MENU" , 30 * "-")
    print(" ")
    print("---------- Hello, welcome to game Tic Tac Toe. Have fun! ---------")
    print(" ")
    option = input("* Player vs Player ........[1]\n* Player vs AI ............[2]\n* If you wanna exit .......[3]\n* Enter your choice .....[1-3] ")
    print("")
    print(67 * "-")
    while True:
        if option == "1":
            print("You've chosen Player vs Player")
        elif option == "2":
            print("You've chosen Player vs AI")
        elif option == "3":
            print("Bye Bye")
            sys.exit()
        else:
            print(" ")
            print("Please choose correct number!")
            option = input("* Player vs Player ........[1]\n* Player vs AI ............[2]\n* If you wanna exit .......[3]\n* Enter your choice .....[1-3] ")
            print("")
            continue
        return option
 
def player_input():
    player1 = input("Please choose 'X' or 'O' ")

    if player1 == "3":
            print("Bye Bye")
            sys.exit()

    while True:
        if player1.upper() == 'X':
            player2='O'
            print("Your choice is:  " + player1.upper() + ". Player 2 is " + player2.upper())
        elif player1.upper() == 'O':
            player2='X'
            print("Your choice is: " + player1.upper() + ". Player 2 is " + player2.upper())
        else:
            player1 = input("Please choice 'X' or 'O' ")
            continue
        return player1.upper(),player2.upper() 
 
 
def get_empty_board():
    start_board = []
 
    for i in range(3):
        row = []
        for j in range(3):
            row.append('.')
        start_board.append(row)
    return start_board
 
def is_correct_letter(userInput):
    possible_letters = ["A", "B", "C"]
    entered_letter = userInput[0].upper()
    if entered_letter not in possible_letters:
        return False
    return True
 
def is_number(userInput):
    try:
        value = int(userInput)
    except ValueError:
        return False
    possible_numbers = [1, 2, 3]
    if value not in possible_numbers:
        return False
    return True
 
def check_coordinates(already_chosen, round, is_ai):
    error_msg = "Enter correct coordinates."
    while True:
        
        if round % 2 == 0 or is_ai:
            user_input = input('Player 1 please enter coordinates: ')
        else:
            user_input = input('Player 2 please enter coordinates: ')
        if len(user_input) != 2:
            if user_input == "3":
                print("Bye Bye")
                sys.exit()
            else:
                print(error_msg)
                continue
        isLetter = is_correct_letter(user_input[0])
        isNumber = is_number(user_input[1])
        try:
            coordinate = (user_input[0].upper(), int(user_input[1]))
            if isLetter is False or isNumber is False:
                print(error_msg)
                continue
        except:
            print(error_msg)
            continue
        if coordinate not in already_chosen:
            already_chosen.append(coordinate)
        else:
            print("This coordinate is already occupied!")
            continue
        return coordinate
 
def get_human_coordinates(already_chosen, round, is_ai):
    is_ai = False
    coordinate = check_coordinates(already_chosen, round, is_ai)
    return coordinate
 
def create_new_board(board, move, current_player, coordinates):
    for row in range(len(coordinates)):
        for index in range(len(board)):
            if current_player == "X":
                if move == coordinates[row][index]:
                    board[row][index] = "X"
            else:
                if move == coordinates[row][index]:
                    board[row][index] = "O"
    return board 
 
 
def get_winning_player(board, current_player, players, coordinates, already_chosen, round, is_ai, game_mode):
    winner = None
    if round % 2 == 0 or game_mode == "1":
        move = get_human_coordinates(already_chosen, round, is_ai)
    else:
        move = get_random_ai_coordinates(board, players, coordinates, current_player, round, already_chosen)
    new_board = create_new_board(board, move, current_player, coordinates)
    
    hori = new_board[0][0]==new_board[0][1]==new_board[0][2]!= '.' or new_board[1][0]==new_board[1][1]==new_board[1][2]!='.' or new_board[2][0]==new_board[2][1]==new_board[2][2]!= '.'
    verti = new_board[0][0]==new_board[1][0]==new_board[2][0]!= '.' or new_board[0][1]==new_board[1][1]==new_board[2][1]!= '.' or new_board[0][2]==new_board[1][2]==new_board[2][2]!= '.'
    dia = new_board[0][0]==new_board[1][1]==new_board[2][2]!= '.' or new_board[2][0]==new_board[1][1]==new_board[0][2]!= '.' 
    if hori or verti or dia:
        display_board(board)
        print("%s has won!" % current_player)
        winner = current_player
    return winner

def is_winner(board, current_player):
    
    return ((board[0][0] == current_player and board[0][1] == current_player and board[0][2] == current_player) or # across the top
    (board[1][0] == current_player and board[1][1] == current_player and board[1][2] == current_player) or # across the middle
    (board[2][0] == current_player and board[2][1] == current_player and board[2][2] == current_player) or # across the bottom
    (board[0][0] == current_player and board[1][0] == current_player and board[2][0] == current_player) or # down the left side
    (board[0][1] == current_player and board[1][1] == current_player and board[2][1] == current_player) or # down the middle
    (board[0][2] == current_player and board[1][2] == current_player and board[2][2] == current_player) or # down the right side
    (board[0][0] == current_player and board[1][1] == current_player and board[2][2] == current_player) or # diagonal
    (board[0][2] == current_player and board[1][1] == current_player and board[2][0] == current_player)) # diagonal

def display_board(board):
    row_list = ("A", "B", "C")
    index = 0
    for row in board:
        if index < 1:
            print('   ' + "1" + ' | ' + "2 " + '| ' + "3")
        print(row_list[index] + ' ' + ' ' + row[0] + ' | ' + row[1] + ' | ' + row[2])
        index += 1
        print('  ---+'+('---'*(len(board)-2))+'+---')
 
def is_board_full(board, winning_player, current_player):
    full = False
 
    for i in board:
        if "." in i:
            full = False
            break
        else:
            full = True
    if full and winning_player != current_player:
        cls()
        display_board(board)
        print("It's a tie!")
    return full

def copy_current_board(board):
    copied_board = []
    
    for i in board:
        row = []
        for value in i:
            row.append(value)
        copied_board.append(row)
        
    return copied_board

def choose_random_move(board, coordinates):
    possible_moves = []
    for row in range(3):
        for index in range(3):
            if board[row][index] == ".":
                possible_moves.append(coordinates[row][index])
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None

def predicted_move(copied_board, coordinates, current_player, already_chosen, row, index):
    if coordinates[row][index] not in already_chosen:
        copied_board[row][index] = current_player
    
def get_random_ai_coordinates(board, players, coordinates, current_player, round, already_chosen):
    is_ai = True
    
    if current_player == players[0]:
        if round % 2 == 0:
            coordinate = check_coordinates(already_chosen, round, is_ai)
            current_player = players[0]
            return coordinate
        else:
            current_player = players[1]
    else:
        # Check if AI can win in the next move    
        for row in range(3):
            for index in range(3):
                copied_board = copy_current_board(board)
                if copied_board[row][index] == ".":
                    predicted_move(copied_board, coordinates, current_player, already_chosen, row, index)
                    if is_winner(copied_board, current_player):
                        already_chosen.append(coordinates[row][index])
                        return coordinates[row][index]
                    
        # Check if player 1 can win in the next move    
        for row in range(3):
            for index in range(3):
                copied_board = copy_current_board(board)
                if copied_board[row][index] == ".":
                    predicted_move(copied_board, coordinates, players[0], already_chosen, row, index)
                    if is_winner(copied_board, players[0]):
                        already_chosen.append(coordinates[row][index])
                        return coordinates[row][index]
                    
        move = choose_random_move(board, coordinates)
        if move != None:
            return move
        
        if coordinates[1][1] not in already_chosen:
            already_chosen.append(coordinates[1][1])
            return coordinates[1][1]
        
        return choose_random_move(board, coordinates)


def cls():
    os.system('cls' if os.name=='nt' else 'clear') 
        
 
def main():
    already_chosen = []
    round = 0
    coordinates = [[("A", 1),("A", 2),("A", 3)],[("B", 1),("B", 2),("B", 3)],[("C", 1),("C", 2),("C", 3)]]
    is_ai = False
    game_mode = get_menu_option()
    board = get_empty_board()
    players = player_input()
    
    is_game_running = True
    while is_game_running:
        cls()
        display_board(board)
        if game_mode == "1" or round % 2 == 0:
            is_ai = False
        if players[0] == "X":
            if round % 2 == 0:
                current_player = "X"
            else:
                current_player = "O"
        else:
            if round % 2 == 0:
                current_player = "O"
            else:
                current_player = "X"        
        winning_player = get_winning_player(board, current_player, players, coordinates, already_chosen, round, is_ai, game_mode)
        its_a_tie = is_board_full(board, winning_player, current_player)
        if winning_player == current_player:
            is_game_running = False
        elif its_a_tie:
            is_game_running = False
        round += 1
if __name__ == '__main__':
    main()