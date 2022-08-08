import os
import random
from graphicsv2 import graphics_welcome, graphics_xwin, graphics_owin, graphics_tie, graphics_quit
import time

 #  ______  _____ _____ ______ _   _ _______ _____          _       _____ 
 # |  ____|/ ____/ ____|  ____| \ | |__   __|_   _|   /\   | |     / ____|
 # | |__  | (___| (___ | |__  |  \| |  | |    | |    /  \  | |    | (___  
 # |  __|  \___ \\___ \|  __| | . ` |  | |    | |   / /\ \ | |     \___ \ 
 # | |____ ____) |___) | |____| |\  |  | |   _| |_ / ____ \| |____ ____) |
 # |______|_____/_____/|______|_| \_|  |_|  |_____/_/    \_\______|_____/
#####################################################################################################################################

def init_board():
    """Returns an empty 3-by-3 board (with zeros)."""
    board_default = [['.','.','.'],['.','.','.'],['.','.','.']]
    board = [list(i) for i in zip(*board_default)]
    return board




def get_move(player_move):
    """Returns the coordinates of a valid move for player on board."""
    row, col = (int, int)
    while True:
        if player_move == 'A1':
            row, col = 0, 0
            break
        elif player_move == "A2":
            row, col = 0, 1
            break
        elif player_move == 'A3':
            row, col= 0, 2
            break
        elif player_move == 'B1':
            row, col = 1, 0
            break
        elif player_move == 'B2':
            row, col = 1, 1
            break
        elif player_move == 'B3':
            row, col = 1, 2
            break
        elif player_move == 'C1':
            row, col = 2, 0
            break
        elif player_move == 'C2':
            row, col = 2, 1
            break
        elif player_move == 'C3':
            row, col = 2, 2
            break
    return row, col





def get_input():
    player_move = str(input(f'Move: ').upper())
    return player_move





def mark(board, player, row, col):
    board[row][col] = player
    pass





def has_won(board, player):
    """Returns True if player has won the game."""
    print(board)
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    if board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    if board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True
    if board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    if board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    if board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True
    else:
        return False





def is_full(board):
    """Returns True if board is full."""
    a = 0 
    for row in range(0,3):
        for col in range(0,3):
            if testpoint(board, row, col):
                continue
            else:
                a += 1
    if a == 9:
        return True
    else:
        return False





def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    table = f"""  1   2   3
A  {board[0][0]} | {board[0][1]} | {board[0][2]}
  ---+---+---
B  {board[1][0]} | {board[1][1]} | {board[1][2]}
  ---+---+---
C  {board[2][0]} | {board[2][1]} | {board[2][2]}"""
    print(table)
pass






def print_result(winner, board):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner == "x":
        os.system("clear")
        print_board(board)
        print(graphics_xwin)
    elif winner == "o":
        os.system("clear")
        print_board(board)
        print(graphics_owin)
    pass







def valid_moves(player_move):
    valid_moves = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3", "QUIT"]
    if player_move not in valid_moves:
        os.system("clear")
        print('That\'s not a valid move!')
        return True
    else:
        return False








def taken_moves_test(board, row, col):
    if board[row][col] != ".":
         os.system("clear")
         print('That move has already been made!')
         return True
    else:
        return False


 #          _____ 
 #     /\   |_   _|
 #    /  \    | |  
 #   / /\ \   | |  
 #  / ____ \ _| |_ 
 # /_/    \_\_____|
#########################################################################################################################################


def get_board_copy(board):
    dupeboard = []
    for j in board:
        dupeboard.append(j.copy())
    return dupeboard







def testpoint(board, a, b):
    
    if board[a][b] == '.':
        return True
    else:
        return False







def testWinMove(board, player):
    possible_moves = set(['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3'])
    for moves in possible_moves:
        player_move = moves
        boardcopy = get_board_copy(board)
        row, col = get_move(player_move)
        if testpoint(boardcopy, row, col) == True:
            boardcopy[row][col] = player
        elif testpoint(boardcopy, row, col) == False:
            continue
        print(boardcopy)
        print(valid_moves)
        if has_won(boardcopy, player) != False:
            return row, col
        elif has_won(boardcopy, player) == False:
            continue
    return None






def testCorner(board):
    valid_moves = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for moves in valid_moves:
        player_move = moves
        boardcopy = get_board_copy(board)
        row, col = player_move


        if testpoint(boardcopy, row, col):
            return row,col
        elif testpoint(boardcopy, row, col) == False:
            continue
    return None






def testCenter(board):
    valid_moves = [(1, 1)]
    for moves in valid_moves:
        player_move = moves
        boardcopy = get_board_copy(board)
        row, col = player_move
        

        if testpoint(boardcopy, row, col):
            return row,col
        else:
            return None







def testEmpty(board):
    valid_moves = [(0, 1), (1, 0), (1, 2), (2, 1)]
    for moves in valid_moves:
        player_move = moves
        boardcopy = get_board_copy(board)
        row, col = player_move
        

        if testpoint(boardcopy, row, col):
            return row,col
        else:
            return None







def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    player2 = 'x'
    if player == 'x':
       player2 = 'o'
    move = testWinMove(board, player)
    print('ai')
    if move != None:
        return move
    move = testWinMove(board, player2)
    print('human')
    if move != None:
        return move
    move = testCorner(board)
    print('corner')
    if move != None:
        return move
    move = testCenter(board)
    print('center')
    if move != None:
        return move
    return testEmpty(board)


 #  _    _ _    _ __  __          _   _            _    _ _    _ __  __          _   _ 
 # | |  | | |  | |  \/  |   /\   | \ | |          | |  | | |  | |  \/  |   /\   | \ | |
 # | |__| | |  | | \  / |  /  \  |  \| |  ______  | |__| | |  | | \  / |  /  \  |  \| |
 # |  __  | |  | | |\/| | / /\ \ | . ` | |______| |  __  | |  | | |\/| | / /\ \ | . ` |
 # | |  | | |__| | |  | |/ ____ \| |\  |          | |  | | |__| | |  | |/ ____ \| |\  |
 # |_|  |_|\____/|_|  |_/_/    \_\_| \_|          |_|  |_|\____/|_|  |_/_/    \_\_| \_|                                                                                   
############################################################################################################################


def tictactoe_game_vs():
    global taken_moves, player_move, row, col, board, player, turn
    taken_moves = set([])
    board = init_board()
    turn = 0
    row = 0
    col = 0
    player = ''
    while True:
        if (turn % 2) == 0:
            player = 'x'
            print('X\'s turn')
        elif (turn % 2) == 1:
            player = 'o'
            print('O\'s turn')
        print_board(board)
        player_move = get_input()
        if valid_moves(player_move):
            continue
        if player_move == 'QUIT':
            print(graphics_quit)
            break
        else:
            pass
        row, col = get_move(player_move)
        if taken_moves_test(board, row,col):
            continue
        mark(board, player, row, col)
        if has_won(board, player):
            os.system("clear")
            print_board(board)
            print_result(player, board)
            break
        if is_full(board):
            os.system("clear")
            print_board(board)
            print(graphics_tie)
            break
        turn += 1
        os.system("clear")
        continue

 #           _____            _    _ _    _ __  __          _   _ 
 #     /\   |_   _|          | |  | | |  | |  \/  |   /\   | \ | |
 #    /  \    | |    ______  | |__| | |  | | \  / |  /  \  |  \| |
 #   / /\ \   | |   |______| |  __  | |  | | |\/| | / /\ \ | . ` |
 #  / ____ \ _| |_           | |  | | |__| | |  | |/ ____ \| |\  |
 # /_/    \_\_____|          |_|  |_|\____/|_|  |_/_/    \_\_| \_|
############################################################################################################################


def tictactoe_game_ai_human():
    global taken_moves
    taken_moves = set([])
    board = init_board()
    turn = 0
    row = 0
    col = 0
    player = ''
    ai = 'x'
    human = 'o'
    while True:
        print('X\'s turn')
        print_board(board)
        time.sleep(2)
        row, col = get_ai_move(board, ai)
        try:
            mark(board, ai, row, col)
        except TypeError:
            pass
        if has_won(board, ai):
            os.system("clear")
            print_board(board)
            print_result(ai, board)
            break
        if is_full(board):
            os.system("clear")
            print_board(board)
            print(graphics_tie)
            break
        os.system("clear")
        print('O\'s turn')
        print_board(board)
        player_move = get_input()
        if valid_moves(player_move) == True:
            while True:
                print_board(board)
                player_move = get_input()
                if valid_moves(player_move) == True:
                    continue
                if valid_moves(player_move) == False:
                    break
        if player_move == 'QUIT':
            print(graphics_quit)
            break
        row, col = get_move(player_move)
        if taken_moves_test(board, row,col):
            while True:
                print_board(board)
                player_move = get_input()
                row, col = get_move(player_move)
                if taken_moves_test(board, row, col):
                    continue
                if taken_moves_test(board, row, col) == False:
                    break             
        try:
            mark(board, human, row, col)
        except TypeError:
            pass
        if has_won(board, human):
            os.system("clear")
            print_board(board)
            print_result(board, human)
            break
        if is_full(board):
            os.system("clear")
            print_board(board)
            print(graphics_tie)
            break
        os.system("clear")
        continue

 # _    _ _    _ __  __          _   _                     _____ 
 # | |  | | |  | |  \/  |   /\   | \ | |              /\   |_   _|
 # | |__| | |  | | \  / |  /  \  |  \| |  ______     /  \    | |  
 # |  __  | |  | | |\/| | / /\ \ | . ` | |______|   / /\ \   | |  
 # | |  | | |__| | |  | |/ ____ \| |\  |           / ____ \ _| |_ 
 # |_|  |_|\____/|_|  |_/_/    \_\_| \_|          /_/    \_\_____|
############################################################################################################################


def tictactoe_game_human_ai():
    taken_moves = set([])
    board = init_board()
    turn = 0
    row = 0
    col = 0
    player = ''
    ai = 'o'
    human = 'x'


    while True:
        print('X\'s turn')
        print_board(board)
        player_move = get_input()
        if valid_moves(player_move):
            continue
        if player_move == 'QUIT':
            print(graphics_quit)
            break
        row, col = get_move(player_move)
        if taken_moves_test(board, row,col):
            continue
        try:
            mark(board, human, row, col)
        except TypeError:
            pass
        if has_won(board, human):
            os.system("clear")
            print_board(board)
            print_result(human, board)
            break
        if is_full(board):
            os.system("clear")
            print_board(board)
            print(graphics_tie)
            break
        os.system("clear")
        print('O\'s turn')
        print_board(board)
        time.sleep(2)
        row, col = get_ai_move(board, ai)
        try:
            mark(board, ai, row, col)
        except TypeError:
            pass
        if has_won(board, ai):
            os.system("clear")
            print_board(board)
            print_result(ai, board)
            break
        if is_full(board):
            os.system("clear")
            print_board(board)
            print(graphics_tie)
            break
        os.system("clear")
        continue


 #  __  __          _____ _   _   __  __ ______ _   _ _    _ 
 # |  \/  |   /\   |_   _| \ | | |  \/  |  ____| \ | | |  | |
 # | \  / |  /  \    | | |  \| | | \  / | |__  |  \| | |  | |
 # | |\/| | / /\ \   | | | . ` | | |\/| |  __| | . ` | |  | |
 # | |  | |/ ____ \ _| |_| |\  | | |  | | |____| |\  | |__| |
 # |_|  |_/_/    \_\_____|_| \_| |_|  |_|______|_| \_|\____/ 
############################################################################################################################


def main_menu():
    choose_gamemode = ''
    while True:
        if choose_gamemode != '':
            break
        os.system("clear")
        print(graphics_welcome)
        choose_gamemode = input("Enter gamemode number here: ").upper()
        if choose_gamemode == 'QUIT':
            print(graphics_quit)
            break
        if choose_gamemode == "1":
            os.system("clear")
            tictactoe_game_vs()        # HUMAN-HUMAN
            break
        elif choose_gamemode == "2":
            os.system("clear")
            tictactoe_game_human_ai()   # HUMAN-AI
            break
        elif choose_gamemode == "3":
            os.system("clear")
            tictactoe_game_ai_human()  # AI-HUMAN
            break

        else:
            while choose_gamemode != '1' or '2' or '3' or 'QUIT' :
                os.system("clear")
                print(graphics_welcome)
                print("Invalid Input!")
                choose_gamemode = input("Enter gamemode number here: ").upper()
                if choose_gamemode == 'QUIT':
                    print(graphics_quit)
                    break
                if choose_gamemode == "1":
                    os.system("clear")
                    tictactoe_game_vs()         # HUMAN-HUMAN
                    break
                elif choose_gamemode == "2":
                    os.system("clear")
                    tictactoe_game_human_ai()        # HUMAN-AI
                    break
                elif choose_gamemode == "3":
                    os.system("clear")
                    tictactoe_game_ai_human()
                    break


##################################################################################################################################

if __name__ == '__main__':
    print(graphics_welcome)
    main_menu()