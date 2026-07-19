class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        pairs = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in pairs:
                if len(stack) == 0 or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)
        if len(stack) != 0:
            return False
        return True