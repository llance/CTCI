__author__ = 'lanceli'

import unittest
import numpy as np

def rotate_matrix(inputArray):
    rotated_matrix = np.full((5, 5), 0)


    for i in range(0, len(inputArray)):
        for j in range(0, len(inputArray[i])):
            # print("inputArray[",i,"][",j,"]:", inputArray[i][j])
            if j == 0:
                rotated_matrix[i][j] = inputArray[j+4][i]
            if j == 1:
                rotated_matrix[i][j] = inputArray[j+2][i]
            if j == 2:
                rotated_matrix[i][j] = inputArray[j][i]
            if j == 3:
                rotated_matrix[i][j] = inputArray[j-2][i]
            if j == 4:
                rotated_matrix[i][j] = inputArray[j-4][i]
            print("rotated_matrix[",i,"][",j,"]:", rotated_matrix[i][j])
    return rotated_matrix



class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()