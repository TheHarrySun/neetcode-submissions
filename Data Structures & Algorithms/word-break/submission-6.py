class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [False] * (len(s) + 1)
        visited = [False] * (len(s) + 1)

        cache[len(s)] = True
        def dfs(i):
            if i == len(s):
                return True
            if visited[i]:
                return cache[i]
            seenTrue = False
            for word in wordDict:
                length = len(word)
                if length + i <= len(s) and s[i:i + length] == word:
                    cache[i] = dfs(i + length)
                    if cache[i]:
                        return True                        
            visited[i] = True
            return False

        dfs(0)
        return cache[0]