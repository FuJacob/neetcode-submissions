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
        largest = 0
        for i,h in enumerate(heights + [0]):
            while stack and h < heights[stack[-1]]: ## increasing 
                curr_height = heights[stack.pop()]
                left_idx = stack[-1] if stack else -1 # ???? why
    ## - 1 cuz we dont include  the boundaries 
                largest = max(largest, curr_height * (i - left_idx - 1))
            stack.append(i) ##Always append
        
        return largest


