class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j):
            visited[i][j] = True
            for direction in dirs:
                new_x = i + direction[0]
                new_y = j + direction[1]
                if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0]):
                    continue
                if not visited[new_x][new_y] and grid[new_x][new_y] == "1":
                    dfs(new_x, new_y)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (not visited[i][j]) and grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res