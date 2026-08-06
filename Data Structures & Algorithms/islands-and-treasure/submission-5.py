class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = deque()

        dist = 0
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append([i, j])
        
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q:
            length = len(q)
            for i in range(length):
                x, y = q.popleft()
                if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                    continue
                if visited[x][y]:
                    continue
                visited[x][y] = True
                if grid[x][y] == -1:
                    continue
                
                grid[x][y] = dist
                for direction in dirs:
                    newx = direction[0] + x
                    newy = direction[1] + y
                    q.append([newx, newy])
            dist += 1