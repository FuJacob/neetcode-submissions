class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        keep hashmap, of chars we've seen before in our window
        dynamic
        keep longest global
        if we find duplicate, then what? should bring pointer to the last iteration of the duplicate + 1 i think....
        so then we can keep going
        """

        if not s: return 0
        seen = {}
        longest = 0
        l = 0
        for idx, c in enumerate(s):
            if c in seen:
                ## need ot rmeove alll prev from hashmap till
                t = seen[c]
                while l != (t + 1):
                    del seen[s[l]]
                    l+=1
            else:
                longest = max(idx - l + 1, longest)
            seen[c] = idx
        return longest





        