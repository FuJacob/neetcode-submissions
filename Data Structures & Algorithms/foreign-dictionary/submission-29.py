from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        letter_to_neis = defaultdict(list)
        indegree = defaultdict(int)

        all_letters = set()
        for word in words:
            for c in word:
                all_letters.add(c)
        
        for i in range(1, n):
            word1, word2 = words[i-1], words[i]
            ## we want to comapre this now 
            ## if one o the 2 conditosn false then we n iwt its not true 
            ## inalid of word1 si eaqual or longer 
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            ## false
            ## otherwse lets find the dirs difiernign character
            ptr = 0
            max_length = min(len(word1),len(word2))
            while ptr < max_length and word1[ptr] == word2[ptr]:
                ptr+=1
            ## first idx
            if ptr >= max_length:
                continue ## itsj ust longer it doenstt ttelll us anything
            ## word1 is smaller
            letter_to_neis[word1[ptr]].append(word2[ptr])
            indegree[word2[ptr]] += 1
        roots = [letter for letter in all_letters if indegree[letter] == 0]
        q = deque(roots)
        ans = []
        while q:
            letter = q.popleft()
            ans.append(letter)
            for nei in letter_to_neis[letter]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return "".join(ans) if len(ans) == len(all_letters) else ""

