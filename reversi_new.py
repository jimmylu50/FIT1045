from copy import deepcopy
board = []
direction = [(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(-1,1),(1,1),(1,-1)]
player = [1, 2]
letter = ' abcdefgh'
letters = 'abcdefgh'
numbers = '12345678'
complete_board = [[],
                  [],
                  [],
                  [],
                  [],
                  [],
                  [],
                  []]
def new_board():
    for i in range(8):
        board.append([0]*8)
    board[4][4] = 1
    board[3][3] = 1
    board[3][4] = 2
    board[4][3] = 2
    return board
new_board()

def print_board(board):
    complete_board.clear()
    for i in range(8):
        complete_board.append([])
    for i in range(8):
        complete_board[i].append(i+1)
        for j in range(8):
            complete_board[i].append(board[i][j])
    complete_board.append(letter)
    
    for x in complete_board:
        print(*x, sep = ' | ')
    return complete_board

def score(board):
    black_pieces = 0
    white_pieces = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                black_pieces += 1
            elif board[i][j] == 2:
                white_pieces += 1
    print("The number of black pieces are: " + str(black_pieces))
    print("The number of white pieces are: " + str(white_pieces)) 
    return (black_pieces, white_pieces)

def score2(board):
    black_pieces = 0
    white_pieces = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                black_pieces += 1
            elif board[i][j] == 2:
                white_pieces += 1 
    return (black_pieces, white_pieces)

def enclosing(board, player, pos, direct):
    if player == 1:
        next_player = 2
    else:
        next_player = 1
    pos_row = pos[0]
    pos_col = pos[1]
    dir_row = direct[0]
    dir_col = direct[1]
    if pos_row == 0 or pos_col == 0 or pos_row == 7 or pos_col == 7:
        return False
    if board[pos_row][pos_col] != 0:
        return False
    new_pos_row = pos_row + dir_row
    new_pos_col = pos_col + dir_col
    if board[new_pos_row][new_pos_col] == next_player:
        while board[new_pos_row][new_pos_col] == next_player: 
            if new_pos_row < 0 or new_pos_row > 7 or new_pos_col < 0 or new_pos_col > 7:
                return False
            new_pos_row += dir_row
            new_pos_col += dir_col
            if board[new_pos_row][new_pos_col] == next_player:
                continue
            elif board[new_pos_row][new_pos_col] == player:
                return True
            else:
                return False
    else:
        return False
        
def valid_moves(board, player):
    valid_move = []
    for i in range(8):
        for j in range(8):
            for k in range(len(direction)):
                if enclosing(board, player, (i, j), (direction[k][0], direction[k][1])):
                    valid_move.append(tuple((i, j)))

    return valid_move

def next_state(board, player, pos):
    if player == 1:
        next_player = 2
    else:
        next_player = 1
    for i in range(len(valid_moves(board, player))-1):
        if pos == valid_moves(board, player)[i]:
            for k in range(len(direction)):
                if enclosing(board, player, pos, (direction[k][0], direction[k][1])):
                    pos_row = pos[0]
                    pos_col = pos[1]
                    board[pos_row][pos_col] = player
                    new_pos_row = pos_row + direction[k][0]
                    new_pos_col = pos_col + direction[k][1]
                    while board[new_pos_row][new_pos_col] == next_player:
                        board[new_pos_row][new_pos_col] = player
                        new_pos_row += direction[k][0]
                        new_pos_col += direction[k][1]
                        if board[new_pos_row][new_pos_col] == player:
                            return(board)
                        #I know the assignment specifies that we return both new_board
                        #and next_player here, but I did this so it would
                        #work for other functions. I am not too sure how to do it
                        #the way the assignment wants us to do.
                        

def position(string):
    for i in range(len(letters)):
        for j in range(8):
            if str(string) == str(letters[i])+str(j):
                return(tuple((j-1, i)))

def check_board(board):
    count = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] != 0:
                count += 1
                if count < 64:
                    return True

def check_win(board):
    if score(board)[0] == 0:
        print("The black wins.")
        return
    elif score(board)[1] == 0:
        print("The white wins.")
        return
    elif score(board)[0] > score(board)[1]:
        print("The black wins.")
        return
    elif score(board)[0] < score(board)[1]:
        print("The white wins.")
        return

def run_two_players():
    print_board(board)
    print("Welcome to reversi. The black pieces are represented by 1 and white pieces are represented by 2. ")
    question = input("Would you like to be 1 or 2? ")
    if question == '1':
        player = 1
        otherplayer = 2
    elif question == '2':
        player = 2
        otherplayer = 1
    elif question == 'q':
        return
    for i in range(60):
        while check_board(board):
            if i%2 == 0:
                string = input("Please enter the position of the black piece: ")
                if string == 'q':
                    return
                valid_moves(next_state(board, player, position(string)), player)
                print_board(board)
                score(board)
                i += 1

            elif i%2 != 0:
                string = input("Please enter the position of the white piece: ")
                if string == 'q':
                    return
                valid_moves(next_state(board, otherplayer, position(string)), otherplayer)
                print_board(board)
                score(board)
                i += 1
    check_win(board)

def run_one_player():
    print_board(board)
    print("Welcome to reversi. The black pieces are represented by 1 and white pieces are represented by 2. ")
    question = input("Would you like to be 1 or 2? ")
    if question == '1':
        player = 1
        otherplayer = 2
    elif question == '2':
        player = 2
        otherplayer = 1
    elif question == 'q':
        return
    for i in range(60):
        while check_board(board):
            if i%2 == 0:
                string = input("Please enter the position of the black piece: ")
                if string == 'q':
                    return
                valid_moves(next_state(board, player, position(string)), player)
                print_board(board)
                score(board)
                i += 1
            elif i%2 != 0:
                maximum = 0
                for j in range(len(valid_moves(board, otherplayer))):
                    copy_board = deepcopy(board)
                    valid_moves(next_state(copy_board, otherplayer, valid_moves(board, otherplayer)[j]), otherplayer)
                    if maximum < score2(copy_board)[1]:
                        maximum = score2(copy_board)[1]
                for j in range(len(valid_moves(board, otherplayer))):
                    copy_board = deepcopy(board)
                    valid_moves(next_state(copy_board, otherplayer, valid_moves(board, otherplayer)[j]), otherplayer)
                    if maximum == score2(copy_board)[1]:
                        position1 = valid_moves(board, otherplayer)[j]
                        valid_moves(next_state(board, otherplayer, position1), otherplayer)
                        print_board(board)
                        score(board)
    check_win(board)
                
def running_game():
    choice = input("Would you like to player one player mode or two player mode? (1/2) ")
    if choice == '1':
        run_one_player()
    elif choice == '2':
        run_two_players()
    elif choice == 'q':
        return

running_game()

