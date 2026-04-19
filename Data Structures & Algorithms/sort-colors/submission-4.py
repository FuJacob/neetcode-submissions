class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, blue, ptr = 0, len(nums)-1, 0
        while ptr <= blue: 
            if nums[ptr] == 0:
                nums[red], nums[ptr] = nums[ptr], nums[red]
                red+=1
            elif nums[ptr] == 2:
                nums[blue], nums[ptr] = nums[ptr], nums[blue]
                blue-=1
                continue
            ptr+=1
