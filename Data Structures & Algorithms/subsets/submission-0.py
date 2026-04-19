class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ## sol
        ## holds answer
        sol = [[]]
        ## curr to hold curr one of the sols
        curr = []
        ## backtrack function like dfs
        ## is take in index for what it starts at 
        def backtrack(start):
            ## what's base case
            ## well when length of curr is maxed ouet so then we can add it then return

            for i in range(start, len(nums)):
            ## add whatever option rn
                curr.append(nums[i])
                ### ohh because we need to make copies bro
                ## rmmbere to alwasys make copies bro of arrays or yojull keep mutating same one
                sol.append(curr[:])
                ## add to sol
                ## backtrack to get more optiobns
                ## start + 1 now to get more optoins since we canonly awnt subsets
                ## it woidl be i, i starting at start bruv, 
                ## i are our options, so we would do i. + 1.     , , not start bruv,
                ## otherwise 
                backtrack(i + 1)
                ## pop off now to backtrack
                curr.pop()
            ## base case
            ## when is it over and we have a sol?
            ## well we want subsets so honestly we want ot keep adding it to sol 
        ### BUTT we don't want is duplicate subets
        ## so how do we solve this probkleM?
        ## just anways start building from idx can only pick eleemnts from x idx past
        ## so wont get 2 3 and 3 2 , canonly pick elemens from forward


        ## now usualy iterate thru options
        ## so we have ##optinos = len of nums
        ##. but we dont want tdupklciates s, force to ostart at idx
        
        backtrack(0)
        return sol
                

        