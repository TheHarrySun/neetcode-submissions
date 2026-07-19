class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charset = set()
        for i in s:
            charset.add(i)
        
        res = 0
        for char in charset:
            l = 0
            temp_res = 0
            count = k
            for r in range(len(s)):
                if s[r] != char:
                    count -= 1
                if count == -1:
                    temp_res = max(temp_res, r - l)
                    while s[l] == char:
                        l += 1
                    l += 1
                    count += 1
            temp_res = max(temp_res, r - l + 1)
            res = max(res, temp_res)
        return res