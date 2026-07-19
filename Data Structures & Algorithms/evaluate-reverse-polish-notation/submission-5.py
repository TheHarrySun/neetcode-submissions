class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']

        stack = []

        for token in tokens:
            if token in operators:
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                print(val1, val2)
                if token == '+':
                    stack.append(val1 + val2)
                if token == '-':
                    stack.append(val1 - val2)
                if token == '*':
                    stack.append(val1 * val2)
                if token == '/':
                    stack.append(val1 / val2)
            else:
                stack.append(token)
        return int(stack.pop())