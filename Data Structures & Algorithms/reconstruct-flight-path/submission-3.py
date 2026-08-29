class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)

        for f, t in sorted(tickets)[::-1]:
            adjList[f].append(t)
        
        stack = ["JFK"]
        res = []
        while stack:
            curr = stack[-1]
            if not adjList[curr]:
                res.append(stack.pop())
            else:
                stack.append(adjList[curr].pop())
        return res[::-1]