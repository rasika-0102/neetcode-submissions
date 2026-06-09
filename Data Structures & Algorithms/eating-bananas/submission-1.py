class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       l , r = 1, max(piles) 
       res = r

       while l <= r:
            k = (l+r)//2

            totalhrs = 0
            for p in piles:
                totalhrs += (p+k-1)//k
            
            if totalhrs <= h:
                r = k-1
                res = k
            elif totalhrs > h:
                l = k+1
       return res


        
