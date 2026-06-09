class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_map = {}
        #nums = [1,2,3,3]
        for k, v in enumerate (nums):
            #print(k, v)
            if v in my_map:
                return True
            else:
                my_map[v] = k
        return False
                

        