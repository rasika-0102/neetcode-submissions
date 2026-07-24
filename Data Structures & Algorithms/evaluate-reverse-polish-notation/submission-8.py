class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        my_stack = []

        for op in tokens:
            if op == "+":
                my_stack.append(my_stack.pop() + my_stack.pop())

            elif op == "-":
                a = my_stack.pop()
                b = my_stack.pop()
                my_stack.append(b - a)

            elif op == "*":
                my_stack.append(my_stack.pop() * my_stack.pop())

            elif op == "/":
                a = my_stack.pop()
                b = my_stack.pop()
                my_stack.append(int(b/a))
            
            else:
                my_stack.append(int(op))

        return my_stack[-1]

        