class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        
        l = 0
        r = 0
        res = 0
        while r < len(s):
            if not s[r] in charset:
                charset.add(s[r])
                r += 1
            else:
                res = max(res, len(charset))
                while s[l] != s[r]:
                    charset.remove(s[l])
                    l += 1
                l += 1
                r += 1
        return max(res, len(charset))