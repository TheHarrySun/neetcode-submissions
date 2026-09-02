class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            temp = i
            res_temp = 0
            while temp != 0:
                res_temp += 1 if temp & 1 == 1 else 0
                temp >>= 1
            res.append(res_temp)
        return res