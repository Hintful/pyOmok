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

    def __init__(self, rule):
        # init board
        self.board = np.zeros((MAX_BOARD_SIZE, MAX_BOARD_SIZE))
        for i in range(MAX_BOARD_SIZE):
            for j in range(MAX_BOARD_SIZE):
                self.allMoves.append((i,j))

        self.rule = rule

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

    def getMoves(self, player): # returns list of allowed moves for the player based on given ruleset
        moves = copy.deepcopy(self.allMoves)

        for i in range(MAX_BOARD_SIZE):
            for j in range(MAX_BOARD_SIZE):
                if(board[i][j] != Player.empty): moves.remove((i,j)) # remove taken spots
        
        if(self.rule == Ruleset.Freestyle): # no more moves to remove for Freestyle ruleset
            return moves
        elif(self.rule == Ruleset.Standard): # no 6+ moves allowed
            pass
        elif(self.rule == Ruleset.Renju): # no 6+/33/44 allowed for black player
            pass

    def minimax(board, depth, alpha, beta, player, isMaxPlayer):
        if depth == 0 or self.gameOver(board):
            return self.heuristic(board, player)
        elif isMaxPlayer:
            maxVal = -(math.inf) # init to -inf

            for nextBoard in self.getMoves(player):
                val = self.minimax(nextBoard, depth - 1, alpha, beta, (player + 1) % 2, not isMaxPlayer)
                maxVal = max(maxVal, val)
                alpha = max(alpha, val)
                if beta <= alpha:
                    break

            return maxVal
        else: # not isMaxPlayer
            minVal = math.inf # init to +inf

            for nextBoard in self.getMoves(player):
                val = self.minimax(nextBoard, depth - 1, alpha, beta, (player + 1) % 2, not isMaxPlayer)
                minVal = min(minVal, val)
                beta = min(beta, val)
                if beta <= alpha:
                    break

            return minVal


    def heuristics(self, board, player):
        pass


    def gameOver(self, board):
        for x in [Player.black, Player.white]
            for i in range(MAX_BOARD_SIZE):
                for j in range(MAX_BOARD_SIZE):
                    # flags for boundary check
                    rightCheckable = (i < MAX_BOARD_SIZE - 4)
                    downCheckable = (j < MAX_BOARD_SIZE - 4)
                    leftCheckable = (i >= 4)

                    if rightCheckable and (board[i][j] == x and board[i][j+1] == x and board[i][j+2] == x and board[i][j+3] == x and board[i][j+4] == x):
                        return True
                    if rightCheckable and downCheckable and (board[i][j] == x and board[i+1][j+1] == x and board[i+2][j+2] == x and board[i+3][j+2] == x and board[i+4][j+4] == x):
                        return True
                    if downCheckable and (board[i][j] == x and board[i+1][j] == x and board[i+2][j] == x and board[i+3][j] == x and board[i+4][j] == x):
                        return True
                    if downCheckable and leftCheckable and (board[i][j] == x and board[i+1][j-1] == x and board[i+2][j-2] == x and board[i+3][j-3] == x and board[i+4][j-4] == x):
                        return True

        return False
