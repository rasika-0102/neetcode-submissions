class Solution:
    def calPoints(self, operations: List[str]) -> int:
        my_stack = []

        for op in operations:
            if op == "+":
                my_stack.append(my_stack[-1] + my_stack[-2])
            elif op == "D":
                my_stack.append( 2 * my_stack[-1])
            elif op == "C":
                my_stack.pop()
            else:
                my_stack.append(int(op))
        return sum(my_stack)

        