"""
Tic Tac Toe Player
"""
import copy

import math

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
    count = 0
    for row in board:
        for mark in row:
            if mark == X or mark == O:
                count += 1
    if count % 2 == 0:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    posActions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                posActions.add((i, j))
    return posActions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    marker = player(board)
    temp = copy.deepcopy(board)
    temp[action[0]][action[1]] = marker
    return temp

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #The winner could only be the player that played last
    #Checks to see who played last
    if player(board) == X:
        marker = O
    else:
        marker = X
    #checks if the player won on horizontals or verticals
    for i in range(len(board)):
        vCount, hCount = 0, 0
        for j in range(len(board[i])):
            if board[i][j] == marker:
                hCount += 1
            if board[j][i] == marker:
                vCount += 1
        if hCount == 3 or vCount == 3:
            return marker
    #Checks diagnols
    if board[0][0] == board[1][1] == board[2][2] == marker:
        return marker
    if board[0][2] == board[1][1] == board[2][0] == marker:
        return marker
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    count = 0
    for row in board:
        for marks in row:
            if marks == X or marks == O:
                count += 1
    if count == 9:
        return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0


def mini(board):
    if terminal(board):
        return None, utility(board)
    act = actions(board)
    minimum = 5
    move = None
    for posAct in act:
        temp = result(board, posAct)
        moves, val = max_(temp)
        if val < minimum:
            minimum = val
            move = posAct
            if minimum == -1:
                return move, minimum
    return move, minimum

def max_(board):
    if terminal(board):
        return None, utility(board)
    act = actions(board)
    maximum = -5
    move = None
    for posAct in act:
        temp = result(board, posAct)
        moves, val = mini(temp)
        if val > maximum:
            maximum = val
            move = posAct
            if maximum == 1:
                return move, maximum
    return move, maximum


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(terminal(board)):
        return winner(board)
    act = actions(board)
    p = player(board)
    if p == X:
        move, val = max_(board)
        return move
    else:
        move, val = mini(board)
        return move
