class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0

        q = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i, j])
                if grid[i][j] == 1:
                    fresh += 1
        
        def valid(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != 1:
                return False
            return True
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            length = len(q)
            for _ in range(length):
                x, y = q.popleft()
                for direction in dirs:
                    new_x = x + direction[0]
                    new_y = y + direction[1]
                    if valid(new_x, new_y):
                        grid[new_x][new_y] = 2
                        q.append([new_x, new_y])
                        fresh -= 1
            res += 1
        return res if fresh == 0 else -1