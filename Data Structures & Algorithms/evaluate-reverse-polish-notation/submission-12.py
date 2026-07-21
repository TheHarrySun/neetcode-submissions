class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ops = ['+', '-', '*', '/']
        for token in tokens:
            if token in ops:
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                if token == '+':
                    stack.append(n1 + n2)
                elif token == '-':
                    stack.append(n1 - n2)
                elif token == '*':
                    stack.append(n1 * n2)
                else: 
                    stack.append(n1 / n2)
            else:
                stack.append(token)
        return int(stack[0])