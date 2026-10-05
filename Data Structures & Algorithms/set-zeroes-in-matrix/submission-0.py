class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        rowZero = False

        #mark the starting point corresponding to that element == 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        
        #to mark inner elements = 0
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        #to mark oth row elements to 0
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
        #to mark 0th col elements to 0
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0

 




        
        
        