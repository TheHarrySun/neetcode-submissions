class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        brute force
        '''
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