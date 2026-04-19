class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        h=[]
        ans=[]
        tfm_tasks = [(et,pt,i) for i, (et,pt) in enumerate(tasks)]
        tfm_tasks.sort()
        curr_time = 0
        i=0
        n = len(tasks)
        ## instead of 1 at a time, we ca do while 
        while i < n or h:
            ## if not h and the curr time is less thean the et
            if not h and curr_time < tfm_tasks[i][0]:
                curr_time = tfm_tasks[i][0]
        
            while i < n and tfm_tasks[i][0] <= curr_time: ## these guys are ready
                heapq.heappush(h, (tfm_tasks[i][1], tfm_tasks[i][2]))
                i+=1
            ## lets do nxt task
            pt, idx = heapq.heappop(h)
            ans.append(idx)
            curr_time += pt
    
        return ans




