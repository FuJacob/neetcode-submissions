class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        graph = defaultdict(list)
        indegree = {c: 0 for word in words for c in word}
        for i in range(n-1):
            word1,word2 = words[i], words[i+1]
            if len(word1) > len(word2) and word1.startswith(word2):
                ## INVALID CASE
                return ""
            
            for c1, c2 in zip(word1,word2):
                if c1 != c2:
                    ## if c2 isnt in the graph of c1 (ie already countede)
                    if c2 not in graph[c1]:
                        graph[c1].append(c2)
                        indegree[c2] +=1
                    break
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []
        while q:
            char = q.popleft()
            res.append(char)
            for nei in graph[char]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        if len(res) < len(indegree):
            return ""
        return "".join(res)
            
            
        

