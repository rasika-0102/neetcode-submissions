class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = ''
        for c in s:
            if c.isalnum():
                f+= c.lower()
            
        l = 0
        r = len(f) - 1

        while l < r:
            if f[l] != f[r]:
                return False
            l += 1
            r -= 1
        return True

            

        