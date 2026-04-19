class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ## seems to be related to backtracing
        ## essientalyl youre given choice iot pick nubmer every time  and need sol of unique combos of nums
        ## where the chosen numb sum up to target
        ## we will implment backtracking sol
        ## sol array
        ## curr array
        ## backtrack recursive function
        ## takes 

        sol = []
        curr = []
        ## we dont want duplciates, so take in start index too
        ## while still allowing for same number chocsen as man times
        ## this way we ca build the trees for every combo but by enforcing need to move forward we ca
        ##
        ## this way it can still use te same number multiple tmes but need always move fowrard
        def backtrack(start, curr_sum):
            ## base case is if sum is equal to target
            if curr_sum == target:
                sol.append(curr[:])
                return
            
            ## go thru options
            ## can use any num unlimited times

            for i in range(start, len(nums)):
                if curr_sum + nums[i] <= target:
                    ## don;'t increment i, otherwise that won't let same num be reused
                    ## instead just leave as i and when we iterate thru other optins it gets to recuse
                    ## thats hte fukng sum curr is the aray ekep track wat nums acutally used
                    curr.append(nums[i])
                    backtrack(i, curr_sum + nums[i])
                    curr.pop()
        
        backtrack(0, 0)
        return sol
        