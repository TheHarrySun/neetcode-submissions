class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # the issue with this problem is that it is hard to keep track of if you have
        # the right number of each chars
        
        # the clever way is to keep a variable have (which is # of chars from t you 
        # have enough of) and need (which is # of chars from t you need)

        if t == "":
            return ""

        if len(s) < len(t):
            return ""
        
        map_t = {}
        window = {}
        for char in t:
            map_t[char] = 1 + map_t.get(char, 0)
        
        have = 0
        need = len(map_t)
        l = 0

        res = [-1, -1]
        length = float("infinity")
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if window[s[r]] == map_t.get(s[r], 0):
                have += 1
            
            while have == need:
                if r - l + 1 < length:
                    res = [l, r + 1]
                    length = r - l + 1
                
                window[s[l]] -= 1
                if window[s[l]] == map_t.get(s[l], 0) - 1:
                    have -= 1
                l += 1
        return s[res[0]:res[1]] if length != float("infinity") else ""