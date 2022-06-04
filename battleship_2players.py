from re import I


board = []
board2 = []
 
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
 
 
def display_board(board, board2):
 
    board = get_empty_board(board)
    board2 = get_empty_board2(board2)
    
 
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
        #print('  '+(''*(len(board)-2))+'')
 
 
    # #result = "\n".join("{} {} {} {}".format(a, x, b, y) for a, x, b, y in zip(row_list, board, row_list, board2))
    # print(result)
 
def check_position(board, coordinates, placement, ship_type):
    for i in range(len(board)):
        for j in range(len(coordinates)):
            if placement == coordinates[i][j]:
                if board[i][j] != "0":
                    return False
                if ship_type == 1:
                    if board[i+1][j] == "X" or board[i-1][j] == "X":
                        return False
                    elif board[i][j+1] == "X" or board[i][j-1] == "X":
                        return False
                else:
                    if ship_type == 2:
                        if i == 0 or j == 0:
                            if board[i+1][j] == "0" or board[i][j+1] == "0":
                                return True
                            elif i != (len(board)-1):
                                if j != (len(board)-1):
                                    if board[i+1][j] == "X" or board[i][j+1] == "X":
                                        return True
                            else:
                                continue
                        elif i == (len(board)-1) or j == (len(board)-1):
                            if board[i-1][j] == "X" or board[i][j-1] == "X":
                                return False
                            else:
                                continue
                        else:
                            if board[i+1][j] == "X" or board[i-1][j] == "X" or board[i][j+1] == "X" or board[i][j-1] == "X":
                                if board[i+1][j] != "X" or board[i-1][j] != "X" or board[i][j+1] != "X" or board[i][j-1] != "X":
                                    return True
                                else:
                                    return False
            else:
                continue
                                   
    return True    
 
display_board(board, board2)
