class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1 ,0]]

        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        res = 0
        def bfs(x, y):
            q = deque()
            q.append([x, y])
            while q:
                i, j = q.popleft()
                if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                    continue
                if not visited[i][j] and grid[i][j] == "1":
                    visited[i][j] = True
                    for direction in directions:
                        q.append([i + direction[0], j + direction[1]])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == "1":
                    bfs(i, j)
                    res += 1
        return res