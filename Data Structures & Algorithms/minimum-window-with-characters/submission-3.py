class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        brute force
        
        if t == "":
            return ""

        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        res, resLen = [-1, -1], float('infinity')

        for i in range(len(s)):
            countS = {}
            for j in range(i, len(s)):
                countS[s[j]] = 1 + countS.get(s[j], 0)

                flag = True
                for c in countT:
                    if countT[c] > countS.get(c, 0):
                        flag = False
                        break
                if flag and (j - i + 1) < resLen:
                    res = [i, j]
                    resLen = j - i + 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
        '''
        # more optimal solution
        if t == "":
            return ""

        countT = defaultdict(int)
        window = defaultdict(int)
        for c in t:
            countT[c] += 1
        
        have = 0
        need = len(countT)
        res = [-1, -1]
        resLen = float('infinity')

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            if c in countT and window[c] == countT[c]:
                have += 1
            
            if have == need:
                while have == need:
                    if r - l + 1 < resLen:
                        res = [l, r]
                        resLen = r - l + 1
                    window[s[l]] -= 1
                    if s[l] in countT and window[s[l]] < countT[s[l]]:
                        have -= 1
                    l += 1
        return s[res[0]:res[1] + 1] if resLen != float('infinity') else ""