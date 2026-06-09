class Solution:
    def arrangeCoins(self, n: int) -> int:
        l , r = 0 , n
        res = 0

        while l <= r:

            rows = (l + r) // 2
            coins = rows / 2 * (rows + 1)
            
            if coins > n:
                r = rows - 1
            else:
                l = rows + 1
                res = max(rows, res)
        
        return res


     
        
        
            

        