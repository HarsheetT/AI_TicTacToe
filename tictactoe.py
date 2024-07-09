"""
Tic Tac Toe Player
"""

import math
import copy

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
    countX = 0
    countO = 0

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == X:
                countX += 1
            elif board[row][col] == O:
                countO += 1

    if countX > countO:
        return O
    else:
        return X
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                possibleActions.add((row, col))

    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Invalid action")
    
    row,col = action
    board_copy = copy.deepcopy(board)
    board_copy[row][col] = player(board)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    # Check rows
    for row in range(len(board)):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != EMPTY:
            return board[row][0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winnerPlayer = winner(board)
    if winnerPlayer == X:
        return 1
    elif winnerPlayer == O:
        return -1
    else:
        return 0
    

def maxValue(board):
    """
    Returns the maximum utility value for the current player on the board.
    """
    if terminal(board):
        return utility(board)

    value = -math.inf
    for action in actions(board):
        value = max(value, minValue(result(board, action)))

    return value

def minValue(board):
    """
    Returns the minimum utility value for the current player on the board.
    """
    if terminal(board):
        return utility(board)

    value = math.inf
    for action in actions(board):
        value = min(value, maxValue(result(board, action)))

    return value


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):
        return None

    bestAction = None
    bestValue = -math.inf

    if player(board) == X:
        for action in actions(board):
            value = minValue(result(board, action))
            if value > bestValue:
                bestValue = value
                bestAction = action
    else:
        for action in actions(board):
            value = maxValue(result(board, action))
            if value < bestValue:
                bestValue = value
                bestAction = action

    return bestAction

