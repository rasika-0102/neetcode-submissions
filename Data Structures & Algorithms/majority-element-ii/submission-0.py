class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        size = len(nums)
        count = {}
        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for key in count:
            if count[key] > size // 3:
                res.append(key)
        return res


        

        