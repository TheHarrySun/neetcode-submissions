class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        directions = [[0, 1], [1, 0], [0, -1], [-1 ,0]]
        def bfs(i, j):
            q = deque()
            q.append([i, j])

            area = 0
            while q:
                x, y = q.popleft()
                if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                    continue
                if grid[x][y] == 1:
                    area += 1
                    for direction in directions:
                        new_x = direction[0] + x
                        new_y = direction[1] + y
                        q.append([new_x, new_y])
                        grid[x][y] = 0
            return area
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, bfs(i, j))
        return res