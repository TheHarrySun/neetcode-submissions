class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        q1 = deque()
        pacific = [[0] * len(heights[0]) for _ in range(len(heights))]
        for i in range(len(heights)):
            q1.append([i, 0])
            pacific[i][0] = 1
        for i in range(len(heights[0])):
            if i != 0:
                q1.append([0, i])
                pacific[0][i] = 1

        def valid(x, y, visited):
            if x < 0 or y < 0 or x >= len(heights) or y >= len(heights[0]) or visited[x][y] != 0:
                return False
            return True

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q1:
            x, y = q1.popleft()

            for direction in directions:
                new_x = direction[0] + x
                new_y = direction[1] + y
                if valid(new_x, new_y, pacific):
                    if heights[new_x][new_y] >= heights[x][y]:
                        pacific[new_x][new_y] = 1
                        q1.append([new_x, new_y])
                    
        q2 = deque()
        atlantic = [[0] * len(heights[0]) for _ in range(len(heights))]
        for i in range(len(heights)):
            q2.append([i, len(heights[0]) - 1])
            atlantic[i][len(heights[0]) - 1] = 1
        for i in range(len(heights[0])):
            if i != len(heights[0]) - 1:
                q2.append([len(heights) - 1, i])
                atlantic[len(heights) - 1][i] = 1
        
        while q2:
            x, y = q2.popleft()
            for direction in directions:
                new_x = direction[0] + x
                new_y = direction[1] + y
                if valid(new_x, new_y, atlantic):
                    if heights[new_x][new_y] >= heights[x][y]:
                        atlantic[new_x][new_y] = 1
                        q2.append([new_x, new_y])

        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if atlantic[i][j] == 1 and pacific[i][j] == 1:
                    res.append([i, j])
        return res