class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = 0
        r = len(matrix) - 1
        
        while l < r:
            for i in range(r - l):
                top = l
                bottom = r

                #save tl in tmp
                tmp = matrix[top][l + i]

                # bl -> tl
                matrix[top][l + i] = matrix[bottom - i][l]

                # br -> bl
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # tr -> br
                matrix[bottom][r - i] = matrix[top + i][r]

                # tmp -> tr
                matrix[top + i][r] = tmp

            r -= 1
            l += 1




            

        