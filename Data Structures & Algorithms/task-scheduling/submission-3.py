class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        task_to_freq = Counter(tasks)
        heap = [-freq for freq in task_to_freq.values()]
        heapq.heapify(heap)
        cooldown = deque()
        while heap or cooldown:
            time +=1
            if heap:
                count = heapq.heappop(heap)
                count +=1

                if count < 0:
                    cooldown.append((time+n, count))
            ## next heap is. too much
            if cooldown and cooldown[0][0] == time: ## 0?
            ## done cooldonw 
                _, count = cooldown.popleft()
                heapq.heappush(heap, count)
        return time