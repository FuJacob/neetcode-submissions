class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        indegree = {c:0 for word in words for c in word}
        graph = defaultdict(set)
        n = len(words)
        for i in range(n-1):
            w1,w2 = words[i], words[i+1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for c1,c2 in zip(w1,w2):
                if c1 != c2:
                    ## c1 -> c2
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] +=1
                    break
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []
        while q:
            c = q.popleft()
            res.append(c)
            for nei in graph[c]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    q.append(nei)
        if len(res) < len(indegree):
            return ""
        return "".join(res)
            
                        
                        
