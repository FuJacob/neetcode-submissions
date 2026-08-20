class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0
        char_to_freq = defaultdict(int)
        start = 0
        for i,c in enumerate(s):
            char_to_freq[c] += 1
            ## case maybe our window too far, and now its to omany non known cjhars
            ## while most freq + k < window length, keep removing andd showrtening thte window
            while max(list(char_to_freq.values())) + k < i - start + 1:
                char_to_freq[s[start]] -= 1
                start+=1
            ## at this poitn, we haev valid window
            length = max(length, i - start + 1)
        return length



