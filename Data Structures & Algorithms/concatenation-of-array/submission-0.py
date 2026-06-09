class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)   # make a list of length 2n filled with 0’s
        n = len(nums)

        for i in range(0, n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        return ans
#you can use this approch of assigning values into the array 
#but don't forget to initialize the ans array. you can't 
#assign values in empty array. initialize it to zero first then assign
        