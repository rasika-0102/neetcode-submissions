class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counterT = Counter(t)
    
        counterS = Counter()
        
        res = ""
        minLen = float('inf')
        l = 0

        for r in range(len(s)):
            counterS[s[r]] += 1

            while l <= r and counterS & counterT == counterT:
                
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    res = s[l:r+1]
                
                
                counterS[s[l]] -= 1
                if counterS[s[l]] == 0:
                    del counterS[s[l]]  
                l += 1

        return res