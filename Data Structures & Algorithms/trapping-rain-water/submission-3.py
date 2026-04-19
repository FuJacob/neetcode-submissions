class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        tallest_left = tallest_right = 0
        water = 0
        while l <= r:
            tallest_left = max(height[l], tallest_left)
            tallest_right = max(height[r], tallest_right)
            
            ## which side can we calcuate 
            if tallest_left < tallest_right:
                water += max(0,tallest_left - height[l])
                l+=1
            else:
                water += max(0,tallest_right - height[r])
                r-=1
        
        return water