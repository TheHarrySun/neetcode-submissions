class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        ans = []
        def dfs(before, after):
            if before == after and before == n:
                res.append("".join(ans))
                return

            if before < n:
                ans.append("(")
                dfs(before + 1, after)
                ans.pop()
            if before > after:
                ans.append(")")
                dfs(before, after + 1)
                ans.pop()
        dfs(0, 0)
        return res