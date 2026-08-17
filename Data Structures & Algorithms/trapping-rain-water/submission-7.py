class Solution:
    def trap(self, height: List[int]) -> int:
        ## monotnic stack
        ## decreasing
        ## keep track (idx, biggest so far (incl it))
        ## if hit bigger, we know limitnig now we can start solving how much water
        # n = len(height)
        # l,r = 0, n - 1 
        # biggest_left, biggest_right = height[l], height[r]
        # ans = 0
        # while l <= r:
        #     biggest_left = max(biggest_left, height[l])
        #     biggest_right = max(biggest_right, height[r])
        #     if biggest_left > biggest_right:
        #         ans += biggest_right - height[r]
        #         r-=1
        #     else:
        #         ans += biggest_left - height[l]
        #         l+=1
        # return ans

        stack = []
        ans = 0
        for idx, h in enumerate(height):
            while stack and height[stack[-1]] <= h:
                top_idx = stack.pop()
                if not stack: 
                    break
                width = idx - stack[-1] - 1
                min_height = min(h, height[stack[-1]]) - height[top_idx]
                ans += width * min_height
            stack.append(idx)
        return ans
                




