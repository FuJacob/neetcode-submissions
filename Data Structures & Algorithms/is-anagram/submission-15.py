class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = Counter(s)
        freqT = Counter(t)
        if len(freqS) != len(freqT):
            return False
        for char in freqT.keys():
            if freqT[char] != freqS[char]:
                return False
        return True
        
