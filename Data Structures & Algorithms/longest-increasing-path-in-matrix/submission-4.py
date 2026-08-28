class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            ans = 1
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dire in directions:
                x, y = dire
                nx, ny = x + i, y + j
                if nx < 0 or nx >= len(matrix) or ny < 0 or ny >= len(matrix[0]) or matrix[nx][ny] <= matrix[i][j]:
                    continue
                ans = max(ans, 1 + dfs(nx, ny))
            memo[(i, j)] = ans
            return ans
        
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, dfs(i, j))
        return res