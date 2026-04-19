class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for key,v in freq.items():
            heap.append((v,key))
        heapq.heapify(heap)

        while len(heap) != k:
            heapq.heappop(heap)

        return [num for count, num in heap]