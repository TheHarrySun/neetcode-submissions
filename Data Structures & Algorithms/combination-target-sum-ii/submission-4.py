from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def dfs(i: int, subset: List[int], total: int):
            if total == target:
                ans.append(subset.copy())
                return
            elif total > target:
                return
            
            if i == len(candidates):
                return
            
            subset.append(candidates[i])
            total += candidates[i]
            dfs(i + 1, subset, total)
            
            subset.pop()
            total -= candidates[i]
            curr = candidates[i]
            while i < len(candidates) and curr == candidates[i]:
                i += 1
            dfs(i, subset, total)
            
        dfs(0, [], 0)
        return ans