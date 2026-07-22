class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        if target < matrix[0][0]:
            return False
        if target > matrix[-1][0]:
            row = len(matrix) - 1
        else:
            l = 0
            r = len(matrix) - 1
            while l != r - 1:
                m = l + (r - l) // 2
                if matrix[m][0] == target:
                    return True
                if matrix[m][0] < target:
                    l = m
                elif matrix[m][0] > target:
                    r = m
            if matrix[r][0] == target:
                return True
            row = l
        
        l = 0
        r = len(matrix[row]) - 1
        while l < r:
            m = l + (r - l) // 2
            if matrix[row][m] == target:
                return True
            if matrix[row][m] < target:
                l = m + 1
            if matrix[row][m] > target:
                r = m
        return matrix[row][l] == target