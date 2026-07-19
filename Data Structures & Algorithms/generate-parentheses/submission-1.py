class Solution:
    def backtrack(self, length: int, open_par: int, close_par: int, curr: str):
        if open_par < close_par or open_par > length / 2 or close_par > length / 2:
            return []
        
        if open_par + close_par == length:
            return [curr]
        
        return self.backtrack(length, open_par + 1, close_par, curr + '(') + self.backtrack(length, open_par, close_par + 1, curr + ')')

    def generateParenthesis(self, n: int) -> List[str]:
        return self.backtrack(2 * n, 0, 0, "")