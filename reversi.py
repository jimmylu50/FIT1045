from copy import copy
board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'W', 'B', ' ', ' ', ' '],
        [' ', ' ', ' ', 'B', 'W', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
complete_board = [[],
                  [],
                  [],
                  [],
                  [],
                  [],
                  [],
                  []]
copy_board = []
letter_board = [' ' , 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
def new_board():
    board = []
    for i in range(8):
        board.append([' '] * 8)
        
    return board

def print_board2(board):
    complete_board.clear()
    for i in range(8):
        complete_board.append([])
    for i in range(8):
        complete_board[i].append(i+1)
        for j in range(8):
            complete_board[i].append(board[i][j])
    complete_board.append(letter_board)
    
    for x in complete_board:
        print(*x, sep = ' | ')
    return complete_board

print_board2(board)

def score(board):
    black_pieces = 0
    white_pieces = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'B':
                black_pieces += 1
            elif board[i][j] == 'W':
                white_pieces += 1
    print("The number of black pieces is: " + str(black_pieces))
    print("The number of white pieces is: " + str(white_pieces))

score(board)

#question = input("1 player or 2 players?")  
player = ['W','B']
pos = () #input("What position would you like to place your piece? ")
direct = [[0,1],[1,0],[-1,0],[0,-1],[-1,-1],[-1,1],[1,1],[1,-1]]
letter = 'abcdefgh'
copy_board = copy(board)

def enclosing_white(board, player, direct):
    down = 0
    right = 0
    top = 0
    left = 0
    count = 0
    for j in range(8):
        for i in range(8):
            if copy_board[j][i] == player[0]:
                up = int(j)
                left = int(i)
                down = int(7-j)
                right = int(7-i)
                top_left = min(up, left)
                top_right = min(up, right)
                bottom_left = min(down, left)
                bottom_right = min(down, right)
                for k in range(1, up):
                    if copy_board[j-k][i]==player[0]:
                        for m in range(1, k):
                            if copy_board[j-m][i] == player[1]:
                                count += 1
                                if count == k-1:
                                    return True
                                    count = 0 
                                else:
                                    return False
                                    count = 0
                                    
                for k in range(2, down):
                    if copy_board[j+k][i]==player[0]:
                        for m in range(1, k-1):
                            if copy_board[j+m][i] == player[1]:
                                count += 1
                                m += 1
                                if count == k-1:
                                    count = 0
                                    return True
                                else:
                                    return False
                                    count = 0
                for k in range(1, left):
                    if copy_board[j][i-k]==player[0]:
                        for m in range(1, k):
                            if copy_board[j][i-m] == player[1]:
                                count += 1
                                if count == k-1:
                                    count = 0
                                    return True
                                else:
                                    return False
                                    count = 0
                for k in range(2, right):
                    if copy_board[j][i+k]==player[0]:
                        for m in range(1, k-1):
                            if copy_board[j][i+m] == player[1]:
                                count += 1
                                if count == k-1:
                                    count = 0
                                    return True
                                else:
                                    return False
                                    count = 0
                for k in range(1, top_left):
                    if copy_board[j-k][i-k]==player[0]:
                        for m in range(1, k):
                            if copy_board[j-m][i-m] == player[1]:
                                count += 1
                                if count == k-1: 
                                    count = 0
                                    return True
                                else:
                                    return False
                                    count = 0
                for k in range(1, top_right):
                    if copy_board[j-k][i+k]==player[0]:
                        for m in range(1, k):
                            if copy_board[j-m][i+m] == player[1]:
                                count += 1
                                if count == k-1: 
                                    count = 0
                                    return True
                                else:
                                    return False
                                    count = 0
                for k in range(1, bottom_left):
                    if copy_board[j+k][i-k]==player[0]:
                        for m in range(1, k):
                            if copy_board[j+m][i-m] == player[1]:
                                count += 1
                                if count == k-1: 
                                    count = 0
                                    return True
                                else:
                                    return False
                                    count = 0
                for k in range(1, bottom_right):
                    if copy_board[j+k][i+k]==player[0]:
                        for m in range(1, k):
                            if copy_board[j+m][i+m] == player[1]:
                                count += 1
                                if count == k-1: 
                                    count = 0
                                    return True
                                else:
                                    return False
                                    count = 0
                        
def enclosing_black(board, player, direct):
    down = 0
    right = 0
    top = 0
    left = 0
    count = 0
    for j in range(8):
        for i in range(8):
            if copy_board[j][i] == player[1]:
                up = int(j)
                left = int(i)
                down = int(7-j)
                right = int(7-i)
                top_left = min(up, left)
                top_right = min(up, right)
                bottom_left = min(down, left)
                bottom_right = min(down, right)
                for k in range(1, up):
                    if copy_board[j-k][i]==player[1]:
                        for m in range(1, k):
                            if copy_board[j-m][i] == player[0]:
                                count += 1
                                if count == k-1:
                                    return True
                                    count = 0
                                else:
                                    return False
                                    count = 0
                for k in range(1, down):
                    if copy_board[j+k][i]==player[1]:
                        for m in range(1, k):
                            if copy_board[j+m][i] == player[0]:
                                count += 1
                                if count == k-1:
                                    return True
                                    count = 0
                                else:
                                    return False
                                    count = 0
                for k in range(1, left):
                    if copy_board[j][i-k]==player[1]:
                        for m in range(1, k):
                            if copy_board[j][i-m] == player[0]:
                                count += 1
                                if count == k-1:
                                    return True
                                    count = 0
                                else:
                                    return False
                                    count = 0
                                    
                for k in range(1, right):
                    if copy_board[j][i+k]==player[1]:
                        for m in range(1, k):
                            if copy_board[j][i+m] == player[0]:
                                count += 1
                                if count == k-1:
                                    return True
                                    count = 0
                                else:
                                    return False
                                    count = 0
                for k in range(1, top_left):
                    if copy_board[j-k][i-k]==player[1]:
                        for m in range(1, k):
                            if copy_board[j-m][i-m] == player[0]:
                                count += 1
                                if count == k-1:
                                    return True
                                    count = 0
                                else:
                                    return False
                                    count = 0
                for k in range(1, top_right):
                    if copy_board[j-k][i+k]==player[1]:
                        for m in range(1, k):
                            if copy_board[j-m][i+m] == player[0]:
                                count += 1
                                if count == k-1:
                                    return True
                                    count = 0
                                else:
                                    return False
                                    count = 0
                for k in range(1, bottom_left):
                    if copy_board[j+k][i-k]==player[1]:
                        for m in range(1, k):
                            if copy_board[j+m][i-m] == player[0]:
                                count += 1
                                if count == k-1:
                                    return True
                                    count = 0
                                else:
                                    return False
                                    count = 0
                for k in range(1, bottom_right):
                    if copy_board[j+k][i+k]==player[1]:
                        for m in range(1, k):
                            if copy_board[j+m][i+m] == player[0]:
                                count += 1
                                if count == k-1:
                                    return True
                                    count = 0
                                else:
                                    return False
                                    count = 0
def valid_moves_white(board, player):
    valid_move = []
    for j in range(8):
        for i in range(8):
            if copy_board[j][i] == ' ':
                copy_board[j][i] = player[0]
                if enclosing_white(board, player, direct)==True:
                    valid_move.append(j)
                    valid_move.append(i)
                    copy_board[j][i] = "'"
                else:
                    copy_board[j][i] = ' '
    
def valid_moves_black(board, player):
    valid_move = []
    for j in range(8):
        for i in range(8):
            if copy_board[j][i] == ' ':
                copy_board[j][i] = player[1]
                if enclosing_black(board, player, direct)==True:
                    valid_move.append(j)
                    valid_move.append(i)
                    copy_board[j][i] = "'"
                else:
                    copy_board[j][i] = ' '

def position_white(pos):
    for i in range(len(letter)):
        for j in range(1,9):
            if str(pos) == str(letter[i])+str(j):
                if copy_board[j-1][i] == "'":
                    copy_board[j-1][i] = player[0]                 
                else:
                    return False
                    print("This is an invalid move. Please try again.")
                    

def position_black(pos):
    for i in range(len(letter)):
        for j in range(1,9):
            if str(pos) == str(letter[i])+str(j):
                if copy_board[j-1][i] == "'":
                    copy_board[j-1][i] = player[1]
                else:
                    return False
                    print("This is an invalid move. Please try again.")

def next_state_white(board, player):
    left = 0
    right = 0
    up = 0
    down = 0
    for i in range(8):
        for j in range(8):
            if copy_board[i][j] == "'":
                copy_board[i][j] = " "
            if copy_board[i][j] == player[1]:
                left = int(j)
                up = int(i)
                down = int(7-i)
                right = int(7-j)
                for k in range(min(left, right)):
                    if copy_board[i][j-k] == player[0] and copy_board[i][j+k] == player[0]:
                        copy_board[i][j] = player[0]
                for k in range(min(up, down)):
                    if copy_board[i-k][j] == player[0] and copy_board[i+k][j] == player[0]:
                        copy_board[i][j] = player[0]
                for k in range(min(min(up, left), min(down, right))):
                    if copy_board[i-k][j-k] == player[0] and copy_board[i+k][j+k] == player[0]:
                        copy_board[i][j] = player[0]
                for k in range(min(min(up, right), min(down, left))):
                    if copy_board[i-k][j+k] == player[0] and copy_board[i+k][j-k] == player[0]:
                        copy_board[i][j] = player[0]

def next_state_black(board, player):
    left = 0
    right = 0
    up = 0
    down = 0
    for i in range(8):
        for j in range(8):
            if copy_board[i][j] == "'":
                copy_board[i][j] = " "
            if copy_board[i][j] == player[0]:
                left = int(j)
                up = int(i)
                down = int(7-i)
                right = int(7-j)
                for k in range(min(left, right)):
                    if copy_board[i][j-k] == player[1] and copy_board[i][j+k] == player[1]:
                        copy_board[i][j] = player[1]
                for k in range(min(up, down)):
                    if copy_board[i-k][j] == player[1] and copy_board[i+k][j] == player[1]:
                        copy_board[i][j] = player[1]
                for k in range(min(min(up, left), min(down, right))):
                    if copy_board[i-k][j-k] == player[1] and copy_board[i+k][j+k] == player[1]:
                        copy_board[i][j] = player[1]
                for k in range(min(min(up, right), min(down, left))):
                    if copy_board[i-k][j+k] == player[1] and copy_board[i+k][j-k] == player[1]:
                        copy_board[i][j] = player[1]

    
def run_two_players():
    pos = input("Is it the turn of 1st player of 2nd player? ")
    while pos != "q":
        for i in range(60):
            if i%2 == 0:
                next_state_black(board, player)
                valid_moves_white(copy_board, player)
                print_board2(board)
                score(board)
                pos = input("Where would you like to place the piece? ")
                position_white(pos)
                if position_white(pos) == False:
                    i = i - 1
                else:
                    i += 1
            else:
                next_state_white(board, player)
                valid_moves_black(board, player)
                print_board2(board)
                score(board)
                pos = input("Where would you like to place the piece? ")
                position_black(pos)
                if position_black(pos) == False:
                    i = i - 1
                else:
                    i += 1
def run_one_player():
    while pos != "q":
        for i in range(60):
            if i %2 ==0:
                next_state(board, player)
                valid_moves_white(copy_board, player)
                print_board2(board)
                score(board)
                pos = input("Where would you like to place the piece? ")
                position_white(pos)
            else:
                for i in range(8):
                    for j in range(8):
                        next_state(board, player)
                        valid_moves_black(board, player)
                        highest = 0
if pos == 1:
    run_one_player()
else:
    run_two_players()



