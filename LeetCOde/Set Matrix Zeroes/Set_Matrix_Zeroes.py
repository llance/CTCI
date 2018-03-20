# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

# click to show follow up.

# Follow up:
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row_len = len(matrix)
        col_len = len(matrix[0])

        row = [False for i in range(row_len)]
        col = [False for j in range(col_len)]


        for i in range(0, row_len):
            for j in range(0, col_len):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True

        for x in range(0, row_len):
            for y in range(0, col_len):
                if row[x] or col[y]:
                    matrix[x][y] = 0


