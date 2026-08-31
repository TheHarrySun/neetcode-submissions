class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {c : set() for w in words for c in w}
        indegree = {c : 0 for w in words for c in w}

        for i in range(0, len(words) - 1):
            first = words[i]
            second = words[i + 1]
            idx = 0
            while idx < len(first):
                if idx >= len(second):
                    return ""
                if first[idx] == second[idx]:
                    idx += 1
                    continue
                if second[idx] not in adjList[first[idx]]:
                    adjList[first[idx]].add(second[idx])
                    indegree[second[idx]] += 1
                idx += 1
                break
        
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []

        while q:
            curr = q.popleft()
            for adj in adjList[curr]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)
            res.append(curr)
        if len(res) != len(adjList):
            return ""
        return "".join(res)