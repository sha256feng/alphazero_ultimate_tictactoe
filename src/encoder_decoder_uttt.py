#!/usr/bin/env python

import numpy as np
from utictactoe_board import board

def encode_board(board):
    board_state = board.current_board
    encoded = np.zeros([9,9,4]).astype(int)
    encoder_dict = {"O":0, "X":1}
    for row in range(9):
        for col in range(9):
            if board_state[row,col] != " ":
                encoded[row, col, encoder_dict[board_state[row,col]]] = 1
    if board.player == 1:
        encoded[:,:,2] = 1 # player to move
    i,j = board.old_move
    if i == -1 and j == -1:
        pass
    else:
        encoded[i,j,3] = 1
    return encoded

def decode_board(encoded):
    decoded = np.zeros([9,9]).astype(str)
    decoded[decoded == "0.0"] = " "
    decoder_dict = {0:"O", 1:"X"}
    for row in range(9):
        for col in range(9):
            for k in range(2):
                if encoded[row, col, k] == 1:
                    decoded[row, col] = decoder_dict[k]
            if encoded[row, col, 3] == 1:
                old_move = (row, col)
    cboard = board()
    cboard.current_board = decoded
    cboard.player = encoded[0,0,2]
    if old_move:
        cboard.old_move = old_move
    else:
        cboard.old_move = (-1,-1)
    return cboard