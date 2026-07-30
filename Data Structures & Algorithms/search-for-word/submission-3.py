class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(i, x, y):
            if i == len(word):
                return True
            if (x < 0 or y < 0 or x >= len(board) or y >= len(board[0])):
                return False
            if word[i] != board[x][y]:
                return False
            
            ans = False
            for entry in dirs:
                new_x = x + entry[0]
                new_y = y + entry[1]
                board[x][y] = '#'
                ans = ans or dfs(i + 1, new_x, new_y)
                board[x][y] = word[i]
            return ans

        res = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    res = dfs(0, i, j) or res
        return res