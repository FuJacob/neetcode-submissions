class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        given s 
        dicotnairy strings wordDict

        return True if s can be broken into space epreate sueqnce of ditonary words

        reuse words
        all unique

        neetcode
        dp i reprenstes withere u can split word into dictniary words or not  by length s i 
        dp i respesnts if. try every word, right, if u can split eg if word len n 
        dp i- n cna u split this into words?

        dp[0] = in there or not 
        dp [1] tr every word - if its big enough
        ngl we wanna try base case instead i think with lenght so no need manual handle first case


        """
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            for word in wordDict:
                if i - len(word) >= 0:
                    past_word = s[i-len(word):i]
                    if past_word == word and dp[i-len(word)]:
                        dp[i] = True
                        break
        return dp[n]



