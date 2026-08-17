class Solution:
    """

nums=[-1,0,1,2,-1,-4]
-4 -1 -1 0 1 2
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        for idx, num in enumerate(nums):

            if idx > 0 and num == nums[idx-1]:
                continue
            l, r = idx+1, n - 1

            target = -num
            while l < r:
                if l > idx + 1 and nums[l] == nums[l-1]: ## ened this to skip duplciate if we inner finds anotehr
                    l+=1
                    continue
                if r < n - 1 and nums[r] == nums[r+1]: # same for righ side coudl be move and find duplciate too 
                    r-=1
                    continue
                curr = nums[l] + nums[r]
                if curr == target:
                    ans.append([num, nums[l], nums[r]]) ## euqal? who do we move? move obth
                    r -=1
                    l += 1
                    ## we dont have any other idea of combo
                elif curr > target:
                    r -=1
                else:
                    l+=1
        return ans