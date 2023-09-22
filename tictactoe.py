"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    Xcount = 0
    Ocount = 0
    for i in range(3):
        for j in range(3):
            if (board[i][j] == X):
                Xcount += 1
            elif (board[i][j] == O):
                Ocount += 1
    if (Xcount > Ocount):
        return O
    elif (Ocount > Xcount):
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if (board[i][j] == EMPTY):
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]

    curr_player = player(board)
    copy_board = deepcopy(board)
    if (board[i][j] != EMPTY):
        raise Exception
    copy_board[i][j] = curr_player
    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows:
    for row in board:
      if row.count(X) == 3:
        return X
      if row.count(O) == 3:
        return O

    # Check columns:
    for j in range(3):
      column = ''
      for i in range(3):
        column += str(board[i][j])

      if column == 'XXX':
        return X
      if column == 'OOO':
        return O

    # Check Diagonals:
    diag1 = ''
    diag2 = ''
    j = 2

    for i in range(3):
      diag1 += str(board[i][i])
      diag2 += str(board[i][j])
      j -= 1

    if diag1 == 'XXX' or diag2 == 'XXX':
      return X
    elif diag1 == 'OOO' or diag2 == 'OOO':
      return O

    # Otherwise no current winner, return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or not actions(board):
      return True
    else:
      return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winning_player = winner(board)
    if (winning_player == X):
        return 1
    elif (winning_player == O):
        return -1
    else:
        return 0


def max_value(board):
    if (terminal(board)):
        return (utility(board), None)

    u = float(-math.inf)
    best_action = None
    for action in actions(board):
        min_value_result = min_value(result(board, action))
        if min_value_result[0] >= u:
            best_action = action
            u = min_value_result[0]
    return (u, best_action)


def min_value(board):
    if (terminal(board)):
        return (utility(board), None)

    u = float(math.inf)
    best_action = None
    for action in actions(board):
        max_value_result = max_value(result(board, action))
        if max_value_result[0] <= u:
            best_action = action
            u = max_value_result[0]
    return (u, best_action)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return utility(board)

    # posssible_actions = actions(board)
    best_Action = None

    if (player(board) == X):
            best_Action = max_value(board)[1]

    elif (player(board) == O):
            best_Action = min_value(board)[1]

    return best_Action
