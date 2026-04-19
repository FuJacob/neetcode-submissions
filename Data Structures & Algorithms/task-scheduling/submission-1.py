class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        youre given array of CPU tasks tasks, where tasks[i] is an uppercase english char from A -> Z
        youre also given integer n

        each CPU cycle allwos completion of a single task
        and tasks may be completed in any order

        identical tasks must be spereated by least n CPU cycles

        return min number of CPU cycles required to complete all takss
        """
        time = 0
        freq = Counter(tasks)
        ## max heap
        ## oh 
        heap = [-x for x in freq.values()]
        heapq.heapify(heap)
        q = deque()  # Queue to store tasks in cooldown: each element is (available_time, remaining_count)


        ## so while we have shit in the q or the heap
        while q or heap:
            ## count as 1 cycle
            time+=1

            if heap:
                count = heapq.heappop(heap)
                ## it's negative
                ## decrement
                count +=1
                if count != 0:
                    ## add to q for cooldown 
                    q.append((time+n, count))
            
            if q and q[0][0] == time:
                _, ready_count = q.popleft()
                heapq.heappush(heap, ready_count)
        return time


        