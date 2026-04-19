class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        ans = ""
        ptr = 0
        while ptr < len(word):
            for i in range(1,len(strs)):
                if ptr >= len(strs[i]) or word[ptr] != strs[i][ptr]:
                    return ans
            ans += word[ptr]
            ptr+=1
        return ans