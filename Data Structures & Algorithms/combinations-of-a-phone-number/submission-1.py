class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {'2':'abc', '3':'def', '4': 'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if len(digits) == 0:
            return []
        res = []

        ans = []
        def dfs(i):
            if i == len(digits):
                res.append("".join(ans))
                return
            
            digit = digits[i]
            chars = map[digit]
            for char in chars:
                ans.append(char)
                dfs(i + 1)
                ans.pop()
        dfs(0)
        return res