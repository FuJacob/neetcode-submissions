class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        given string s, return # of substrings within s that are palindromes
        ## of substrings

        within s that are pladinreoms 

        ## of strings ithint s
        try differnet lenghts 
        how many substrings do we have within this range?

        its bascially how many plaidorneoms do we have fro, i to j
        thats the funal answer
dp i k reprenetsn # of paldiromes within this range
whats the recurrance relation
we need ot know actually the palidrome or not 
to build off of that.
prob have bool araray if paldirome or not 

then jsut count 


        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = n
        for i in range(n):
            dp[i][i] = True
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i+length-1
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j]:
                    count+=1
        return count
                    
            
