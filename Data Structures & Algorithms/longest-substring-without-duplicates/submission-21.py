class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest = 0
        l = 0
        for idx, c in enumerate(s):
            if c in seen and seen[c] >= l:
                l = seen[c] + 1
            longest = max(longest, idx - l + 1)
            seen[c] = idx
        return longest