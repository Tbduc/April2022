width =5
height = 5
board =[]
colour = {"MS":'\033[1;32;40m',"ME":'\033[0;37;40m'}
signe = colour["MS"]+"X"+colour["ME"]
mid_h = int((height+2)/2)
mid_w = int((width+2)/2)
initial_coordinates = [mid_h,mid_w]

def board_creation(width, height):
    for i in range(height): 
        board.append([" "] * width)
    for i in board:
        i.insert(0,"")
        i.append("")
    board.insert(0,[""] (width +2))
    board.append([""] (width+2))

def print_board(board):
    for x, y in enumerate(board):
        print(f'{" ".join(y)}')

def player(board, signe):
    board[initial_coordinates[0]][initial_coordinates[1]] = signe
    print_board(board)

board_creation(width, height)
player(board, signe)