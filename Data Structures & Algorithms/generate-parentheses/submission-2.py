from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(n: int, curr: str, num_op: int, num_close: int):
            if len(curr) == 2 * n:
                return [curr]
            ans = []
            if num_op - num_close > 0 and num_close < n:
                ans.extend(generate(n, curr + ')', num_op, num_close + 1))
            if num_op < n:
                ans.extend(generate(n, curr + '(', num_op + 1, num_close))
            return ans
        return generate(n, '', 0, 0)