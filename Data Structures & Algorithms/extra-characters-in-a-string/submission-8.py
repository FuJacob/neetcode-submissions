class TrieNode:
    def __init__(self, is_word = False):
        self.is_word = is_word
        self.children = {}

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [n] * (n+1)
        root = TrieNode()
        for word in dictionary:
            ptr = root
            for c in word:
                if c not in ptr.children:
                    ptr.children[c] = TrieNode() 
                ptr = ptr.children[c]
            ptr.is_word = True

        dp[n] = 0
        for i in range(n-1,-1,-1):
            ptr = root
            for j in range(i, n):
                dp[i] = min(dp[i], j- i + 1 + dp[j+1]) 
                if s[j] not in ptr.children:
                    break
                ptr = ptr.children[s[j]]
                if ptr.is_word:
                    dp[i] = min(dp[i], dp[j+1]) 
        return dp[0]










