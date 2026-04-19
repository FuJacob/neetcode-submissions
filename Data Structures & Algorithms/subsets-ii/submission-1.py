class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ## given array nums of integers
        ## can have duplicates
        ## return all possible subsets
        ## soltion must not have duplicate subsets

        sol = []
        curr = []
        ## right now the issue is we are duplcating susbsets bcuz thereye's duplciate nubmers
        ## i thin kwe can sort the array beforehand
        ## then we can make isre to check to make sure that the last number wasnt same, cuz iif it was then it wouldve
        ## covered all the possible subsets already 
        nums.sort()
        def backtrack(start):
            sol.append(curr[:])
            for i in range(start, len(nums)):
                ## i greaterh tna start not 0 , otherwise that wioudl ill off valid branches cuz then u kill no matter if it's duplciated next, by doing start we make it able to take it as long as its not same branch????? yeae 
                if i > start and nums[i - 1] == nums[i]:
                    continue
                curr.append(nums[i])
                backtrack(i+1)
                curr.pop()
        backtrack(0)
        return sol
        