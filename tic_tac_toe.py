import string
import sys
import random
import os
import time


def init_board(number):
    board = [['.']* number for i in range(number)]
    return board


def clear():
    os.system("clear")

def start_menu():

    print(

        """\u001b[32;1m

    Welcome to the Tic Tac Toe Game!


    Please Choose Player Mode:
        1. Tic Tac Toe (3x3) - Human vs Human
        2. Tic Tac Toe (3x3) - Human vs AI
        3. Gomoku (9x9) - Human vs Human
        4. Gomoku (9x9) - Human vs AI
        5. Exit\u001b[0m

        """
        )

    while True:
        player_mode = input(colour_print(32, "Please give me your choice! \n" ))
        if player_mode == '1':
            return 3, 'HUMAN-HUMAN'
        elif player_mode == '2':
            return 3,'HUMAN-AI'
        elif player_mode == '3':
            return 9, 'HUMAN-HUMAN'
        elif player_mode == '4':
            return 9, 'HUMAN-AI'
        elif player_mode == '5':
            sys.exit()
        else:
            print(colour_print(31, "Invalid option, please give me a valid option"))
            continue




def validate_moves(board):
    """ Validates moves on a dynamic board, returns valid_moves list
        and valid letters, valid numbers"""
    abc_list = string.ascii_uppercase
    abc_list = list(abc_list)
    valid_letters = []
    valid_numbers = []
    valid_moves = []
    for col in range(len(board)):
        col_number = str(col+1)
        for row in range(len(board)):
            x = str(row+1)
            row_letter = abc_list[col]
            valid_coord = row_letter+x
            valid_moves.append(valid_coord)
        valid_letters.append(row_letter)
        valid_numbers.append(col_number)        
    return valid_moves, valid_letters, valid_numbers


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    valid_moves = validate_moves(board)[0]
    valid_letters, valid_numbers = validate_moves(board)[1], validate_moves(board)[2]
    user_input = ""
    while True:
        user_input = input(colour_print(32, "Please give me a coordinate!")).upper()
        if user_input not in valid_moves:
            print(colour_print(31, "It's not a valid coordinate! Please try again!"))
            continue
        else:
            row_index, col_index = user_input[0], user_input[1::]
            row = valid_letters.index(row_index)
            col = valid_numbers.index(col_index)
            if board[row][col] != '.':
                print(colour_print(31, "The field is already taken!"))
                continue
            return row, col


def smart_ai_checking_one(board, player2, enemy):
    list = []
    number = len(board)-1
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == enemy:
                if row == 0 and col == 0:
                    return [(row+1, col), (row, col+1), (row+1, col+1)]
                elif row != 0 and col == 0 and row != number:
                    return [(row+1, col), (row, col+1), (row+1, col+1), (row-1, col+1), (row-1, col)]
                elif row == 0 and col != 0 and col !=number:
                    return [(row+1, col), (row, col+1), (row+1, col+1), (row-1, col-1), (row, col-1)]
                elif col == number and row == 0:
                    return [(row+1, col), (row, col-1), (row+1, col+1)]
                elif col == number and row != 0 and row != number:
                    return [(row+1, col), (row+1, col-1), (row, col-1),(row-1, col-1),(row-1, col)]
                elif col == number and row==number:
                    return [(row, col-1), (row-1, col-1), (row-1, col)]
                elif row == number and col !=0 and col!=number:
                    return [(row, col+1), (row, col-1), (row-1, col-1),(row-1, col),(row-1, col+1)]
                elif row == number and col == 0:
                    return [(row-1, col), (row-1, col+1), (row, col+1)]
                else:
                    return [(row+1, col), (row+1, col+1), (row+1, col-1),(row, col+1), (row, col-1), (row-1, col-1), (row-1, col), (row-1, col+1)]
               

def smart_ai_checking_two(board, player2, enemy):
    for row in range(len(board)):
        for col in range(len(board[row])):
            try:
                if board[row][col] != '.':
                    if board[row][col+1] != '.':
                        if board[row][col+2] == '.':
                            return row, col+2
                    if board[row+1][col] != '.':
                        if board[row+2][col] == '.':
                            return row+2, col
                    if board[row+1][col+1] != '.':
                        if board[row+2][col+2] == '.':
                            return row+2, col+2
                    if board[row+1][col-1] != '.':
                        if board[row+2][col-2] == '.':
                            return row+2, col-2
            except IndexError:
                continue
    ai_move_list = []
    ai_move_list = smart_ai_checking_one(board, player2, enemy) # ki kell tal??lni mit cisn??ljon a list??val pl random v??lasszon
    coord = random.choice(ai_move_list)    
    return coord


def get_ai_move(board, player2, enemy):
    """Returns the coordinates of a valid move for player on board."""
    valid_moves = ai_validate_moves(board)
    number = len(board)
    if number == 3 and board[1][1] != player2 and board[1][1] != enemy:
        row, col = 1, 1
    elif number == 3 and board[1][1] == enemy:
        corner_coords = [(0, 0), (0, 2), (2, 0), (2, 2)]
        row, col = random.choice(corner_coords)
    else:
        row, col =  smart_ai_checking_two(board, player2, enemy)
    return row, col


def ai_validate_moves(board):
    valid_moves = []
    ai_tuple_coord = ()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == '.':
                ai_tuple_coord = (row, col)
                valid_moves.append(ai_tuple_coord)
    return valid_moves


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    if board[row][col] == '.':
        board[row][col] = player
    return board



def has_won(board, player, number):
    """Returns True if player has won the game."""
    if has_won_row(board, player, number) or has_won_coloumn(board, player, number) or has_won_diagonal1(board, player, number):
        return True
    elif has_won_diagonal2(board, player, number):
        return True
    else:
        return False    
       

def has_won_row(board, player, number):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            try:
                if board[row][col] == player and board[row][col+1] == player:
                    count += 1
                    if number < 7:
                       if count == 2:
                            return True
                    else:
                        if count == 4:
                            return True                        
                elif board[row][col] == player and board[row][col+1] != player:
                    count = 0   
            except IndexError:
                continue
    return False


def has_won_coloumn(board, player, number):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            try:
                if board[row][col] == player and board[row+1][col] == player:
                    count += 1
                    if number < 7:
                        if count == 2:
                            return True
                    else:
                        if count == 4:
                            return True                        
                elif board[row][col] == player and board[row+1][col] != player:
                    count = 0    
            except IndexError:
                continue
    return False
    

def has_won_diagonal1(board, player, number):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            try:
                if board[row][col] == player and board[row+1][col+1] == player:
                    count += 1
                    if number < 7:
                        if count == 2:
                            return True
                    else:
                        if count == 4:
                            return True                        
                elif board[row][col] == player and board[row+1][col+1] != player:
                    count = 0    
            except IndexError:
                continue
    return False


def has_won_diagonal2(board, player, number):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            try:
                if board[row][col] == player and board[row-1][col+1] == player:
                    count += 1
                    if number < 7:
                        if count == 2:
                            return True
                    else:
                        if count == 4:
                            return True                        
                elif board[row][col] == player and board[row-1][col+1] != player:
                    count = 0    
            except IndexError:
                continue
    return False


def is_full(board):
    """Returns True if board is full."""
    for row in range(len(board)):
        for element in board[row]:
            if element == '.':
                return False
    return True


def colour_print(colour_code, word):
    return f'\u001b[{colour_code};1m{word}\u001b[0m'


def print_board(board, number):
    """Prints a 3-by-3 board on the screen with borders."""
    abc_list = string.ascii_uppercase
    for number in range(number):
        if number == 0:
            print('  ', colour_print(31, str(number+1)), end='  ')
        elif number > 0 and number < 10:
            print('  ' + colour_print(31, str(number+1)), end='  ')
        else:
            print(' ' + colour_print(31, str(number+1)), end='  ')
    print('')
    for i in range(len(board)):
        for j in range(len(board[i])):
            if j == 0:
                print(colour_print(31, abc_list[i]) + '  ' + board[i][j], end = ' ' + ' |')
            else:
                print(' ' + board[i][j], end = ' ' + ' |')
        print('')
        if i!=len(board)-1:
            print('  ' + '----+' * len(board))
    print("\n")


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    print(f'{winner} player takes it all! Congrats for {winner} player !')
    play_again()


def play_again():
    while True:
        user_input = input(colour_print(32, "Would you like to play again?\nYes or No?\nPress y or n"))
        if user_input.lower() == "y":
            clear()
            main_menu()
        elif user_input.lower() == "n":
            print(colour_print(32, "Thank you for playing!\nHave a nice day!"))
            sys.exit()
        else:
            print(colour_print(31, "Invalid input, please try again! y/n"))
            continue


def tictactoe_game(board, number, mode='HUMAN-HUMAN'):
    counter = pow(number, 2)
    time.sleep(2)
    clear()
    print_board(board, number)
    while True:
        player1, player2 = colour_print(31, "X"), colour_print(32, "0") 
        if counter % 2 == 1:
            row, col = get_move(board, player1)
            time.sleep(1)
            clear()
            board = mark(board, player1, row, col)
            print_board(board, number)
            if has_won(board, player1, number):
                print_result(player1)
            counter -= 1
        else:
            if mode == 'HUMAN-HUMAN':
                row, col = get_move(board, player2)
                time.sleep(1)
                clear()
                board = mark(board, player2, row, col)
            else:
                time.sleep(2)
                clear()
                row, col = get_ai_move(board, player2, player1)
                board = mark(board, player2, row, col)
            print_board(board, number)
            if has_won(board, player2, number):
                print_result(player2)
            counter -= 1
        if is_full(board):
            print(colour_print(31, "It's a tie!"))
            play_again()


def main_menu():
    number, mode = start_menu()
    board = init_board(number)
    if mode == 'HUMAN-HUMAN':
        tictactoe_game(board, number, 'HUMAN-HUMAN')
    if mode == 'HUMAN-AI':
        tictactoe_game(board, number, 'HUMAN-AI')


if __name__ == '__main__':
    main_menu()

