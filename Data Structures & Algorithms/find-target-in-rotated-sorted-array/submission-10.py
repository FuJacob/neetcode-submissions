class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        we're given array of length n orignaly sorted in ascending order
        it's been rotated

        given rotated soeted arary nums and integer target , return index of target in nus mor -1 if not present
        all numbers are unique
        o log n binary search
        """

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r)//2
            if nums[m] == target:
                return m
            ## else find which side is sorted man
            ## that means it's sorted here true
            if nums[l] <= nums[m]:
                ## same here then bruhv
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    ## check right side
                    l = m + 1
            else:
                ## check the fuckign inclsuive r i guess cuz it could laos be the target
                if nums[r] >= target > nums[m]:
                    l  = m + 1
                else:
                    ## check left side
                    r = m - 1

        return -1


        