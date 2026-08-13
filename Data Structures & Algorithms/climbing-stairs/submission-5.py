class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        ans = [0] * n
        counter = n - 1
        ans[counter] = 1
        counter = n - 2
        ans[counter] = 2
        counter = n - 3
        while counter >= 0:
            ans[counter] = ans[counter + 1] + ans[counter + 2]
            counter -= 1
        return ans[0]