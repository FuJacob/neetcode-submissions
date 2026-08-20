class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        char_to_idx = {}
        start = 0
        n = len(s)
        for i, c in enumerate(s):
            if c in char_to_idx:
                new_start = char_to_idx[c]
                while start < n and new_start >= start:
                    del char_to_idx[s[start]]
                    start+=1
            char_to_idx[c] = i
            longest = max(longest, i - start + 1)
        return longest



        