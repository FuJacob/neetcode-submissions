class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ## we can use a heap
        ## keep the length of our heap at k
        ## max heap
        heap = list(map(lambda x:-x, nums))
        heapq.heapify(heap)
        for i in range(k-1):
            heapq.heappop(heap)
        return -heap[0]
        