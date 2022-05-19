def get_menu_option():
    print("Hello, welcome to game Tic Tac Toe. Have fun! ")

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
    value = int(userInput)
    possible_numbers = [1, 2, 3]
    if value not in possible_numbers:
        return False
    return True

def check_coordinates(already_chosen, current_player):
    error_msg = "Enter correct coordinates."
    while True:
        if current_player == "X":
            user_input = input('Player 1 please enter coordinates: ')
        else:
            user_input = input('Player 2 please enter coordinates: ')
        isLetter = is_correct_letter(user_input[0])
        isNumber = is_number(user_input[1])
        try:
            coordinate = (user_input[0].upper(), int(user_input[1]))
            if coordinate[0].strip().lstrip('-').replace('.', '', 1).isdigit() or len(user_input) > 2:
                print(error_msg)
                continue
            elif isLetter is False or isNumber is False:
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
 
def get_human_coordinates(already_chosen, coordinates, current_player):
    coordinate = check_coordinates(already_chosen, current_player)     
    for row in coordinates:
        for element in row:
            if element == coordinate:
                return element
 
"""def movement(already_chosen, coordinates, current_player, player):
    new_board = [['.','.','.'],['.','.','.'],['.','.','.']]
    move = get_human_coordinates(already_chosen, coordinates, current_player)
    new_board = create_new_board(new_board, move, current_player, player, coordinates, already_chosen)
    display_board(new_board)
    is_board_full(new_board)"""
 
def create_new_board(board, move, current_player, player, coordinates, already_chosen):
    #board = current_board(already_chosen, move, coordinates)
    for row in range(len(coordinates)):
        for index in range(len(board)):
            if move == coordinates[row][index] and len(already_chosen) > 1:
                board[row][index] = coordinates[row][index]
            elif coordinates[row][index] in already_chosen and type(board[row][index]) != str:
                board[row][index] = coordinates[row][index]
            if current_player == "X":
                if player[0] == "X" and move == coordinates[row][index]:
                    board[row][index] = "X"
                elif player[0] == "O" and move == coordinates[row][index]:
                    board[row][index] = "O"
            else:
                if player[1] == "X" and move == coordinates[row][index]:
                    board[row][index] = "X"
                elif player[1] == "O" and move == coordinates[row][index]:
                    board[row][index] = "O"
    return board
 
"""
def current_board(already_chosen, move, coordinates):
    flat_list = [coordinate for row in coordinates for coordinate in row]
    current_board = []
    index = 0
    for i in coordinates:
        current_board.append([])
        for j in range(3):
            current_board[j].append('.')   
            if move in already_chosen and len(already_chosen) > 1:
                while (index < len(flat_list)):
                    if (already_chosen.count(flat_list[index]) > 0):
                        current_board[index][j] = flat_list[index]
                    index += 1
            else:
                current_board[index][j].append(move)           
    return current_board
"""

def player_input():
    player1 = input("Please choose 'X' or 'O' ")
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
 
 
def get_winning_player(board, current_player, players, coordinates, already_chosen):
    winner = None
    move = get_human_coordinates(already_chosen, coordinates, current_player)
    new_board = create_new_board(board, move, current_player, players, coordinates, already_chosen)
    hori = new_board[0][0]==new_board[0][1]==new_board[0][2]!= '.' or new_board[1][0]==new_board[1][1]==new_board[1][2]!='.' or new_board[2][0]==new_board[2][1]==new_board[2][2]!= '.'
    verti = new_board[0][0]==new_board[1][0]==new_board[2][0]!= '.' or new_board[0][1]==new_board[1][1]==new_board[2][1]!= '.' or new_board[0][2]==new_board[1][2]==new_board[2][2]!= '.'
    dia = new_board[0][0]==new_board[1][1]==new_board[2][2]!= '.' or new_board[2][0]==new_board[1][1]==new_board[0][2]!= '.' 
    if hori or verti or dia:
        display_board(board)
        print("%s wins" % current_player)
        winner = current_player
    return winner
 
def display_board(board):
 
    row_list = ("A", "B", "C")
    index = 0
    for row in board:
 
        if index < 1:
            print('   ' + "1" + ' | ' + "2 " + '| ' + "3")
        print(row_list[index] + ' ' + ' ' + row[0] + ' | ' + row[1] + ' | ' + row[2])
        index += 1
 
        print('  ---+'+('---'*(len(board)-2))+'+---')
 
  
def is_board_full(board):
    full = False

    for i in board:
        if "." in i:
            full = False
            break
        else:
            full = True
    if full:
        display_board(board)
        print("Tie")
    return full
 
 
 
def main():
    player1 = ''
    player2 = ''
    already_chosen = []
    round = 0
    coordinates = [[("A", 1),("A", 2),("A", 3)],[("B", 1),("B", 2),("B", 3)],[("C", 1),("C", 2),("C", 3)]]
    
    game_mode = get_menu_option()
    board = get_empty_board()
    players = player_input()
    
    is_game_running = True
    while is_game_running:
        display_board(board)
        if players[0] == "X" and round % 2 == 0:
            current_player = "X"
        else:
            current_player = "O"
        ### TO DO ###
        # in each new iteration of the while loop the program should 
        # alternate the value of `current_player` from `X` to `O`
        
        ### TO DO ###
        # based on the value of the variables `game_mode` and `current_player` 
        # the programm should should choose betwen the functions
        # get_random_ai_coordinates or get_umbeatable_ai_coordinates or get_human_coordinates
        
        #get_coordinates = get_human_coordinates(already_chosen, coordinates)
        
        ### TO DO ###
        # based on the values of `winning_player` and `its_a_tie` the program
        # should either stop displaying a winning/tie message 
        # OR continue the while loop
        winning_player = get_winning_player(board, current_player, players, coordinates, already_chosen)
        its_a_tie = is_board_full(board)
        if winning_player == current_player:
            is_game_running = False
        elif its_a_tie:
            is_game_running = False
        round += 1

if __name__ == '__main__':
    main()

