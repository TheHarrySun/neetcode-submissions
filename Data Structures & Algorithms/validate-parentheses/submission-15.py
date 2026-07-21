class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'(':')', '{': '}', '[': ']'}

        stack = []
        for char in s:
            if char in valid.keys():
                stack.append(valid[char])
                continue
            if not stack or stack[-1] != char:
                return False
            stack.pop()
        return True if len(stack) == 0 else False