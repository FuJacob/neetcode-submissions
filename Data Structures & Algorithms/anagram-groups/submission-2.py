class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            key = list(s)
            key.sort()
            key = "".join(key)
            if key in seen:
                seen[key].append(s)
            else:
                seen[key] = [s]
        
        ans = []
        for group in seen.values():
            ans.append(group)
        return ans


