class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        if i use bars height as height of the rectangle, how wide can i stertch it?

        monotonic stack of indices, increasing height.
        once we hit a lower hit, then we know the right height limit.
        we also need to know the left height limi.t how do we know that?
        pop off the top (curr height we are anaylzing)
        well its the thing on the top of our stack right now since its smaller than the one we popped.
        calcuate height of that.
        then move on.
        """
        stack = []
        max_area = 0
        heights.append(0)
        for i,h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                left_idx = stack[-1] if stack else -1
                width = i - left_idx - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        return max_area


