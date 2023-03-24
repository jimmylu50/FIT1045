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
    return black_pieces

score(board) 
player = ['W','B']
direct = [[0,1],[1,0],[-1,0],[0,-1],[-1,-1],[-1,1],[1,1],[1,-1]]
letter = 'abcdefgh'
copy_board = copy(board)
otherplayer = ''

def enclosing(board, player, otherplayer, direct):
    down = 0
    right = 0
    top = 0
    left = 0
    count = 0
    for j in range(8):
        for i in range(8):
            if copy_board[j][i] == player:
                up = int(j)
                left = int(i)
                down = int(7-j)
                right = int(7-i)
                top_left = min(up, left)
                top_right = min(up, right)
                bottom_left = min(down, left)
                bottom_right = min(down, right)
                for k in range(1, up):
                    if copy_board[j-k][i] == player:
                        for m in range(1, k):
                            if copy_board[j-m][i] == otherplayer:
                                count += 1
                                if count == k-1:
                                    count = 0
                                    return True
                                else:
                                    count = 0
                                    return False
                                    
                for k in range(1, down):
                    if copy_board[j+k][i]==player:
                        for m in range(1, k-1):
                            if copy_board[j+m][i] == otherplayer:
                                count += 1
                                if count == k-1:
                                    count = 0
                                    return True
                                else:
                                    count = 0
                                    return False
                for k in range(1, left):
                    if copy_board[j][i-k]==player:
                        for m in range(1, k):
                            if copy_board[j][i-m] == otherplayer:
                                count += 1
                                if count == k-1:
                                    count = 0
                                    return True
                                else:
                                    count = 0
                                    return False
                for k in range(1, right):
                    if copy_board[j][i+k]==player:
                        for m in range(1, k):
                            if copy_board[j][i+m] == otherplayer:
                                count += 1
                                if count == k-1:
                                    count = 0
                                    return True
                                else:
                                    count = 0
                                    return False
                for k in range(1, top_left):
                    if copy_board[j-k][i-k]==player:
                        for m in range(1, k):
                            if copy_board[j-m][i-m] == otherplayer:
                                count += 1
                                if count == k-1:
                                    count = 0
                                    return True

                                else:
                                    count = 0
                                    return False

                for k in range(1, top_right):
                    if copy_board[j-k][i+k]==player:
                        for m in range(1, k):
                            if copy_board[j-m][i+m] == otherplayer:
                                count += 1
                                if count == k-1:
                                    count = 0
                                    return True

                                else:
                                    count = 0
                                    return False

                for k in range(1, bottom_left):
                    if copy_board[j+k][i-k]==player:
                        for m in range(1, k):
                            if copy_board[j+m][i-m] == otherplayer:
                                count += 1
                                if count == k-1:
                                    count = 0
                                    return True

                                else:
                                    count = 0
                                    return False

                for k in range(1, bottom_right):
                    if copy_board[j+k][i+k]==player:
                        for m in range(1, k):
                            if copy_board[j+m][i+m] == otherplayer:
                                count += 1
                                if count == k-1:
                                    count = 0
                                    return True

                                else:
                                    count = 0
                                    return False


                                    
def valid_moves(board, player, otherplayer):
    valid_move = []
    for j in range(8):
        for i in range(8):
            if copy_board[j][i] == ' ':
                copy_board[j][i] = player
                pos = (j, i)
                if enclosing(board, player, otherplayer, direct):
                    valid_move.append((j, i))
                    copy_board[j][i] = "'"
                else:
                    copy_board[j][i] = ' '


def position(pos, player):
    for i in range(len(letter)):
        for j in range(1,9):
            if str(pos) == str(letter[i])+str(j):
                if copy_board[j-1][i] == "'":
                    copy_board[j-1][i] = player                 
                else:
                    print("This is an invalid move. Please try again.")
                    

def next_state(board, player, otherplayer):
    left = 0
    right = 0
    up = 0
    down = 0
    for i in range(8):
        for j in range(8):
            if copy_board[i][j] == "'":
                copy_board[i][j] = " "
            if copy_board[i][j] == player:
                left = int(j)
                up = int(i)
                down = int(7-i)
                right = int(7-j)
                for k in range(min(left, right)):
                    if copy_board[i][j-k] == otherplayer and copy_board[i][j+k] == otherplayer:
                        copy_board[i][j] = otherplayer
                for k in range(min(up, down)):
                    if copy_board[i-k][j] == otherplayer and copy_board[i+k][j] == otherplayer:
                        copy_board[i][j] = otherplayer
                for k in range(min(min(up, left), min(down, right))):
                    if copy_board[i-k][j-k] == otherplayer and copy_board[i+k][j+k] == otherplayer:
                        copy_board[i][j] = otherplayer
                for k in range(min(min(up, right), min(down, left))):
                    if copy_board[i-k][j+k] == otherplayer and copy_board[i+k][j-k] == otherplayer:
                        copy_board[i][j] = otherplayer

def check_board(board):
    for i in range(8):
        for j in range(8):
            if copy_board[:i][:j] == " " or copy_board[:i][:j] == "'":
                return True
                

def run_two_players():
    while True:
        for i in range(60):
            if i%2 == 0:
                next_state(board, player[0], player[1])
                valid_moves(board, player[0], player[1])
                print_board2(board)
                score(board)
                pos = input("Where would you like to place the white piece? ")
                if pos == ('q'):
                    quit
                position(pos, player[0])
                if position(pos, player[0]) == False:
                    i = i - 1
                else:
                    i += 1
                    
            else:
                next_state(board, player[1], player[0])
                valid_moves(board, player[1], player[0])
                print_board2(board)
                score(board)
                pos = input("Where would you like to place the black piece? ")
                if pos == ('q'):
                    quit
                position(pos, player[1])
                if position(pos, player[1]) == False:
                    i = i - 1
                else:
                    i += 1
    if check_board(board):
        print("The game has ended")
        
    
def run_one_player():
    while pos != "q":
        for i in range(60):
            if i %2 ==0:
                next_state(board, player)
                valid_moves(copy_board, player)
                print_board2(board)
                score(board)
                pos = input("Where would you like to place the piece? ")
                position_white(pos)
            else:
                next_state(board, player[1], player[0])
                valid_moves(board, player[1], player[0])
                maximum = 0
                for i in range(8):
                    for j in range(8):
                        if copy_board[i][j] == "'":
                            copy_board[i][j] = player[1]
                            
                print_board2(board)
                score(board)
                position(pos, player[1])
question = input("Would you like to play 1 player mode or 2 player mode: ")
if question == '1':
    print(True)
else:
    run_two_players()



