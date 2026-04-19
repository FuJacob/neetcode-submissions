class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            key = ".".join(list(map(lambda x:str(x), freq)))
            if key in seen:
                seen[key].append(s)
            else:
                seen[key] = [s]
        
        ans = []
        for group in seen.values():
            ans.append(group)
        return ans


