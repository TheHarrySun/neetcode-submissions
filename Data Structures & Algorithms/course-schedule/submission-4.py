class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToPrereq = {}
        for i in range(numCourses):
            courseToPrereq[i] = []
        
        for pair in prerequisites:
            a, b = pair
            courseToPrereq[a].append(b)

        visited = set()

        def dfs(c):
            if c in visited:
                return False
            if not courseToPrereq[c]:
                return True
            visited.add(c)
            for entry in courseToPrereq[c]:
                if not dfs(entry):
                    return False
            visited.remove(c)
            courseToPrereq[c] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
                
        return True