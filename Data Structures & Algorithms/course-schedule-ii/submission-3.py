class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseToPrereq = [[] for _ in range(numCourses)]
        prereqCounts = [0] * numCourses
        for entry in prerequisites:
            x, y = entry
            courseToPrereq[x].append(y)
            prereqCounts[y] += 1

        res = []
        
        q = deque()
        for i in range(numCourses):
            if prereqCounts[i] == 0:
                q.append(i)
        finished = 0
        while q:
            curr = q.popleft()
            res.append(curr)
            finished += 1

            for i in courseToPrereq[curr]:
                prereqCounts[i] -= 1
                if prereqCounts[i] == 0:
                    q.append(i)
        return res[::-1] if finished == numCourses else []