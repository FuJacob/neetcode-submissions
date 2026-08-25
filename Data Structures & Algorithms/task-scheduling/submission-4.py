import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_to_freq = defaultdict(int)
        for task in tasks:
            task_to_freq[task] +=1
        heap = [-freq for freq in task_to_freq.values()] ## counts
        heapq.heapify(heap)
        ## max heap more freq
        time = 0
        cooldown = deque([]) ## queue for cooldonw
        ## (timeto ready, freq)
        while heap or cooldown: 
            time +=1
            if cooldown and cooldown[0][0] == time:
                _, freq = cooldown.popleft()
                heapq.heappush(heap, freq) 
            if heap: ## vali ready ot use
                freq = heapq.heappop(heap)
                freq += 1 ## down one
                if freq < 0:
                    cooldown.append((time+n+1, freq))
        return time