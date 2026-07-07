class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum = {0 : 1}
        currsum = 0
        res = 0
        
        for n in nums:
            currsum += n
            diff = currsum - k

            if diff in prefixsum:
                res += prefixsum.get(diff, 0)

            prefixsum[currsum] = 1 + prefixsum.get(currsum, 0)

        return res

            
        