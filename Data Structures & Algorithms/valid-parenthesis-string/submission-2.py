class Solution:
    def checkValidString(self, s: str) -> bool:
        s1 = []
        s2 = []
        for i, char in enumerate(s):
            if char == '(':
                s1.append(i)
            elif char == '*':
                s2.append(i)
            else:
                if s1:
                    s1.pop()
                elif s2:
                    s2.pop()
                else:
                    return False
            
        while s1 and s2:
            left = s1.pop()
            star = s2.pop()
            if left > star:
                return False
        return len(s1) == 0