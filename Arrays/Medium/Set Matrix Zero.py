'''
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

If a item is 0, the wholr row and column becomes zero. 
Hint: Use the first row and first column to keep track if that row or column becomes 0 in the end
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])

        row_zero = False
        for i in range(m):
            if matrix[i][0] == 0:
                row_zero = True
        col_zero = False
        for j in range(n):
            if matrix[0][j] == 0:
                col_zero = True

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        if col_zero:
            for j in range(n):
                matrix[0][j] = 0
        if row_zero:
            for i in range(m):
                matrix[i][0] = 0
