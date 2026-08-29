class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjList = {}
        totalList = wordList.copy()
        totalList.append(beginWord)

        for word in totalList:
            for i in range(len(word)):
                if i == 0:
                    idx = "*" + word[1:]
                elif i == len(word) - 1:
                    idx = word[:(len(word) - 1)] + "*"
                else:
                    idx = word[:i] + "*" + word[i + 1:]
                if idx in adjList:
                    adjList[idx].add(word)
                else:
                    adjList[idx] = set([word])
        visited = set([beginWord])
        q = deque()
        q.append(beginWord)
        ans = 0
        while q:
            ans += 1
            length = len(q)
            for j in range(length):
                curr = q.popleft()
                visited.add(curr)
                if curr == endWord:
                    return ans
                for i in range(len(curr)):
                    if i == 0:
                        idx = "*" + curr[1:]
                    elif i == len(curr) - 1:
                        idx = curr[:len(curr) - 1] + "*"
                    else:
                        idx = curr[:i] + "*" + curr[i + 1:]
                    adjWords = adjList[idx]
                    for word in adjWords:
                        if word not in visited:
                            q.append(word)
        return 0