class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = Counter(s1)
        n = len(s1)
        seen = defaultdict(int)
        l = 0
        for idx, char in enumerate(s2):
            seen[char] += 1
            while idx - l + 1 > n:
                seen[s2[l]] -= 1
                if seen[s2[l]] == 0:
                    del seen[s2[l]]
                l+=1
            if idx - l + 1 == n:
                if freq.items() == seen.items():
                    return True
        return False






