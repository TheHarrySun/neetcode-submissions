class Solution:
    # this is like a slightly optimized brute force
    def containsEnough(self, map1, map2):
        for key, val in map2.items():
            if key in map1 and map1[key] >= val:
                continue
            return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        if s == t:
            return t
        
        res = ""
        length = len(s) + 1
        map_t = {}
        for char in t:
            map_t[char] = 1 + map_t.get(char, 0)
        
        for l in range(len(s)):
            if not s[l] in map_t:
                continue
            r = l
            map_s = {}
            while r < len(s):
                map_s[s[r]] = 1 + map_s.get(s[r], 0)

                if self.containsEnough(map_s, map_t):
                    if r - l + 1 < length:
                        length = r - l + 1
                        res = s[l:r + 1]
                    break
                r += 1
        return res