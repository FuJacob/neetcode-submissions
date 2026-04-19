class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        tallest_left = tallest_right = 0
        water = 0
        while l <= r:
            if tallest_left < tallest_right:
                if tallest_left > height[l]:
                    water += tallest_left - height[l]
                tallest_left = max(height[l], tallest_left)
                l+=1
            else:
                if tallest_right > height[r]:
                    water += tallest_right - height[r]
                tallest_right = max(height[r], tallest_right)
                r-=1
        
        return water