from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        letter_to_neis = defaultdict(list)
        indegree = {}
        for word in words:
            for c in word:
                indegree[c] = 0 ## intlaize all to 0  the charcaters used
        
        for i in range(1, n):
            word1, word2 = words[i-1], words[i]
            if len(word1) > len(word2) and word1.startswith(word2):
                ## if first word longer and startws with the toher one its cant be rue
                return ""
            
            for c1,c2 in zip(word1, word2):
                if c1 != c2:
                    letter_to_neis[c1].append(c2)
                    indegree[c2] += 1
                    break
        roots = [letter for letter, indeg in indegree.items() if indeg == 0]
        q = deque(roots)
        ans = []
        while q:
            letter = q.popleft()
            ans.append(letter)
            for nei in letter_to_neis[letter]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return "".join(ans) if len(ans) == len(indegree) else ""

