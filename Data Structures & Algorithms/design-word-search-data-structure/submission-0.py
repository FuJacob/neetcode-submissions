class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:
    """
    okay we want to design a data sructure that supports adding new words
    and searching for existing words. 

    void add word shoulda dd word to the data atsrcture

    search word should return true if any string in the data strcuture matches word
    or false wotherse
    if it has dot . then that menas it cna be matched with any letter.


    okay i think it would be simple to imeplent add word. we would just mkae a trie

    for search, it's the . that adds some complexitiy where we will ened to probably iterate trhoguh all the letters
    to see if it can end up matching something... can jist use a recursive function on each all the children

    """
    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

        

    def search(self, word: str) -> bool:
        def dfs(i, node):
            curr = node
            for i in range(i, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.end
        return dfs(0, self.root)

            


        
