class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_chars = [0] * 26
        
        for i in s1:
            s1_chars[ord(i) - ord('a')] += 1

        s2_chars = [0] * 26
        for i in range(len(s1)):
            s2_chars[ord(s2[i]) - ord('a')] += 1

        if s1_chars == s2_chars:
            return True
        
        l = 0
        while l + len(s1) < len(s2):
            r = l + len(s1)
            s2_chars[ord(s2[l]) - ord('a')] -= 1
            s2_chars[ord(s2[r]) - ord('a')] += 1
            if s1_chars == s2_chars:
                return True
            l += 1
        return False