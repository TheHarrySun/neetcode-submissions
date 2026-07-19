class Solution:
    def countSubstrings(self, s: str) -> str:
        count = 0

        if len(s) == 1:
            return 1
        if len(s) == 2:
            if s[0] == s[1]:
                return 3
            else:
                return 2

        for i in range(0, len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                    count += 1
                else:
                    break
        
        for i in range(0, len(s) - 1):
            l = i
            r = i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                    count += 1
                else:
                    break        
        return count