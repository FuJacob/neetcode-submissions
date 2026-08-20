class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ## window size of s1
        ## check if freqs = freq?  26
        m,n = len(s1), len(s2)
        left = 0
        s1_char_to_freq = defaultdict(int)
        window_char_to_freq = defaultdict(int) 
        
        for c in s1:
            s1_char_to_freq[c] +=1
    
        for right, c in enumerate(s2):
            window_char_to_freq[c] +=1
            if right - left + 1 > m: ## too big
                window_char_to_freq[s2[left]] -=1
                if window_char_to_freq[s2[left]] <= 0:
                    del window_char_to_freq[s2[left]]
                left +=1
            if s1_char_to_freq == window_char_to_freq:
                return True

        return False

