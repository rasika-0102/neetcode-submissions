class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)

        longest = 0

        for n in my_set:
            if (n - 1) not in my_set:
                length = 1
                while n + length in my_set:
                    length += 1
                longest = max(length, longest)
        return longest
            

                
                

        