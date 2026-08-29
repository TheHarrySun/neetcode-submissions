class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1
        
        ans = -1
        currSum = -1
        for i in range(n):
            if currSum < 0:
                ans = i
                currSum = 0
            currSum += gas[i] - cost[i]

        return ans