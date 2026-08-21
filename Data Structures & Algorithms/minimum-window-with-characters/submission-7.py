class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def get_idx(c):
            if c.isupper():
                return ord(c) - ord('A')
            return ord(c) - ord('a') + 26

    
        m,n = len(s), len(t)
        if m < n:
            return ""
        need = [0] * 52
        for c in t:
            need[get_idx(c)] +=1

        window = [0] * 52
        left = 0
        shortest_substring = ""
        shortest_length = float('inf')
        for right, c in enumerate(s):
            c_ord = get_idx(c)
            if need[c_ord] > 0:
                window[c_ord] +=1
            
            while left < m:
                left_ord = get_idx(s[left])
                if need[get_idx(s[left])] == 0:
                    left+=1
                elif window[get_idx(s[left])] > need[get_idx(s[left])]:
                    window[left_ord] -= 1
                    left+=1
                else:
                    break
            
            curr_length = right - left + 1
            if shortest_length > curr_length:
                is_answer = True
                for need_count, window_count in zip(need,window):
                    if window_count < need_count:
                        is_answer = False
                        break
                if is_answer:
                    shortest_substring = s[left:right+1]
                    shortest_length = curr_length
        return shortest_substring


        