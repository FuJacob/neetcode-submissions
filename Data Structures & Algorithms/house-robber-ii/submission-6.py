class Solution:
    def rob(self, nums: List[int]) -> int:
        ## 2 arrays
        ## use index math to cehck if it loops?
        ## iterate thru
        ## check all once hit end.
        ## ok 
        n = len(nums)
        if n <= 1:
            return nums[0]
        def max_money(start, end):
            rob = [0] * (n-1)
            not_rob = [0] * (n-1)
            rob[0] = nums[start]
            for i in range(start, end):
                rob[i-start] = not_rob[i-1-start] + nums[i]
                not_rob[i-start] = max(not_rob[i-1-start], rob[i-1-start])
            return max(rob[-1], not_rob[-1])
        return max(max_money(1,n), max_money(0,n-1))

