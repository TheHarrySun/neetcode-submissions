class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]

        res = []

        col = set()
        posDiag = set()
        negDiag = set()
        def dfs(r):
            if r == n:
                ans = ["".join(board[i]) for i in range(len(board))]
                res.append(ans)

            for c in range(len(board[0])):
                if c not in col and r + c not in posDiag and r - c not in negDiag:
                    col.add(c)
                    posDiag.add(r + c)
                    negDiag.add(r - c)
                    board[r][c] = "Q"
                    dfs(r + 1)
                    col.remove(c)
                    posDiag.remove(r + c)
                    negDiag.remove(r - c)
                    board[r][c] = "."
        dfs(0)
        return res