class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        count = {}
        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            window = r - l + 1
            diff = window - maxf

            if diff > k:
                count[s[l]] -= 1
                l += 1
            
            longest = max(r - l + 1, longest)

        return longest




        