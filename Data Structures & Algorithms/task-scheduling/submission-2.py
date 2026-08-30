class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        minCPU, taskCnts = 0, Counter(tasks)

        maxHeap = [ count for count in taskCnts.values() ]
        heapq.heapify_max(maxHeap)
        queList = deque()

        while maxHeap or queList:
            minCPU += 1
            if maxHeap:
                task = heapq.heappop_max(maxHeap) - 1
                if task: 
                    queList.append((task, minCPU + n))
            if queList and queList[0][1] == minCPU:
                task, dumb = queList.popleft()
                heapq.heappush_max(maxHeap, task)
        
        return minCPU


