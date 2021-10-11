import string

def init_board(number):
    board = [['.']* number for i in range(number)]
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    abc_list = string.ascii_uppercase
    abc_list = list(abc_list)
    valid_moves = []
    for row in range(len(board)):
        for col in range(len(board)):
            x = str(col+1)
            row_letter = abc_list[row]
            valid_coord = row_letter+x
            valid_moves.append(valid_coord)        
    print(valid_moves)
    user_input = ""
    # while user_input not in valid_moves:
    #     user_input = input("Please give me a coordinate! ")
    #     if user_input
    #     row, col = 0, 0
    #     return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    pass


def has_won(board, player):
    """Returns True if player has won the game."""
    return False


def is_full(board):
    """Returns True if board is full."""
    return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    for element in board:
        print (element)


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board(number=3)

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    player1, player2 = "X", "0"
    get_move(board, player1)
    # row, col = get_move(board, player1)
    #mark(board, 1, row, col)

    winner = 0
    print_result(winner)


def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
