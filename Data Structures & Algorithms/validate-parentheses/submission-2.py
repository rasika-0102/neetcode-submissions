class Solution:
    def isValid(self, s: str) -> bool:
        
        my_stack = []
        my_map = {")" : "(", "]" : "[", "}" : "{"}

        for p in s:
            if p in my_map:
                if my_stack and my_stack[-1] == my_map[p]:
                    my_stack.pop()
                else:
                    return False
            else:
                my_stack.append(p)

        return True if not my_stack else False

    

        