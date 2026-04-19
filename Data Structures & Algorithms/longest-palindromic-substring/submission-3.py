class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        given string s return longert sbustring s that is a palidrome.
        read torwad and backward.
        LONGEST SUBSTRING

        IE WE CAN SKIP ? 
        yes.
        what does this mean
        IE matching left and teh reverse
        SEE HOW MANY WE CAN GET MATCH BY THEN. the longest substring

        s
        reverserd s
        create 2d array
        if match, then take which one is longer? 
        how do we know what that string is tho
        store the stupid string? then fetch count when need be?

        dp ij represnets the longest substring that is palindrome

        ohhhh
        i orembmer now 
        we bascally check every possible length of substrin to see if ti worsk or not

        1, 2 ,3 , 4
        try each window see if its a panidrome.
        then this way we can store booleans instead of the acutal string so we know if a a range is a pladirome or not 
        if it is, the nwe can probably incrlement lengh

        """
        n = len(s)
        ## 2d array. index start and index end
        dp = [[False] * n for _ in range(n)]
        ## base case, all length ones, they are paldrines
        for i in range(n):
            dp[i][i] = True
        ## dont double check
        ## max len always to be 1 bro 
        start = 0
        max_len = 1
        for length in range(2, n+1):
            for i in range(n- length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                    ## if we ahve a apldrime so far
                    ## not wiethehr if current works or not
                if dp[i][j] and length > max_len:
                    max_len = length
                    start = i
        return s[start:start+max_len]
        




        

        