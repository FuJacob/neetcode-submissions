class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_to_words = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                key[idx] += 1
            str_key = ",".join([str(v) for v in key])
            sorted_to_words[str_key].append(s)
        return [l for l in sorted_to_words.values()]