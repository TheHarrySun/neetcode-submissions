class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        max_str = [0, 0]

        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        for i in range(1, len(s) - 1):
            l = i
            r = i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            length = r - l - 1
            if length > max_len:
                max_len = length
                max_str = [l + 1, r - 1]
        
        for i in range(0, len(s) - 1):
            l = i
            r = i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            length = r - l - 1
            if length > max_len:
                max_len = length
                max_str = [l + 1, r - 1]
        
        return s[max_str[0]: (max_str[1] + 1)]