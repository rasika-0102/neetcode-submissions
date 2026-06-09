class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for v in tokens:
            if v == "+":
                stack.append(stack.pop() + stack.pop())

            elif v == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)

            elif v == "*":
                stack.append(stack.pop() * stack.pop())

            elif v == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            
            else:
                stack.append(int(v))

        return stack[0]
       

        