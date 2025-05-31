import copy

main_board = ['_' for x in range(9)]
board_x_col_win = ['x', '_', '_', 'x', '_', '_', 'x', '_', '_']
board_o_row_win = ['o', 'o', 'o', 'x', '_', '_', 'x', '_', '_']
board_draw = ['o', 'x', 'o', 'x', 'x', 'o', 'x', 'o', 'x']
board_no_winner = ['o', '_', 'o', 'x', 'x', '_', '_', '_', 'x']

print(main_board)


def print_board(board):
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])


def check_for_win(board):
    winner = None
    # first check x's then check o's
    for side in ['x', 'o']:
        # check for row wins
        for index in [0, 3, 5]:
            if board[index] == side and board[index + 1] == side and board[index + 2] == side:
                return side
        # check for col wins
        for index in [0, 1, 2]:
            if board[index] == side and board[index + 3] == side and board[index + 6] == side:
                return side
        # check for diagnal wins
        if board[0] == side and board[4] == side and board[8] == side:
            return side
        if board[2] == side and board[4] == side and board[6] == side:
            return side
    # if no winner yet, see if there are any moves left to be made
    if moves_left(board):
        return None  # no winner, game continues
    else:
        return 'draw'  # no winner, game is over


def moves_left(board):
    """
    returns true if there are no moves left to make
    """
    for square in board:
        if square == '_': return True
    return False


def eval_board(board, side, current_turn):
    next_turn = 'x'
    if current_turn == 'x': next_turn = 'o'
    eval_score = 0
    win_state = check_for_win(board)
    # if board game ends in draw return 0
    if win_state == 'draw':
        return 0
    # if game continues recursively check the next layer of moves
    if win_state == None:
        #iter through all possible moves
        for square_index, square_contents in enumerate(board):
            #if this is a valid move, evlauate the possible futures of that move
            if square_contents == '_': # if the square is empty
                next_board = copy.deepcopy(board)
                next_board[square_index] = current_turn
                eval_score += eval_board(next_board, side, next_turn)
        return eval_score # return the score of this board state

    # if board is a win return 1
    if win_state == side:
        return 1
    # if board is a loss return -1
    if win_state != side:
        return -1





print_board(main_board)
print(check_for_win(main_board))
print_board(board_x_col_win)
print(check_for_win(board_x_col_win))
print_board(board_o_row_win)
print(check_for_win(board_o_row_win))
print_board(board_draw)
print(check_for_win(board_draw))
print_board(board_no_winner)
print(check_for_win(board_no_winner))
print(eval_board(board_no_winner, 'x', 'x'))
print(eval_board(board_no_winner, 'o', 'x'))

