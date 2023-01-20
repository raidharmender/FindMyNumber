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

    def add_key(self, row: int, col: int) -> Tuple[int, int]:
        """
        Add key in seq member variable by randomly selecting one move from the next_moves
        """
        next_moves = self.get_moves(row, col)
        prev = None
        if len(self.seq) >=2:
            prev = self.seq[-2]
        next_moves = [(row, col) for (row, col) in next_moves if self.arr[row][col] != prev] 
        arr_row, arr_col = next_moves[randint(0, len(next_moves) - 1)]
        if arr_row > -1 and arr_col > -1:
            self.seq.append(str(self.arr[arr_row][arr_col]))
        return (arr_row, arr_col)

    def gen_seq(self, row: int, col: int, seq_len: int = SEQ_LEN) -> str:
        """
        Generate sequence of length SEQ_LEN
        """
        (in_row, in_col) = self.reset_vars()

        if self.check_dim(row, col):
            self.seq.append(self.arr[row][col])
            for _idx in range(seq_len - 1):
                if in_row != -1 and in_col != -1:
                    (in_row, in_col) = self.add_key(in_row, in_col)
                elif in_row is None and in_col is None:
                    return self.seq
                else:
                    (in_row, in_col) = self.add_key(row, col)
            for idx, elem in enumerate(self.seq):
                count = 0
                if elem in VOWELS:
                    if count < VOWEL_COUNT:
                        count += 1
                    else:
                        self.seq = self.seq[: idx - 1]
                        break
            for idx, elem in enumerate(self.seq):
                if idx > 1 and self.seq[idx] == self.seq[idx - 2]:
                    self.seq = self.seq[: idx - 1]
                    break
            return self.seq
        raise ValueError("Input dimensions do not match with matrix")

    def reset_vars(self) -> Tuple[int, int, int, int]:
        """
        Gen Seq resets some variables which can be used by the object
        """
        in_row, in_col = [-1] * 2
        self.seq = []
        return (in_row, in_col)

    def get_moves(
        self, row: int, col: int) -> List[Tuple[int, int]]:
        """
        Generate knight moves and filter invalid outcomes
        """
        if row < 0 or col < 0:
            raise ValueError("Rows or columns cannot be negative")
        next_moves = list(product([row - 1, row + 1], [col - 2, col + 2])) + list(
            product([row - 2, row + 2], [col - 1, col + 1])
        )
        next_moves = [
            (row, col)
            for row, col in next_moves
            if row > -1
            and col > -1
            and row < self.row  # Avoid crossing row boundary
            and col < self.col  # Avoid crossing the col boundary
            and self.arr[row][col]  ## Avoid invalid cells marked as None
        ]
        return next_moves

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

    def check_dim(self, row: int, col: int) -> bool:
        """
        Compare the input dimensions with matrix dimensions
        """
        if self.row >= row and self.col >= col:
            return True
        return False
