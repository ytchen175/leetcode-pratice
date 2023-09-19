class TrieNode:
    def __init__(self):
        self.childrens = dict() 
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root

        for w in word:
            if w not in curr.childrens:
                curr.childrens[w] = TrieNode() # {"a": TrieNode()}
                curr = curr.childrens[w] # move to next character node, eg. get into a's TrieNode 
            else:
                curr = curr.childrens[w] # move to next character node, eg. get into a's TrieNode 
        curr.end_of_word = True # set last node as the end_of_word (EOW)

    def search(self, word: str) -> bool:
        curr = self.root
        
        for w in word:
            if w not in curr.childrens:
                return False
            else:
                curr = curr.childrens[w]

        return curr.end_of_word # if last node is not end_of_word then False, else True 

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for w in prefix:
            if w not in curr.childrens:
                return False
            else:
                curr = curr.childrens[w]
        return True # whether last node is or is not end_of_word, return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)