class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        rowZero = False

        # starting point - 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        # inner points - 0 (1, rows/ cols)
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # # Zero first column
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        # # Zero first row
        if rowZero == True:
            for c in range(cols):
                matrix[0][c] = 0
