class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        windowmax = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            validwin = (r - l + 1) - maxf 
            if validwin > k:
                count[s[l]] -= 1
                l += 1
            
            windowmax = max(windowmax, r-l+1)
        return windowmax
            

        