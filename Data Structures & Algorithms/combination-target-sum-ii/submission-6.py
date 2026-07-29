class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        ans = []
        def dfs(i, curr_sum):
            if curr_sum == target:
                res.append(ans.copy())
                return
            elif curr_sum > target:
                return
            
            if i == len(candidates):
                return
            
            curr_sum += candidates[i]
            ans.append(candidates[i])
            dfs(i + 1, curr_sum)
            curr_sum -= candidates[i]
            ans.pop()
            j = i
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, curr_sum)
        dfs(0, 0)
        return res