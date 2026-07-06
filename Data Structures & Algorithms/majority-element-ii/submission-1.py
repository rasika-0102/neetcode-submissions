class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        res = []
        n = len(nums)

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for key in count:
            if count[key] > n//3:
                res.append(key)
        return res




        