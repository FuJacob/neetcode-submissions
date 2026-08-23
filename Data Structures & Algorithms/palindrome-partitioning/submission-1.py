class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)
        curr = [] ## hold each list 
        def is_palindrome(s):
            l,r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        def backtrack(start):            
            if start >= n: ## if were were too big
                ans.append(curr[:]) ## now we. are done.
                return
        
            for i in range(start,n): ## othewise
                if is_palindrome(s[start:i+1]):
                    curr.append(s[start:i+1])
                    backtrack(i+1) ## + 1 after dumb fuck
                    curr.pop()
        backtrack(0)
        return ans