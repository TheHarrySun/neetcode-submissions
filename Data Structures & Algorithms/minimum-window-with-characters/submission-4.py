from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = {}
        for char in t:
            if not char in t_dict.keys():
                t_dict[char] = 1
            else:
                t_dict[char] += 1
        
        resLen = float('infinity')
        res = ""
        s_dict = defaultdict(int)
        have = 0
        need = len(t_dict)
        l = 0
        for r in range(len(s)):
            s_dict[s[r]] += 1
            
            if s[r] in t_dict and s_dict[s[r]] == t_dict[s[r]]:
                have += 1
                    
            while have == need:
                if (r - l + 1) < resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                
                s_dict[s[l]] -= 1
                if s[l] in t_dict and s_dict[s[l]] < t_dict[s[l]]:
                    have -= 1
                l += 1
        return res if resLen != float('infinity') else ""