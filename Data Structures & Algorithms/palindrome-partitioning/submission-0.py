class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        okay we're given string s
        we want to split s into substrings where very substring is a palindrome


        return all possible lists of palindromic substrinsg

        return solution in any order

        what is palindrome?
        same characters goign forwards and backwards

        at each step we have decision to include the next letter or not. we shoudl
        only do so if it' still allows for palindrome.

        once we add it we watn to recruse, then backtrack to explroe other optinos of not including it
        

        we cannot reuse the other chars brh 
        """
        def isPalidrome(s):
            return s == s[::-1]
        ans = []
        curr = []
        def backtrack(start):
            ## base case
            ## assuming curr is a valid option we awnt toj ust append
            ### we want to stop once we run out of characters
            if start == len(s):
                ans.append(curr[:])
                return
            
            ## then we want ot explroe all the options
            ## which is ltierally whether to include a the char our pointer is currently on or not
            ## if we choose ot include we want ot check whetehr it's stil la palidrnome tho.
            ## we can do 2 pointers from whatever was the beginnig of curr
            ## try every possible substring starting at start
            for end in range(start+1, len(s) + 1):
                substr = s[start:end]
                if isPalidrome(substr):
                    curr.append(substr)
                    backtrack(end)
                    curr.pop()
        backtrack(0)
        return ans
        