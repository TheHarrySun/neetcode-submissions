from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        
        row = 0
        while l <= r:
            mid = l + (r - l) // 2
            first = matrix[mid][0]
            if first > target:
                r = mid - 1
            elif first < target:
                if mid != len(matrix) - 1 and matrix[mid + 1][0] > target:
                    row = mid
                    break
                elif mid == len(matrix) - 1:
                    row = mid
                    break
                else:
                    l = mid + 1
            else:
                return True
        
        l = 0
        r = len(matrix[row]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            val = matrix[row][mid]
            if val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
            else:
                return True
            
        return False