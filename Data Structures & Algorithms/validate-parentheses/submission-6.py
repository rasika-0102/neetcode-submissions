class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_map = {"}":"{", ")":"(", "]":"["}

        for p in s:
            if p in my_map:
                if stack and stack[-1] == my_map[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)

        if not stack:
            return True
        else:
            return False

        
        