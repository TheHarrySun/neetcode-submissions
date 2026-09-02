class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                temp = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = temp
        
        for i in range(n):
            for j in range(n // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n - j - 1]
                matrix[i][n - j - 1] = temp
