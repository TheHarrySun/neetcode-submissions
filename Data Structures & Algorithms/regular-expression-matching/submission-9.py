class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dfs(i, j):
            print(i, j)
            if i == len(s) and j == len(p):
                return True
            if j == len(p):
                return False
            if i == len(s):
                if j + 1 < len(p) and p[j + 1] == '*':
                    return dfs(i, j + 2)
                return False
            if (i, j) in memo:
                return memo[(i, j)]
            
            ans = False
            if j + 1 < len(p) and p[j + 1] == '*':
                ans = ans or dfs(i, j + 2)
            if s[i] == p[j] or p[j] == '.':
                if j + 1 < len(p) and p[j + 1] == '*':
                    ans = ans or dfs(i + 1, j) or dfs(i + 1, j + 2)
                else:
                    ans = ans or dfs(i + 1, j + 1)
            memo[(i, j)] = ans
            print(i, j, ans)
            return ans
        return dfs(0, 0)