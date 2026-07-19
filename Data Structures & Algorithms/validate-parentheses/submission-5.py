class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == ']':
                if not stack:
                    return False
                top = stack[-1]
                if top != '[':
                    return False
                stack.pop()
                continue
            if c == '}':
                if not stack:
                    return False
                top = stack[-1]
                if top != '{':
                    return False
                stack.pop()
                continue
            if c == ')':
                if not stack:
                    return False
                top = stack[-1]
                if top != '(':
                    return False
                stack.pop()
                continue
            stack.append(c)
        if not stack:
            return True
        return False