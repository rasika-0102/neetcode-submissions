class Solution:
    def mySqrt(self, x: int) -> int:

        l, r = 0, x

        while l<=r:
            m = l +(r-l) // 2

            if m * m > x: 
                r = m-1
            elif m * m < x:
                l = m+1 #try to find better ans as well
                res = m #save m as current best answer
            else:
                return m
        return res

                

        
        