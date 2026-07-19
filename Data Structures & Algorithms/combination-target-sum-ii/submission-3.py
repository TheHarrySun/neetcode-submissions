class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, curr: List[int], total: int):
            if total == target:
                res.append(curr.copy())
                return

            if i == len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])
            curr_val = curr.pop()
            while i < len(candidates) and candidates[i] == curr_val:
                i += 1
            dfs(i, curr, total)
        dfs(0, [], 0)
        return res