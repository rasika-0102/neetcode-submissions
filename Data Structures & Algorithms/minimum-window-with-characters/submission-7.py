class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts = Counter()
        countt = Counter(t)
        minres = float('inf')
        res = ""

        l = 0

        for r in range(len(s)):
            counts[s[r]] += 1

            while l <= r and counts & countt == countt:
                window = r - l + 1
                if window < minres:
                    minres = window
                    res = s[l: r + 1]

                counts[s[l]] -= 1
                l += 1
        return res


            



