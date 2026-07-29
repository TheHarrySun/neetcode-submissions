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
        
        wait_heap = []
        heapq.heapify(wait_heap)
        while task_heap or wait_heap:
            res += 1
            for entry in wait_heap:
                entry[0] -= 1
            if task_heap:
                val, key = heapq.heappop(task_heap)
                val = val + 1
                if val != 0:
                    heapq.heappush(wait_heap, [n, val, key])
            
            while wait_heap and wait_heap[0][0] == 0:
                _, val, key = heapq.heappop(wait_heap)
                heapq.heappush(task_heap, [val, key])
        return res