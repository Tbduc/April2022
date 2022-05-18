player1 = '1'
player2 = '2'

already_chosen = []
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
 
def check_user_input(force_valid_input):
        while True:
            user_input = input("Enter a coordinate: ")
            coordinate = (user_input[0].upper(), int(user_input[1]))
            if user_input.isalpha() or user_input.isdigit() or len(user_input) > 2 or len(user_input) < 2:
                print("Enter a correct coordinate.")
            else:
                isLetter = is_correct_letter(user_input[0])
                isNumber = is_number(user_input[1])
                if isLetter is False or isNumber is False:
                    if not force_valid_input:
                        return None
                    print("Enter a correct coordinate.")
                elif coordinate in already_chosen:
                    print("Coordinate already entered.")
                else:
                    return coordinate
 
def get_coordinates():
    coordinates = [("A", 1),("A", 2),("A", 3),("B", 1),("B", 2),("B", 3),("C", 1),("C", 2),("C", 3)]
    coordinate = check_user_input(True)
    
    for element in coordinates:
        if element == coordinate:
            return element
 
def chosen_coordinates(chosen_coordinates, coordinate):
    chosen_coordinates.append(coordinate)
    return chosen_coordinates
 
def movement(new_board):
    player = player_input()
    count = 0
    already_chosen = []
    new_board = get_empty_board()
    while count < 9:
        move = get_coordinates()
        coordinates = [[("A", 1),("A", 2),("A", 3)],[("B", 1),("B", 2),("B", 3)],[("C", 1),("C", 2),("C", 3)]]
        for i, j in zip(new_board, coordinates):
            for index in range(len(new_board)):
                if move == j[index] and isinstance(i[index], str) == False and move not in already_chosen:
                    i[index] = j[index]
                elif j[index] in already_chosen and isinstance(i[index], str) == False and len(already_chosen) > 0:
                    i[index] = j[index]
                if count % 2 == 0:
                    if player[0] == "X" and move == j[index]:
                        i[index] = "X"
                    elif player[0] == "O" and move == j[index]:
                        i[index] = "O"
                else: 
                    if player[1] == "X" and move == j[index]:
                        i[index] = "X"
                    elif player[1] == "O" and move == j[index]:
                        i[index] = "O"
                """if move in already_chosen:
                    print("Coordinate already chosen")
                    break"""
                already_chosen = chosen_coordinates(already_chosen, move)
        count += 1
        display_board(new_board)
    print(player)
 
 
 
 
def player_input():
    player1 = input("Wybierz 'X' albo 'O' ")
    while True:
        if player1.upper() == 'X':
            player2='O'
            print("Wybrales " + player1 + ". Player 2 będzie " + player2)
           
        elif player1.upper() == 'O':
            player2='X'
            print("Wybrales " + player1 + ". Player 2 będzie " + player2)
        
        else:
            player1 = input("Wybierz 'X' albo 'O' ")
        return player1.upper(),player2  
 
        
def get_winning_player(new_board):
    
    pass
 
def display_board(board):
 
    rownumb = 0
    row_list = ("A", "B", "C")
    index = 0
    for row in board:
       
        if index < 1:
            print('   ' + "1" + ' | ' + "2" + ' | ' + "3")
        print(row_list[index] + ' ' + ' ' + row[0] + ' | ' + row[1] + ' | ' + row[2])
        index += 1
 
 
        if rownumb == 0:
            print('----'+('----'*(len(board)-2))+'-----')

def get_winning_player():
    pass
movement()