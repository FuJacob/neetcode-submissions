class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ## given array nums of unique integers
        ## we want to:
        ## return all possible permutations
        ## classic backtracking problem because at each time, we have choices we can make
        ## it builds a decision tree
        ## essientally dfs
        ## we'll make a solution array to hold our permutations
        sol = []
        ## then we'll make a curr array to hold our current permutation
        curr = []

        ## then we'll make the backtracking function which would be used recursively
        ## it will take in start idx, which represnets which idx our decisions can start
        ## picking from since we wan't to do permutations
        def backtrack(arr):
            ## in our recursive function, there is always a basecase. when do 
            ## we want to end a branch?
            ## when all numbers are used of course
            if len(curr) == len(nums):
                ## then we want to store the answer
                ## make a copy of curr so it is not referencing the same array
                sol.append(curr[:])
                ## prune the branch

            ## then what we want to do is evaluate our options
            ## we know permutations, cannot repeat of use of characters
            ## so we will evaluate or remainign options from the start idx
            for i in range(len(arr)):
                ## then what we want to do now is have our otion
                curr.append(arr[i])
            ## then we'll check out this branch further on
                backtrack(arr[:i] + arr[i+1:])
            ## then backtrack
                curr.pop()
        backtrack(nums)
        return sol


        