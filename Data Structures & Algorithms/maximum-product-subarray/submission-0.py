class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        given nums
        find subarray
        - that has the largest product within the array
        - return it
        max and min

        at each oidnex we track 2 things
        the max prodcut we can get 
        and the min prodcut we can get 
        ciz then ther max is either we min smash or max smash 
        why? cuz negaitve * negaitve postiive
        dp[0][0] = nums[i]

        ## largest produt within teh array
        ## maxprod i repsentes maximm prodcut you cna make incl i
        """
        n = len(nums)
        max_prod = [float('-inf')] * n
        min_prod = [float('inf')] * n
        max_prod[0] = min_prod[0] = nums[0]
        for i in range(1, n):
            new_max_prod = max_prod[i-1] * nums[i]
            new_min_prod = min_prod[i-1] * nums[i]
            max_prod[i] = max(nums[i], new_max_prod, new_min_prod)
            min_prod[i] = min(nums[i], new_min_prod, new_max_prod)
        return max(max_prod)