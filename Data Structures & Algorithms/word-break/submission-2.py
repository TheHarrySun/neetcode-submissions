from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        cache = [-1] * len(s)
        def dfs(i):
            if i == len(s):
                return True
            
            if cache[i] != -1:
                return cache[i] == 1
             
            res = False
            for word in wordDict:
                n = len(word)
                if i + n <= len(s) and s[i:(i + n)] == word:
                    res = res or dfs(i + n)
            if res:
                cache[i] = 1
            else:
                cache[i] = 0
            return cache[i] == 1
        return dfs(0)
