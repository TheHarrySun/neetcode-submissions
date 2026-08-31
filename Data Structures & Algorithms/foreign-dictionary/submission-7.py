class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)

        adjList = defaultdict(list)
        indegree = defaultdict(int)
        char_set = set()
        for i in range(0, n - 1):
            first = words[i]
            char_set.update(first)
            second = words[i + 1]
            idx = 0
            while idx < len(first):
                if idx >= len(second):
                    return ""
                indegree[first[idx]]
                if first[idx] == second[idx]:
                    idx += 1
                    continue
                adjList[first[idx]].append(second[idx])
                indegree[second[idx]] += 1
                break
        char_set.update(words[len(words) - 1])
        ans = ""
        
        while char_set:
            seen = False
            for entry in char_set:
                if indegree[entry] == 0:
                    ans += entry
                    for adj in adjList[entry]:
                        indegree[adj] -= 1
                    char_set.remove(entry)
                    seen = True
                    break
            if not seen:
                return ""
        return ans