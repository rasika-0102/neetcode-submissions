class Solution:
    def calPoints(self, operations: List[str]) -> int:
        my_stack = []
        for i in operations:
            if i == "+":
                my_stack.append(my_stack[-1] + my_stack[-2])
            elif i == "D":
                my_stack.append(2 * my_stack[-1])
            elif i == "C":
                my_stack.pop()
            else:
                my_stack.append(int(i))
        return sum(my_stack)
            

        