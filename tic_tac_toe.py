import string
import sys

def init_board(number):
    board = [['.']* number for i in range(number)]
    return board


def start_menu():

    print(

        """

    Welcome to the Tic Tac Toe Game!


    Please Choose Player Mode:
        1. Tic Tac Toe (3x3) - Human vs Human
        2. Tic Tac Toe (3x3) - Human vs AI
        3. Gomoku (9x9) - Human vs Human
        4. Gomoku (9x9) - Human vs AI
        5. Exit

        """
        )

    while True:
        player_mode = input("Please give me your choice! \n ")
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
            print("Invalid option, please give me a valid option")
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
        user_input = input("Please give me a coordinate! ").upper()
        if user_input not in valid_moves:
            print("It's not a valid coordinate! Please try again! ")
            continue
        else:
            for element in user_input:      # mukodik, de csak 9x9 es tablaig, ha nagyobbat akarunk, akkor ezt a for ciklus at kell irni!
                if element in valid_letters:
                    row = valid_letters.index(element)
                if element in valid_numbers:
                    col = valid_numbers.index(element)
            if board[row][col] != '.':
                print("The field is already taken")
                continue
            return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    if board[row][col] == '.':
        board[row][col] = player
    return board



def has_won(board, player, number):
    """Returns True if player has won the game."""
    count_list = []
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
                    count -= 1    
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
    return f'\u001b[{colour_code};1m{word}\001'

def print_board(board, number):
    """Prints a 3-by-3 board on the screen with borders."""
    abc_list = string.ascii_uppercase
    for number in range(number):
        if number == 0:
            print('   ' + str(number+1), end='  ')
        else:
            print('  ' + str(number+1), end='  ')
    print('')
    for i in range(len(board)):
        for j in range(len(board[i])):
            if j == 0:
                print(abc_list[i] + '  ' + board[i][j], end = ' ' + ' |')
            else:
                print(' ' + board[i][j], end = ' ' + ' |')
        print('')
        if i!=len(board)-1:
            print('  ' + '----+' * len(board))
    print("\n")


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    print(f'{winner} takes it all! Congrats for {winner} !')
    # play again() function


def tictactoe_game(board, number, mode='HUMAN-HUMAN'):
    counter = pow(number, 2) # ahogy a player lép, csökken egyet
    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board, number)
    while True:
        player1, player2 = "X", "0"
        if counter % 2 == 1:
            row, col = get_move(board, player1)
            board = mark(board, player1, row, col)
            print_board(board, number)
            if has_won(board, player1, number):
                print_result(player1)
            counter -= 1
        else:
            row, col = get_move(board, player2)
            board = mark(board, player2, row, col)
            print_board(board, number)
            if has_won(board, player2, number):
                print_result(player1)
            counter -= 1
        if is_full(board):
            print("It's a tie!")
            break
        # winner = 0
        # print_result(winner)


def main_menu():
    # start menu  >> return number, mode
    number, mode = start_menu()
    board = init_board(number)
    if mode == 'HUMAN-HUMAN':
        tictactoe_game(board, number, 'HUMAN-HUMAN')
    if mode == 'HUMAN-AI':
        tictactoe_game(board, number, 'HUMAN-AI')
    # tictactoe_game('human-AI')


if __name__ == '__main__':
    main_menu()
