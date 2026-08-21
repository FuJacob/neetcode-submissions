class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
         maximum element in the window
         lazy deetion
         1 heaps
         heap  -> biggest elem -> + idx
         (1,0)
         (2,1)
         ## we dont need delet set at lal ecause anything ot left of our window can just be diseted
        """
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
                left+=1
            while heap and heap[0][1] < left:
                heapq.heappop(heap)
            ans.append(-heap[0][0])
        return ans


