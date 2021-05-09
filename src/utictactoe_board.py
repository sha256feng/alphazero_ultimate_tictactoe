#!/usr/bin/env python

import numpy as np

class board():
    def __init__(self):
        self.init_board = np.zeros([9,9]).astype(str)
        self.init_board[self.init_board == "0.0"] = " "
        self.player = 0
        self.current_board = self.init_board
        self.old_move = (-1,-1)
        self.mega_board = np.zeros([3,3]).astype(str)
        self.mega_board[self.mega_board == "0.0"] = " "

    def drop_piece(self, xy):
        """
        Place a bead at position xy.
        :param xy: tuple or list, length 2
        """
        if self.current_board[xy[0], xy[1]] != " ":
            return "Invalid move"
        else:
            if self.player == 0:
                self.current_board[xy[0], xy[1]] = "O"
                self.old_move = xy
                self.player = 1
            elif self.player == 1:
                self.current_board[xy[0], xy[1]] = "X"
                self.old_move = xy
                self.player = 0

    def check_winner(self):
        def _check_ninebox(mat):
            """
            This function can be use to check the small nine-box \
                    or the large nine-box.
            input: mat: a matrix of 3x3
            """
            # look for rows, columns, diagnols
            for i in range(3):
                if mat[i,0] == mat[i,1] == mat[i,2] != ' ':
                    return mat[i,0]
                if mat[0,i] == mat[1,i] == mat[2,i] != ' ':
                    return mat[0,i]
            if mat[0,0] == mat[1,1] == mat[2,2] != ' ':
                return mat[0,0]
            if mat[0,2] == mat[1,1] == mat[2,0] != ' ':
                return mat[1,1]
        
            # look for tie
            count = 0
            for i in range(3):
                for j in range(3):
                    if mat[i,j] != ' ':
                        count += 1
            if count == 9:
                return 'tie'
            else:
                return None

        # update mega_board
        for i in range(3):
            for j in range(3):
                sub_mat = self.current_board[i*3:(i*3+3), j*3:(j*3+3)]
                winner  = _check_ninebox(sub_mat)
                if winner == "O":
                    self.mega_board[i,j] = "O"
                elif winner == "X":
                    self.mega_board[i,j] = "X"
                #elif winner == "tie":
                #    self.mega_board[i,j] = "-"
                else:
                    continue

        winner = _check_ninebox(self.mega_board)
        if winner == "O" or winner == "X":
            return True
        elif winner == "tie":
            return winner
        else:
            return False

    def actions(self):
        acts = []
        
        def _whole_blank_cell(self):
            whole_blank_cells = []
            for i in range(9):
                for j in range(9):
                    if self.current_board[i,j] != '-':
                        whole_blank_cells.append((i,j))
            return whole_blank_cells

        if x != -1:
            x = self.old_move[0] % 3
            y = self.old_move[1] % 3
            for i in range(x*3, x*3+3):
                for j in range(y*3, y*3+3):
                    if self.current_board[i,j] == ' ':
                        acts.append((i,j))
            if len(acts) == 0:
                acts = _whole_blank_cell(self)
        else:
            acts = _whole_blank_cell()
        return acts
