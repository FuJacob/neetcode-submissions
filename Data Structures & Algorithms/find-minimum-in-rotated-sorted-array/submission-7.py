class Solution:
    def findMin(self, nums: List[int]) -> int:
        ### youre given array of length n whih was orignally sorted in ascending order
        ## it's now been rotated bw 1 and n times
        ## so ortaitng array 4 times = moving last 4 elelemts pof thje array to the beginning
        ## rotating the array 6 times produces the orignal array
        ## all nums are unique, return the minimum element of this array
        ## well o of n way is just use min function find min or just have glob min and iterate thru finding the min element
        ## we want to do this in o log n. log n suggests binary search.
        ## hmm
        ## how would we do this in binary search?
        ## we know it was oringalyl sorted in ascending order.  as you can see, it was rotated some nubmer of times though.
        ## however the order is still techincally intact
        ## well i think, if we check and see that the next element that we mvoe onto, is less than the one before
        ## that suggests that that's where it was suppose to actually start if u know what i mean
        ## so what if we just iterate until this happens? what if we check this case from both start and finish
        ## is that o logg n time complexicicty
        ## well yes because we iterate thru array twice as fast essientally.
        ## maybe also keep glob min
        ## i did it compeltely wrong 
        ## the min is the pivot point
        """
        so if we do binary search
        all we want to do jst find the middle
        then we can check mid
        if nums mid is greater than nums right that means the pivot point is somewhere between mid and right
        else it's in the left half

        """

        l, r = 0, len(nums) -1

        while l < r:
            m = l + (r-l) // 2
            if nums[m] > nums[r]:
                ## this must mean the pivot is somewhere between m and r
                ## right half
                l = m + 1
            ## else it;s in the left half, incl possibly middle
            else:
                r = m
        ## end up returning left once l == r then we know we foudn the pivot
        ## while l < r not l <= r bdcause we will get inf loop. why? lowkey i dont know 
        return nums[l]
            