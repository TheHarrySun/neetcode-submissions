class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            temp = i
            ans = 0
            while temp:
                if temp & 1:
                    ans += 1
                temp >>= 1
            res.append(ans)

        return res