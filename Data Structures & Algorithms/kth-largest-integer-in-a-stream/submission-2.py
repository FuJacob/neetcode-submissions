class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)

        ## so we pop off the undeeded elenents wihch is fine
        ## cuz we dont acutally need them since we know
        ## what k is wanted already
        ## this popping will remove the smallest elements until we have k numbers thus 
        ## kth largest is going to be the root

        while len(self.heap) > k:
            heapq.heappop(self.heap)

        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


        
