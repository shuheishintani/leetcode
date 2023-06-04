from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            print(stack)
            if op.isdigit() or op[0] == "-":
                stack.append(int(op))
            elif op == "+":
                stack.append(stack[len(stack) - 1] + stack[len(stack) - 2])
            elif op == "D":
                stack.append(stack[len(stack) - 1] * 2)
            elif op == "C":
                stack.pop()
        return sum(stack)


sol = Solution()
res = sol.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"])
print(res)
