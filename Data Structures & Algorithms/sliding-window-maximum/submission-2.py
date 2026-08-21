class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
         maximum element in the window
         lazy deetion
         1 heaps
         heap  -> biggest elem -> + idx
         (1,0)
         (2,1)
        """
        delete = set()
        n = len(nums)
        heap = []
        left = 0
        ans = []
        for right, num in enumerate(nums):
            heapq.heappush(heap, (-num, right))

            window_length = right - left + 1
            if window_length < k:
                continue
            if window_length > k:
                delete.add((-nums[left], left))
                left+=1
                
            while heap and heap[0] in delete:
                heapq.heappop(heap)
            ans.append(-heap[0][0])
        return ans


