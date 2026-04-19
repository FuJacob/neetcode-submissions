class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        youre given 2d array points
        points[i] = [xi, yi] represents the coordinates of a point 
        on x-y axis

        also integer k

        return k cloest points to orign (0,0)

        we want the k closest points
        so i think we could use a heap, and the top of hepa is farthest poitn, so basically maxheap
        we have the formula

        then waht we can do is keep popping off the heap until we have k elemetns left,t which we can return
        since that means its the k cloest
        """
        def dist(point):
            return math.sqrt(point[0] ** 2 + point[1] ** 2)
        heap = [(-dist(point), point) for point in points]
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        ans = [e[1] for e in heap]
        return ans


