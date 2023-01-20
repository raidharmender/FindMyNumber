"""
Test script for matrix
"""
import unittest
from consts import VOWELS
from matrix import Matrix


class TestMatrix(unittest.TestCase):
    """
    Test class for Matrix
    """

    def test_matrix_dim(self):
        """
        Compare the dimensions
        """
        test_mat = Matrix(4, 5)
        self.assertEqual(test_mat.get_dim(), (4, 5))

    def test_knight_seq_len(self):
        """
        Test case for a sequence length
        """
        test_mat = Matrix(
            4,
            5,
            [
                ["A", "B", "C", "D", "E"],
                ["F", "G", "H", "I", "J"],
                ["K", "L", "M", "N", "O"],
                [None, 1, 2, 3, None],
            ],
        )
        self.assertEqual(len(test_mat.gen_seq(0, 0)), 10)

    def test_knight_vowel(self):
        """
        Test case for more than 2 vowels
        """
        test_mat = Matrix(
            4,
            5,
            [
                ["A", "B", "C", "D", "E"],
                ["F", "G", "H", "I", "J"],
                ["K", "L", "M", "N", "O"],
                [None, 1, 2, 3, None],
            ],
        )
        for _i in range(20):
            count = 0
            for elem in test_mat.gen_seq(1,0):
                if elem in VOWELS:
                    count += 1
            self.assertLessEqual(count, 2)

    def test_knight_seq_start(self):
        """
        Test case for a sequence start character
        """
        test_mat = Matrix(
            4,
            5,
            [
                ["A", "B", "C", "D", "E"],
                ["F", "G", "H", "I", "J"],
                ["K", "L", "M", "N", "O"],
                [None, 1, 2, 3, None],
            ],
        )
        self.assertEqual(test_mat.gen_seq(0, 0)[0], test_mat.arr[0][0])

    def test_knight_move(self):
        """
        test case for expected knight move
        """
        test_mat = Matrix(
            4,
            5,
            [
                ["A", "B", "C", "D", "E"],
                ["F", "G", "H", "I", "J"],
                ["K", "L", "M", "N", "O"],
                [None, 1, 2, 3, None],
            ],
        )
        self.assertListEqual(test_mat.get_moves(1, 1), [(0, 3), (2, 3), (3, 2)])
        self.assertListEqual(test_mat.get_moves(2, 2), [(1, 0), (1, 4), (0, 1), (0, 3)])
        self.assertListEqual(test_mat.get_moves(0, 0), [(1, 2), (2, 1)])
        self.assertListEqual(test_mat.get_moves(2, 4), [(1, 2), (3, 2), (0, 3)])
        
    def test_knight_invalid_index(self):
        """
        test case for invalid move error handling
        """
        test_mat = Matrix(
            4,
            5,
            [
                ["A", "B", "C", "D", "E"],
                ["F", "G", "H", "I", "J"],
                ["K", "L", "M", "N", "O"],
                [None, 1, 2, 3, None],
            ],
        )
        with self.assertRaisesRegex(ValueError, r"^Rows or columns cannot be negative$"):
            test_mat.get_moves(2, -2)

if __name__ == "__main__":
    unittest.main()
