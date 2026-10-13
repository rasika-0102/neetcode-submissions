class Solution:
    def isValid(self, s: str) -> bool:
        my_map = {')':'(', ']':'[', '}':'{'}
        my_stack = []

        for b in s:
            if b in my_map:
                if my_stack and my_map[b] == my_stack[-1]:
                    my_stack.pop()
                else:
                    return False
            else:
                my_stack.append(b)
        
        if not my_stack:
            return True
        else:
            return False
        