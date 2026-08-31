class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)
        for flight in flights:
            f = flight[0]
            t = flight[1]
            p = flight[2]
            adjList[f].append((t, p))

        prices = [float('infinity') for _ in range(n)]
        prices[src] = 0
        for i in range(k + 1):
            tempPrices = prices.copy()
            for flight in flights:
                if prices[flight[0]] == float('infinity'):
                    continue
                tmp = prices[flight[0]] + flight[2]
                if tmp < tempPrices[flight[1]]:
                    tempPrices[flight[1]] = tmp
            prices = tempPrices
        return prices[dst] if prices[dst] != float('infinity') else -1