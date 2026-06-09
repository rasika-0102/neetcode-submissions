class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        #nums = [1,2,3,3]
        for v in nums:
            #print(k, v)
            if v in my_set:
                return True
            else:
                my_set.add(v)
        return False
                

        