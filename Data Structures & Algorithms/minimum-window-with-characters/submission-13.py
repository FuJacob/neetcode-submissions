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
        required = len(need)
        for right, c in enumerate(s):
            window[c] += 1
            if window[c] == need[c]:
                satisfied +=1
            
            while satisfied == required:
                if right - left < best_right - best_left:
                    best_right, best_left = right,left

                if s[left] in need:
                    window[s[left]] -=1

                    if need[s[left]] > window[s[left]]:
                        satisfied -= 1
                left+=1

        return s[best_left: best_right + 1] if best_right != float('inf') else ""
                
