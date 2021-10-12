import string

def init_board(number):
    board = [['.']* number for i in range(number)]
    return board


def start_menu():
    # Human v Human, or Human AI
    #  mode: 1. tic tac toe (3x3)
    # 2. Gomoku (9x9)  ??
    # 3. if input == "dev"
    # return number, (azt returnoli h mekkor a palya, 1 returnolje a 3, 2 9et )
    
    pass

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
    print(valid_moves, valid_letters, valid_numbers)
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
            print (user_input, row, col)
            return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    while True:
<<<<<<< HEAD
        if board[row][col] =='.':
            board[row][col] = player
            break
=======
        if board[row][col] == '.':
            board[row][col] = player
            return board
>>>>>>> 7b6bf491eda028be601e5a4d22002d5d160a3cf3
        else:
            print("this field is already taken field!")
            continue


def has_won(board, player):
    """Returns True if player has won the game."""
    return False


def is_full(board):
    """Returns True if board is full."""
    for row in range(len(board)):
        for element in board[row]:
            if element == '.':
                return False
    return True


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    for element in board:
        print (element)


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(board, number, mode='HUMAN-HUMAN'):
    counter = pow(number, 2) # ahogy a player lép, csökken egyet
    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    while True:
        player1, player2 = "X", "0"
        row, col = get_move(board, player1)
        board = mark(board, player1, row, col)
        print_board(board)
        if is_full(board):
            print("It's a tie!")
            break
        winner = 0
        print_result(winner)


def main_menu():
    # start menu  >> return number, mode
    number = 3
    board = init_board(number)
    tictactoe_game(board, number, 'HUMAN-HUMAN')
    # tictactoe_game('human-AI')


if __name__ == '__main__':
    main_menu()
