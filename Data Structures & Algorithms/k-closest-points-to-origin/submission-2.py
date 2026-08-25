class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_dist_to_origin(x,y):
            return math.sqrt(x**2 + y**2)
        heap = []
        for x,y in points:
            heapq.heappush(heap,(-get_dist_to_origin(x,y), (x,y)))

            while len(heap) > k:
                heapq.heappop(heap)
        return [[x,y] for _,(x,y) in heap]
        
        
