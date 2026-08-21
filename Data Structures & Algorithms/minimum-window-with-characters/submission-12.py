class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m,n = len(s), len(t)
        if m < n:
            return ""
        need = defaultdict(int)
        window = defaultdict(int)
        satisfied = 0 ## satisfied frequenceis
        left = 0

        ## fill in need
        best_left = 0
        best_right = float('inf')
        for c in t:
            need[c] += 1
        for right, c in enumerate(s):
            if c in need:
                window[c] +=1
                if window[c] == need[c]:
                    satisfied +=1
            ## lets see if we can cut down the length or overflow
            while left < m:
                if s[left] not in need: # we dont need
                    left+=1
                elif window[s[left]] > need[s[left]]:
                    ##o verlfow
                    window[s[left]] -= 1
                    left+=1
                else:
                    break
            

            if satisfied == len(need) and best_right - best_left > right - left:
                best_left, best_right = left, right

        return s[best_left:best_right+1] if best_right != float('inf') else ""

            