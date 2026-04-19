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
            if c in seen and seen[c] >= l:
                ## need ot rmeove alll prev from hashmap till
                ## prev stuck on faulty logic error, if we move left pointer over, we need to update our hashmap to remove the older iterations of the
                l = seen[c] + 1
            longest = max(idx - l + 1, longest)
            seen[c] = idx
        return longest





        