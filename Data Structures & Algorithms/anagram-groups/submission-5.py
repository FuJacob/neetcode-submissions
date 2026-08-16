class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_to_words = defaultdict(list)
        for s in strs:
            sorted_to_words["".join(sorted(s))].append(s)
        return [l for l in sorted_to_words.values()]