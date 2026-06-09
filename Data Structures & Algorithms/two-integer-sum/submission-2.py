class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # prevMap = {}
        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in prevMap:
        #         return[prevMap[diff], i]
        #     prevMap[n] = i 

        dic = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dic:
                return [dic[diff], i]
            dic[nums[i]] = i