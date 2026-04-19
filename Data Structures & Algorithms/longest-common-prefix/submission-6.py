class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        ans = ""
        ptr = 0
        for ptr in range(len(word)):
            for i in range(1,len(strs)):
                if ptr >= len(strs[i]) or word[ptr] != strs[i][ptr]:
                    return word[:ptr]
        return word