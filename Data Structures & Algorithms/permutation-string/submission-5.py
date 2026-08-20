class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n = len(s1), len(s2)
        if m > n:
            return False
        
        left = 0
        char_freq = [0] * 26
        window_freq = [0] * 26
        for i in range(m):
            char_freq[ord(s1[i]) - ord('a')] +=1
            window_freq[ord(s2[i]) - ord('a')] +=1
    ## forgot to do a check here incase we alrdy got the answer for first one 
        if char_freq == window_freq:
            return True
        for i in range(m, n):
            window_freq[ord(s2[i]) - ord('a')] +=1
            window_freq[ord(s2[i-m]) - ord('a')] -=1
            if window_freq == char_freq:
                return True

        return False
