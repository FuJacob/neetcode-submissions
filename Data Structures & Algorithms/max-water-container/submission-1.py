class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0
        l,r = 0, n - 1
        while l < r:
            width = r - l
            height = min(heights[r], heights[l])
            ans = max(ans, height *width)

            if heights[r] == heights[l]:
                r -=1
                l +=1
            elif heights[r] > heights[l]:
                l +=1
            else:
                r-=1
        return ans