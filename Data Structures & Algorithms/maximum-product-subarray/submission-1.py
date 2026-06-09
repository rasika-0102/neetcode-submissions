class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curmin = 1
        curmax = 1

        for n in nums:
            tmp = n * curmax
            curmax = max (n * curmax, n * curmin, n)
            curmin = min (tmp , n * curmin, n)

            res = max(res, curmax)
        return res
        
        

        