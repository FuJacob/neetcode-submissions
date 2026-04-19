class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        order amont lettersi snot a bc d ...
        its diferent

        recieve non empty strings words
        sorted lexocigrapphically based on the rules of the new langage

        if order invalid retunr empty
        if mupltie valid
        return any of them

        string a is smalelr if b
        first letter differ is malelr 
        a is prefix of b and a sjhroter


        strategy is u know the list is sorted
        build a graph

        check every pair of words in that order
        if first char differ, we can build edge from that

        get indegree right
        biuld adj graph
        find indegree, if ever get cycle, return 
        otherwise, buid up a res array 
        """
        graph = defaultdict(set)
        indegree = defaultdict(int)
        n = len(words)
        all_chars = set([c for word in words for c in word])
        for i in range(n-1):
            ## check out the other words ? 
            word1, word2 = words[i], words[i+1]
                ## buidl edge
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            ptr1,ptr2 = 0,0
            for c1,c2 in zip(word1, word2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        ## dont add duplicate pairs to the indegree, it will dmangiet 
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break
        ## after this then what?
        ## lets bfs, buidl res, ever get a cycle? then we know tis wrong
        res = []
        for c in all_chars:
            indegree[c] = indegree.get(c, 0)
        ## if indegree 0, we can start there, thats our beginning
        q = deque([char for char in all_chars if indegree[char] == 0])
        ## indegree lamesk it so we only process each one once, how do we know if cycle? 
        while q:
            char = q.popleft()
            ## this ahs been processed n ready
            res.append(char)
            for nei in graph[char]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if len(res) != len(all_chars):
            return ""
        return "".join(res)



                
                

