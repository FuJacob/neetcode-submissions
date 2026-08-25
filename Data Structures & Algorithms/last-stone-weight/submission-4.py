class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) > 1:
            x,y = heapq.heappop(heap), heapq.heappop(heap)
            x,y = -x,-y
            if x < y: 
                heapq.heappush(heap, -(y-x))
            elif y < x: 
                heapq.heappush(heap, -(x-y))
            
        return 0 if not heap else -heap[0]

