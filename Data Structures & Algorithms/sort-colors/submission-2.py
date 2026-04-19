class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        red = 0
        blue = n - 1
        ptr = 0
        while ptr <= blue:
            if nums[ptr] == 0:
                nums[red], nums[ptr] = nums[ptr], nums[red]
                red+=1
                ptr+=1
            elif nums[ptr] == 2:
                nums[blue], nums[ptr] = nums[ptr], nums[blue]
                blue-=1
            else:
                ptr+=1
