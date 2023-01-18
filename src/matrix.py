"""
Matrix class
"""
from random import randint
from typing import List, Tuple
from itertools import product
from consts import SEQ_LEN, VOWEL_COUNT, VOWELS

class Matrix:
    """
    Initialize the matrix
    Initialize seq array as empty
    """

    def __init__(self, row, col, matrix=None) -> None:
        self.row = row
        self.col = col
        self.seq = []
        self.vowel = 0
        if matrix:
            if len(matrix) != row or len(matrix[0]) != col:
                raise ValueError("Matrix dimension mismatch with inputs")
            self.arr = matrix
        else:
            self.arr = [[None] * col] * row

    def random_idx(self, upper_limit: int) -> int:
        """
        Generate random index number between 0 and x
        """
        return randint(0, upper_limit)
        
    def add_key(self, row: int, col: int) -> Tuple[int, int]:
        """
        Add key in seq member variable by randomly selecting one move from the allowed_moves
        """
        allowed_moves = self.get_moves(row, col)
        idx = self.random_idx(len(allowed_moves) - 1)
        (arr_row, arr_col) = allowed_moves[idx]
        arr_row, arr_col = self.check_vowels(allowed_moves, arr_row, arr_col)
        self.seq.append(str(self.arr[arr_row][arr_col]))
        return (arr_row, arr_col)

    def check_vowels(self, allowed_moves, arr_row, arr_col) -> Tuple[int, int]:
        """
        Perform vowel count check and seq
        """
        value = str(self.arr[arr_row][arr_col])
        if value in VOWELS:
            self.vowel +=1
            if self.vowel <= VOWEL_COUNT:
                self.seq.append(value)
            elif self.vowel == VOWEL_COUNT: # regenerate move
                for idx in range(1, len(allowed_moves)):
                    (arr_row, arr_col) = allowed_moves[idx]
                    value = self.arr[arr_row][arr_col]
                    if value in VOWELS:
                        continue
                    else:
                        return (arr_row, arr_col)
                return (None, None)
        return (arr_row, arr_col)

    def check_dim(self, row: int, col: int) -> bool:
        """
        Compare the input dimensions with matrix dimensions
        """
        if self.row >= row and self.col >= col:
            return True
        return False

    def gen_seq(self, row: int, col: int, seq_len: int = SEQ_LEN) -> str:
        """
        Generate sequence of length SEQ_LEN
        """
        in_row = -1
        in_col = -1
        if self.check_dim(row, col):
            self.seq.append(self.arr[row][col])
            for _idx in range(seq_len - 1):
                if in_row != -1 and in_col != -1:
                    (in_row, in_col) = self.add_key(in_row, in_col)
                else:
                    (in_row, in_col) = self.add_key(row, col)
            return "".join(self.seq)
        else:
            raise ValueError("Input dimensions do not match with matrix")

    def __str__(self) -> str:
        return "\n".join([str(row) for row in self.arr])

    def __len__(self) -> int:
        return len(self.arr)

    def __getitem__(self, indices):
        if not isinstance(indices, tuple):
            indices = tuple(indices)

    def get_dim(self) -> Tuple[int, int]:
        """
        get dimensions of the matrix
        """
        return (self.row, self.col)

    def get_moves(self, row: int, col: int) -> List[Tuple[int, int]]:
        """
        Generate knight moves and filter invalid outcomes
        """
        if row < 0 or col < 0:
            raise ValueError("Rows or columns cannot be negative")
        allowed_moves = list(product([row - 1, row + 1], [col - 2, col + 2])) + list(
            product([row - 2, row + 2], [col - 1, col + 1])
        )
        allowed_moves = [
            (row, col)
            for row, col in allowed_moves
            if row > -1
            and col > -1
            and row < self.row
            and col < self.col
            and self.arr[row][col]
        ]
        return allowed_moves
