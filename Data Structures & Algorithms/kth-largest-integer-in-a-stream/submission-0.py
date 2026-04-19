class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = list(map(lambda x: -x, nums))
        self.k = k
        heapq.heapify(self.heap)

        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        ## kth largest int
        ## i.e we want to keep popping top k - 1 th times, then returh
        ## this is slow, how about keeping min heap, max length k return head
        nums2 = []
        for _ in range(self.k - 1):
            nums2.append(heapq.heappop(self.heap))
            
        ans = -self.heap[0]
        for i in range(len(nums2)):
            heapq.heappush(self.heap, nums2[i])
        return ans


        
