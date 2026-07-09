class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countS = Counter()
        countT = Counter(t)
        res = ""
        minLen = float('inf')

        l = 0

        for r in range(len(s)):
            countS[s[r]] += 1

            while l <= r and countS & countT == countT:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    res = s[l: r + 1]
            
                countS[s[l]] -= 1
                l += 1
        return res




        