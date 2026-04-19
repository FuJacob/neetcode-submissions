class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_to_words = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                wild_word = word[:i] + "*" + word[i+1:]
                word_to_words[wild_word].append(word) ## we can get here
        
        ## word, # of word transformed
        q = deque([(beginWord, 1)])
        visited = {beginWord} ## dont repeat visit words
        while q:
            word, num = q.popleft()
            if word == endWord:
                return num
            
            for i in range(len(word)):
                wild_word = word[:i] + "*" + word[i+1:]
                for nei in word_to_words[wild_word]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, num+1))
        return 0


