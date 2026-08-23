class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        curr = []
        def backtrack(num_open, num_close):
            if num_open == num_close == n:
                ans.append("".join(curr))
                return
            if num_open > n or num_close > n:
                return

            curr.append("(")
            backtrack(num_open+1, num_close)
            curr.pop()

            if num_open > num_close:
                curr.append(")")
                backtrack(num_open, num_close+1)
                curr.pop()
        backtrack(0,0)
        return ans