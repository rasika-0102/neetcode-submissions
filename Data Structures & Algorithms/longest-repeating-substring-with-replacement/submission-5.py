class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxf = 0
        l = 0
        maxwindow = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            window = r - l + 1
            validwin = window - maxf

            if validwin > k:
                count[s[l]] -= 1
                l += 1
            
            maxwindow = max(maxwindow, r - l + 1)
        return maxwindow
            



        