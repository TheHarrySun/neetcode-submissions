class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        l = 0
        r = 0
        strset = set()
        length = 0
        ans = 0
        while r < len(s):
            if s[r] in strset:
                ans = max(ans, length)
                length += 1
                while l < r:
                    if s[l] == s[r]:
                        l += 1
                        length -= 1
                        break
                    else:
                        strset.remove(s[l])
                        l += 1
                        length -= 1
                r += 1
            else:
                strset.add(s[r])
                length += 1
                r += 1
        return max(ans, length)
        '''
        l = 0
        ans = 0
        charset = set()

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            ans = max(ans, r - l + 1)
        return ans