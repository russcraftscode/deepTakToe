"""
File: deepTakToe.py
Description: Plays tic-tac-toe by recursively evaluating all
possible outcomes that could come from the available moves
Author: Russell Johnson
Created: 2025-05-31
Version: 1.1
"""


import copy

moves_considered = 0


def print_board(board):
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])


def print_player_choice(board):
    print("0:", board[0], "1:", board[1], "2:", board[2])
    print("3:", board[3], "4:", board[4], "5:", board[5])
    print("6:", board[6], "7:", board[7], "8:", board[8])


def check_for_win(board):
    """
    Checks to see if the game is over or has a winner
    :param board: the board to check
    :return: the side that won, or 'draw', or None if the game continues
    """
    # first check x's then check o's
    for side in ['x', 'o']:
        # check for row wins
        for index in [0, 3, 6]:
            if board[index] == side and board[index + 1] == side and board[index + 2] == side:
                return side
        # check for col wins
        for index in [0, 1, 2]:
            if board[index] == side and board[index + 3] == side and board[index + 6] == side:
                return side
        # check for diagonal wins
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
    """
    Evaluates the strength of a possible move recursively by looking at all possible
    outcomes and the ratio of possible wins to losses
    :param board: the board that shows the move to evaluate
    :param side: the side of the player who is evaluating
    :param current_turn: the side of who's turn it is to move. This is included
    because it considers all possible moves from both sides
    :return: dict of the possible wins and losses
    """
    global moves_considered
    next_turn = 'x'
    if current_turn == 'x': next_turn = 'o'
    eval_score = {"wins": 0, "losses": 0}
    win_state = check_for_win(board)
    # if board game ends in draw return 0
    if win_state == 'draw':
        return eval_score
    # if game continues recursively check the next layer of moves
    if win_state is None:
        # iter through all possible moves
        for square_index, square_contents in enumerate(board):
            # if this is a valid move, evaluate the possible futures of that move
            moves_considered += 1
            if square_contents == '_':  # if the square is empty
                next_board = copy.deepcopy(board)
                next_board[square_index] = current_turn
                move_eval = eval_board(next_board, side, next_turn)
                eval_score["wins"] += move_eval["wins"]
                eval_score["losses"] += move_eval["losses"]
        return eval_score  # return the score of this board state
    # if board is a win return 1
    if win_state == side:
        eval_score["wins"] = 1
        return eval_score
    # if board is a loss return -1
    if win_state != side:
        eval_score["losses"] = 1
        return eval_score


def decide_move(board, side):
    """
    Evaluates all possible moves recursively. Called when it is the deepAI's turn.
    :param board: the current gameboard
    :param side: the side of the deepAI
    :return: the index of the square that should be moved into
    """
    # reject a draw game
    if moves_left(board) == False:
        print("no moves left")
        return None
    # reset the moves considered global tracker
    global moves_considered
    moves_considered = 0
    # evaluate all possible moves
    evaluated_moves = {}
    next_turn = 'x'  # the side of the next player
    if side == 'x': next_turn = 'o'
    for square_index, square_contents in enumerate(board):
        # if this is a valid move, evaluate the possible futures of that move
        if square_contents == '_':  # if the square is empty
            next_board = copy.deepcopy(board)
            next_board[square_index] = side
            move_wins_losses = eval_board(next_board, side, next_turn)
            if move_wins_losses["losses"] == 0 and move_wins_losses["wins"] == 0:
                # bump this up above zero because a draw is better than a loss
                evaluated_moves[square_index] = 0.01
            else:
                evaluated_moves[square_index] = move_wins_losses["wins"] / (
                        move_wins_losses["wins"] + move_wins_losses["losses"])

    # if no wins or blocks needed, take the best long term move
    best_move = max(evaluated_moves, key=evaluated_moves.get)
    print("Considered", moves_considered, "possible outcomes.")
    for key, value in evaluated_moves.items():
        print(f"Square {key} : {value:.2f}")
    print(f"Best move is to go to square {best_move} that has a score of {evaluated_moves[best_move]:.2f}")

    return best_move  # return the index of the square that is best to move into


#################
# Main Gameplay Loop
#################

keep_playing = True
while keep_playing:  # keep looping until the user quits
    # build a blank board
    main_board = ['_' for x in range(9)]

    # loop until the game is over to get human and computer moves
    while check_for_win(main_board) is None:
        print()
        print_player_choice(main_board)
        human_move = int(input("make your move: "))
        main_board[human_move] = 'x'
        # only have the computer move if the game is not over
        if check_for_win(main_board) is None:
            computer_move = decide_move(main_board, 'o')
            main_board[computer_move] = 'o'

    print()
    print_board(main_board)
    outcome = check_for_win(main_board)
    if outcome == 'x': print("you win")
    if outcome == 'o': print("you lose")
    if outcome == 'draw': print("draw game")

    if input("Enter 'q' to quit.").lower() == 'q': keep_playing = False
