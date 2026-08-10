class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        q = deque()
        visited = [[-1] * len(board[0]) for _ in range(len(board))]

        for i in range(len(board)):
            if board[i][0] == 'O':
                q.append([i, 0])
                visited[i][0] = 1
            if board[i][len(board[0]) - 1] == 'O':
                q.append([i, len(board[0]) - 1])
                visited[i][len(board[0]) - 1] = 1
            
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                q.append([0, i])
                visited[0][i] = 1
            if board[len(board) - 1][i] == 'O':
                q.append([len(board) - 1, i])
                visited[len(board) - 1][i] = 1
    
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q:
            x, y = q.popleft()

            for direction in directions:
                nx = x + direction[0]
                ny = y + direction[1]

                if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board[0]) or visited[nx][ny] != -1:
                    continue
                if board[nx][ny] == 'O':
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                else:
                    visited[nx][ny] = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                if visited[i][j] != 1:
                    board[i][j] = 'X'