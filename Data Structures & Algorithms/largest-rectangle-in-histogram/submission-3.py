class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        for idx, h in enumerate(heights + [0]):
            start = idx ## this is the start
            while stack and stack[-1][1] > h:
                top_start, top_height = stack.pop()
                width = idx - top_start
                ans = max(top_height * width, ans)
                ## then what? 
                start = top_start ## we can inherit this since we are simaller
            stack.append((start, h))
        return ans