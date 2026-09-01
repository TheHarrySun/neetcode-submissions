class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distances = [float('infinity')] * n
        distances[src] = 0
        ans = 0
        for i in range(k + 1):
            tempDistances = distances.copy()
            for flight in flights:
                if distances[flight[0]] != float('infinity'):
                    tempDistances[flight[1]] = min(tempDistances[flight[1]], distances[flight[0]] + flight[2])
            distances = tempDistances
        return distances[dst] if distances[dst] != float('infinity') else -1