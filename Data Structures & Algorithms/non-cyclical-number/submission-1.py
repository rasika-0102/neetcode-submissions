class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sumOfSqur(n)

        while slow != fast:
            slow = self.sumOfSqur(slow)
            fast = self.sumOfSqur(fast)
            fast = self.sumOfSqur(fast)
        if fast == 1:
            return True
        else:
            return False

    
    def sumOfSqur(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            output += digit ** 2
            n = n // 10
        return output



        