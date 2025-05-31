main_board = ['b' for x in range(9)]
board_x_col_win = ['x', 'b', 'b', 'x', 'b', 'b', 'x', 'b', 'b']
board_o_row_win = ['o', 'o', 'o', 'x', 'b', 'b', 'x', 'b', 'b']

print(main_board)


def print_board(board):
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])


def check_for_win(board):
    winner = None
    #first check x's then check o's
    for side in ['x', 'o']:
        # check for row wins
        for index in [0, 3, 5]:
            if board[index] == side and board[index + 1] == side and board[index + 2] == side:
                winner = side
        # check for col wins
        for index in [0, 1, 2]:
            if board[index] == side and board[index + 3] == side and board[index + 6] == side:
                winner = side
        # check for diagnal wins
        if board[0] == side and board[4] == side and board[8] == side:
            winner = side
        if board[2] == side and board[4] == side and board[6] == side:
            winner = side
    return winner





print_board(main_board)
print(check_for_win(main_board))
print_board(board_x_col_win)
print(check_for_win(board_x_col_win))
print_board(board_o_row_win)
print(check_for_win(board_o_row_win))
