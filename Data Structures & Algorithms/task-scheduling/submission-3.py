class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0
        task_heap = []
        heapq.heapify(task_heap)
        counts = {}
        
        for task in tasks:
            counts[task] = 1 + counts.get(task, 0)
        
        for key, val in counts.items():
            heapq.heappush(task_heap, [-val, key])
        
        wait_q = deque()
        while task_heap or wait_q:
            res += 1
            for entry in wait_q:
                entry[0] -= 1
            if task_heap:
                val, key = heapq.heappop(task_heap)
                val = val + 1
                if val != 0:
                    wait_q.append([n, val, key])
            
            while wait_q and wait_q[0][0] == 0:
                _, val, key = wait_q.popleft()
                heapq.heappush(task_heap, [val, key])
        return res