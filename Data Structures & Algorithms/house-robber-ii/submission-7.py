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
        def max_money(money):
            n = len(money)
            rob = [0] * n
            no_rob = [0] * n
            rob[0] = money[0]
            for i in range(1, n):
                rob[i] = no_rob[i-1] + money[i]
                no_rob[i] = max(no_rob[i-1], rob[i-1])
            return max(no_rob[-1], rob[-1])
        return max(max_money(nums[1:]),max_money(nums[:-1]))

