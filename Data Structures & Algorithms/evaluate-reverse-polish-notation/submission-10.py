from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            op = c
            if op == '+':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1 + val2)
            elif op == '-':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(-val1 + val2)
            elif op == '*':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1 * val2)
            elif op == '/':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(float(val2) / val1))
            else:
                stack.append(int(op))
        return stack[0]