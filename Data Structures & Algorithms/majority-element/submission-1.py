class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        cand = nums[0]
        for i in range(1, len(nums)):
            if cand == nums[i]:
                count+=1
            else:
                count-=1
                if count == 0:
                    cand = nums[i]
                    count =1
        return cand
