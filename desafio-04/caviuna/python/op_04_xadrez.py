"""Chessbord check position of chess pieces by Caviuna's algorithm."""

import numpy as np


class Chess():
    """Chess class"""

    def __init__(self, pieces_chessboard, pieces_chessboard_01,  joined_matrix_2,  per_matrix_02):
        """ Constructor, initialize the chessboard """

        self.pieces_chessboard = pieces_chessboard
        self.pieces_chessboard_01 = pieces_chessboard_01
        self.joined_matrix_2 = joined_matrix_2
        self.per_matrix_02 = per_matrix_02


    def board_in(self):
        """ Prints the chessboard configuration in the format """

        king = 6*np.ones((2,1), dtype=int)
        queen = 5*np.ones((2,1), dtype=int)
        rook = 4*np.ones((2,2), dtype=int)
        bishop =3*np.ones((2,2), dtype=int)
        knight = 2*np.ones((2,2), dtype=int)
        zeros = np.zeros((8, 4), dtype=int)
        pawn = np.ones((8, 2), dtype=int)
        set_pieces_01 = np.concatenate((king, queen), axis=1)
        set_pieces_02 = np.concatenate((set_pieces_01, rook, bishop,
                                        knight))
        set_pieces_00 = np.concatenate((zeros, pawn), axis=1)
        joined_matrix = np.concatenate((set_pieces_00, set_pieces_02), axis=1)
        zeros_2 = np.zeros((8, 8), dtype=int)
        self.joined_matrix_2 = np.concatenate((joined_matrix, zeros_2), axis=1)

        return ()


    def random_matrix(self):
        """ Place pieces randomly on the chess board """

        rng = np.random.default_rng()
        per_martix = rng.permuted(self.joined_matrix_2, axis=1)
        self.per_matrix_02 = per_martix[:, :8]

        return ()


    def count_pieces(self):
        """ Counts the number of pieces on the board and prints the result """

        self.pieces_chessboard_01 = np.transpose(np.nonzero(self.per_matrix_02))
        self.pieces_chessboard = [self.per_matrix_02[row, col] for row,
                                 col in zip(*np.nonzero(self.per_matrix_02))]

        return ()


chess_p = Chess(pieces_chessboard=[], pieces_chessboard_01=[], joined_matrix_2=[], per_matrix_02=[])


chess_p.board_in()


chess_p.random_matrix()
per_matrix_02_p = chess_p.per_matrix_02
print()
print(f'The random method board generator: \n{per_matrix_02_p}')
print()


chess_p.count_pieces()
pieces_chessboard_01_p = chess_p.pieces_chessboard_01
print(f'Position of the rows and columns of the pieces: \n{pieces_chessboard_01_p}')
print()
piece_chessboard = chess_p.pieces_chessboard
print(f'Placement order of pieces:  \n{piece_chessboard}')
print()
len_piece = len(piece_chessboard)
print(f'Count of number of pieces: {len_piece}')
print()
print('Quantity of pieces on the chessboard:')
print(f'King: {piece_chessboard.count(6)} piece(s)')
print(f'Queen: {piece_chessboard.count(5)} piece(s)')
print(f'Rook: {piece_chessboard.count(4)} piece(s)')
print(f'Bishop: {piece_chessboard.count(3)} piece(s)')
print(f'Knight: {piece_chessboard.count(2)} piece(s)')
print(f'Pawn: {piece_chessboard.count(1)} piece(s)')
print()
