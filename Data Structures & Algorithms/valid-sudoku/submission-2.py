class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            count = [0] * 10
            count2 = [0] * 10
            for j in range(9):
                entry = board[i][j]
                if entry != ".":
                    entry = int(entry)
                    if count[entry] != 0:
                        return False
                    count[entry] += 1
                entry2 = board[j][i]
                if entry2 != ".":
                    entry2 = int(entry2)
                    if count2[entry2] != 0:
                        return False
                    count2[entry2] += 1
        
        for i in range(3):
            for j in range(3):
                count = [0] * 10
                for row in range(3):
                    for col in range(3):
                        entry = board[i * 3 + row][j * 3 + col]
                        if entry == ".":
                            continue
                        entry = int(entry)
                        if count[entry] != 0:
                            return False
                        count[entry] += 1
        return True