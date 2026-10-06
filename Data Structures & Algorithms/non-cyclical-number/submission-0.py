class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sumOfSqurs(n)

        while slow != fast:
            slow = self.sumOfSqurs(slow)
            fast = self.sumOfSqurs(fast)
            fast = self.sumOfSqurs(fast)
        
        if fast == 1:
            return True
        else:
            return False
        
    def sumOfSqurs(self, n: int) -> int:
        output = 0
        
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n//10
        return output

