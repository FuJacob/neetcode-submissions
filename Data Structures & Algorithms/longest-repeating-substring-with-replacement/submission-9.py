class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0
        char_to_freq = defaultdict(int)
        left = 0
        for right,c in enumerate(s):
            char_to_freq[c] += 1
            while max(char_to_freq.values()) + k < right - left + 1:
                char_to_freq[s[left]] -= 1
                left+=1
            length = max(length, right - left + 1)
        return length



