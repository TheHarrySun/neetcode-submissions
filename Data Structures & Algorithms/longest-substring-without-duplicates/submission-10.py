class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        unique = set()

        res = 0
        while r < len(s):
            if s[r] in unique:
                res = max(res, r - l)
                while l < r:
                    if s[l] == s[r]:
                        l += 1
                        break
                    unique.remove(s[l])
                    l += 1
            else:
                unique.add(s[r])
            r += 1
        return max(res, r - l)
