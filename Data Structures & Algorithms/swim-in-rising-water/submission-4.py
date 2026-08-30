class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        while minHeap:
            dist, x, y = heapq.heappop(minHeap)
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return dist
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for direction in directions:
                nx = x + direction[0]
                ny = y + direction[1]
                if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or (nx, ny) in visited:
                    continue
                ndist = max(dist, grid[nx][ny])
                visited.add((nx, ny))
                heapq.heappush(minHeap, (ndist, nx, ny))
        return -1