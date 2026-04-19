class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        curr = []

        def backtrack(o,c):
            ## base case
            if len(curr) == 2*n:
                ans.append("".join(curr[:]))
                return
            ## valid
            ## check open v close
            ## if adding one more close is over the curr open ones
            if o < n:
                ## always add if o is less than cuz it woudl always be valid
                curr.append("(")
                backtrack(o+1, c)
                curr.pop()
            ## same here if c is less than open
            if c < o:
                curr.append(")")
                backtrack(o, c+1)
                curr.pop()
        backtrack(0,0)
        return ans

            


        