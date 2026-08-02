class Node:
    def __init__(self):
        self.children = {}
        self.end = False
        self.index = -1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        for i in range(len(words)):
            word = words[i]
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = Node()
                curr = curr.children[char]
            curr.end = True
            curr.index = i
        
        res = []
        curr = root

        visited = [[False] * len(board[0]) for _ in range(len(board))]

        def dfs(x, y, node):
            if node.end and node.index != -1:
                res.append(words[node.index])
                node.index = -1

            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for direction in directions:
                new_x = direction[0] + x
                new_y = direction[1] + y
                if new_x < 0 or new_y < 0 or new_x >= len(board) or new_y >= len(board[0]):
                    continue
                if not visited[new_x][new_y] and board[new_x][new_y] in node.children:
                    visited[new_x][new_y] = True
                    dfs(new_x, new_y, node.children[board[new_x][new_y]])
                    visited[new_x][new_y] = False
            

        for i in range(len(board)):
            for j in range(len(board[0])):
                char = board[i][j]
                if char in root.children:
                    visited[i][j] = True
                    dfs(i, j, root.children[char])
                    visited[i][j] = False
        return res