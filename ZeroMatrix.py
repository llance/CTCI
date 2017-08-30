__author__ = 'lanceli'
import unittest

def zero_matrix(inputMatrix):
    inputMatrix_replicate = inputMatrix
    for row in range(0, len(inputMatrix)):
        for col in range(0, len(inputMatrix[row])):
            if inputMatrix[row][col] == 0:
                inputMatrix_replicate = clean_matrix_row_and_col(inputMatrix_replicate, row, col)
    print_matrix(inputMatrix_replicate)
    return inputMatrix_replicate

def clean_matrix_row_and_col(matrix_to_clean, row_arg, col_arg):
    for row in range(0, len(matrix_to_clean)):
        for col in range(0, len(matrix_to_clean[row])):
            if row == row_arg:
                matrix_to_clean[row_arg][col] = 0
            if col == col_arg:
                matrix_to_clean[row][col_arg] = 0

    return matrix_to_clean

def print_matrix(matrix_to_print):
    for i in range(0, len(matrix_to_print)):
        for j in range(0, len(matrix_to_print[i])):
            print("rotated_matrix[",i,"][",j,"]:", matrix_to_print[i][j])



class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()