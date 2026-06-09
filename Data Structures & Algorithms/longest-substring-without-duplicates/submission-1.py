class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        my_set = set()

        for r in range(len(s)):
            while s[r] in my_set:
                my_set.remove(s[l])
                l += 1
            
            w = (r-l)+1
            my_set.add(s[r])
            longest = max(longest, w)
        
        return longest

        