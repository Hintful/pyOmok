import sys
import math
import numpy as np
from copy import deepcopy
from enum import IntEnum

MAX_BOARD_SIZE = 15

class Ruleset(IntEnum):
    Freestyle = 0
    Standard = 1
    Renju = 2

class Player(IntEnum):
    empty = 0
    black = 1
    white = 2

class Omok:
    # attributes
    allMoves = []

    def __init__(self):
        # init board
        self.board = np.zeros((MAX_BOARD_SIZE, MAX_BOARD_SIZE))
        for i in range(MAX_BOARD_SIZE):
            for j in range(MAX_BOARD_SIZE):
                self.allMoves.append((i,j))

    def printBoard(self):
        for i in range(MAX_BOARD_SIZE):
            for j in range(MAX_BOARD_SIZE):
                if(self.board[i][j] == Player.empty): print("_", end='')
                elif(self.board[i][j] == Player.black): print("x", end='')
                elif(self.board[i][j] == Player.white): print("o", end='')
                else:
                    print("\nprintBoard Error: unknown board element")
                    break
            print("") # newline

    def getMoves(self, rule, player): # returns list of allowed moves for the player based on given ruleset
        moves = copy.deepcopy(self.allMoves)

        for i in range(MAX_BOARD_SIZE):
            for j in range(MAX_BOARD_SIZE):
                if(board[i][j] != Player.empty): moves.remove((i,j))
        
        if(rule == Ruleset.Freestyle):
            return moves
        elif(rule == Ruleset.Standard):
            pass
        elif(rule == Ruleset.Renju):
            pass
